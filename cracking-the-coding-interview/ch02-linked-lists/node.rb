class Node
	attr_accessor :value, :next

	def self.from_array(array)
		return nil if array.empty?
		result = node = Node.new(array.first)
		1.upto(array.size - 1) do |index|
			node.next = Node.new(array[index])
			node = node.next
		end
		result
	end

	def initialize(value, next_node = nil)
		@value = value
		@next = next_node
	end

	def ==(node)
		to_a == node.to_a
	end

	def to_a
		# I am recursive!
		# nil.to_a => []
		[value] + self.next.to_a
	end

	def to_s
		to_a.join(', ')
	end

	def inspect
		to_a.join(' -> ')
	end
end