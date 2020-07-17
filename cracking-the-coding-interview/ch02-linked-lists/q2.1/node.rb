class Node
	attr_accessor :value, :next

	def initialize(value, next_node = nil)
		@value = value
		@next = next_node
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