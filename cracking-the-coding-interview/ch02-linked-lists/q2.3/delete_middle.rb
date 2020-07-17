# Delete Middle Node:
# Implement an algorithm to delete a node in the middle 
# (i.e., any node but the first and last node, not necessarily the exact middle) of a singly 
# linked list, given only access to that node.
# EXAMPLE
# Input: the node c from the linked list a - >b- >c - >d - >e- >f
# Result: nothing is returned, but the new linked list looks like a - >b- >d - >e- >f

# [a] -> [b] -> [c] -> [d] -> [f]

# input  [c]
# result [a]->[b] -> [d] -> [f]
# not delete the first node (? which one is the first node)
# not delete the last node (point to null)
require 'rspec'
require_relative '../node.rb'

class DeleteMiddleNode
  def self.call(node)
    return false if node.nil? || node.next.nil?
    node.value = node.next.value
    node.next = node.next.next
    true
  end
end

RSpec.describe DeleteMiddleNode do
 	context 'when the node is empty' do
    it 'returns false' do
      expect(DeleteMiddleNode.call(nil)).to be false
    end
  end

  context 'when the list has one node' do
    it 'returns false' do
      node = Node.new('a')

			expect(DeleteMiddleNode.call(node)).to eq false
    end

    it "doesn't modify the list" do
      node     = Node.new('a')
      expected = node.dup

      DeleteMiddleNode.call(node)

			expect(node).to eq expected
    end
  end

  context 'when the list has three nodes' do
    context 'when the node to delete is in the middle' do
      it 'returns true' do
        head = Node.new('a', Node.new('b', Node.new('c')))
        node = head.next

        expect(DeleteMiddleNode.call(node)).to eq true
      end

      it 'removes the node correctly' do
        head = Node.new('a', Node.new('b', Node.new('c')))
        expected = Node.new('a', Node.new('c'))
        node = head.next

        result = DeleteMiddleNode.call(node)

        expect([ result, head ]).to eq [ true, expected ]
      end
    end

    it 'does not delete the last node' do
      head = Node.new('a', Node.new('b', Node.new('c')))
      node = head.next.next

      expect(DeleteMiddleNode.call(node)).to eq false
    end
  end
end


# a = [1]
# def modify(n = a)
#   n << 2
# end
#
# modify(a)
# puts a
# a = [1, 2]
