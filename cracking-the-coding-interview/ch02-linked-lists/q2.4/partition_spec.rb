
require 'rspec'
require_relative '../node'
require './partition'

RSpec.describe Partition do

  def expect_valid_partition(node, partition, expected_left, expected_right)
    results_array = described_class.call(node, partition).to_a

    index = 0
    index += 1 while results_array[index] < partition

    results_left  = results_array[0...index]
    results_right = results_array[index...results_array.size]

    expect(results_left).to  contain_exactly(*expected_left)
    expect(results_right).to contain_exactly(*expected_right)
  end

  context 'when the list is empty' do
    it 'returns nil' do
      expect(described_class.call(nil, 6)).to be_nil
    end
  end

  context 'when the list has 1 element' do
    it 'returns the the list unchanged' do
      node     = Node.new(5)
      expected = node.dup

      expect(described_class.call(node, 6)).to eq expected
    end
  end

  context 'when the list has 2 element' do
    it 'puts values lower than the pivot at the beginning' do
      node     = Node.new(7, Node.new(5))
      expected = Node.new(5, Node.new(7))

      expect(described_class.call(node, 6)).to eq expected
    end

    it 'keeps the values if they are already ok' do
      node     = Node.new(5, Node.new(7))
      expected = Node.new(5, Node.new(7))

      expect(described_class.call(node, 6)).to eq expected
    end

    it 'keeps the values if they are the same' do
      node     = Node.new(6, Node.new(6))
      expected = Node.new(6, Node.new(6))

      expect(described_class.call(node, 6)).to eq expected
    end
  end

  context 'when the list has 3 elements' do
    it 'will work for 6 -> 7 -> 5' do
      node = Node.new(6, Node.new(7, Node.new(5)))

      expect_valid_partition(node, 6, [5], [6, 7])
    end

    it 'will work for 6 -> 4 -> 5' do
      node = Node.new(6, Node.new(4, Node.new(5)))

      expect_valid_partition(node, 6, [4, 5], [6])
    end
  end
end