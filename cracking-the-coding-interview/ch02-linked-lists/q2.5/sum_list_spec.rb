require 'rspec'
require_relative 'sum_list'

RSpec.describe SumList do
  context '#call' do
    it 'returns nil for nil lists' do
      expect(described_class.call(nil, nil)).to be_nil
    end

    it 'returns the first list if the second one is nil' do
      node = Node.new(1)
      expect(described_class.call(node, nil)).to eq node
    end

    it 'returns the second list if the first one is nil' do
      node = Node.new(1)
      expect(described_class.call(nil, node)).to eq node
    end

    it 'add 2 lists with single nodes' do
      node = Node.new(1)
      expect(described_class.call(node, node)).to eq Node.new(2)
    end
    
    it 'returns 0 -> 1 when 1 and 9 are added' do
       node1  = Node.from_array([1])
       node2  = Node.from_array([9])
       result = Node.from_array([0, 1])

       expect(described_class.call(node1, node2)).to eq result
    end

    it 'returns 2 -> 0 when 0 -> 1 and 0 -> 1 are added' do
       node1  = Node.from_array([0, 1])
       node2  = Node.from_array([0, 1])
       result = Node.from_array([0, 2])

       expect(described_class.call(node1, node2)).to eq result
    end
    
    it 'returns 0 -> 0 -> 1 when 0 -> 5 and 0 -> 5 are added' do
       node1  = Node.from_array([0, 5])
       node2  = Node.from_array([0, 5])
       result = Node.from_array([0, 0, 1])

       expect(described_class.call(node1, node2)).to eq result
    end
  end
end
