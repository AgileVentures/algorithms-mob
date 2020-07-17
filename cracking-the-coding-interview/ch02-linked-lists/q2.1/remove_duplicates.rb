# Remove Dups: Write code to remove duplicates from an unsorted linked list. 
#  FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?

require 'set'
require_relative 'node'
class RemoveDuplicates
	def call(head)
		node_values = Set[]
		node_values << head.value
		node = head
		while node.next
			if node_values.include?(node.next.value)
				node.next = node.next.next
			else
				node_values << node.next.value
				node = node.next
			end
		end
		head
	end
	
	# 1 -> 2 -> 2 -> 3
	# {}
	# {1}
	# {1, 2, 3}
	# 1 -> 2 -> 3


	def remove_duplicates_without_extra_memory(head)
		# thoughts 
		# sort the linked list (o(n)?)
		# remove duplicates from the sorted linked list

		# fist value, iterate from secon to end and see 
		# B -> B
		# remove_value_from_list(head, value)
		base_node = head
		while base_node && base_node.next 
			node = base_node
			while node && node.next
				next_node = node.next
				if next_node.value == base_node.value
					node.next = next_node.next # skip next_node
				else
					node = node.next # go to the next
				end
			end
			base_node = base_node.next
		end	
		head
	end
end

list = Node.new('B', Node.new('B',  Node.new('B')))
# RemoveDuplicates.new.call(list)
puts list
RemoveDuplicates.new.remove_duplicates_without_extra_memory(list)
p list.to_a
puts list
p list

