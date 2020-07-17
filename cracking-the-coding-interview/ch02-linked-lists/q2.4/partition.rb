
class Partition
  def self.call(node, partition)
    return node if node.nil? || node.next.nil?
    node = Node.from_array(node.to_a.sort)
  end
end