def node_list_from_array(array)
  return nil if array.empty?
  result = node = Node.new(array.delete_at(0))
  array.each do |value|
    node.next = Node.new(value)
    node = node.next
  end
  result
end

RSpec.shared_examples 'sums two node lists of number digits in normal order' do
  def from_array(array)
    node_list_from_array(array)
  end

  include_examples 'sums two node lists of number digits'
end

RSpec.shared_examples 'sums two node lists of number digits in inverse order' do
  def from_array(array)
    array&.reverse!
    node_list_from_array(array)
  end

  include_examples 'sums two node lists of number digits'
end

RSpec.shared_examples 'sums two node lists of number digits' do
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
       node1  = from_array([1])
       node2  = from_array([9])
       result = from_array([1, 0])

       expect(described_class.call(node1, node2)).to eq result
    end

    it 'returns 2 -> 0 when 0 -> 1 and 0 -> 1 are added' do
       node1  = from_array([1, 0])
       node2  = from_array([1, 0])
       result = from_array([2, 0])

       expect(described_class.call(node1, node2)).to eq result
    end
    
    it 'returns 0 -> 0 -> 1 when 0 -> 5 and 0 -> 5 are added' do
       node1  = from_array([5, 0])
       node2  = from_array([5, 0])
       result = from_array([1, 0, 0])

       expect(described_class.call(node1, node2)).to eq result
    end
  end
end