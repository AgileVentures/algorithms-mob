# Sum Lists: You have two numbers represented by a linked list, 
# where each node contains a single digit. The digits are stored
# in reverse order, such that the 1's digit is at the head of the list. 
# Write a function that adds the two numbers and returns the sum as a linked list.
#
# EXAMPLE
# Input: (7-> 1 -> 6) + (5 -> 9 -> 2). That is, 617 + 295.
# Output: 2 -> 1 -> 9. That is, 912.
#
# FOLLOW UP
# Suppose the digits are stored in forward order. Repeat the above problem. EXAMPLE
# Input: (6 -> 1 -> 7) + (2 -> 9 -> 5). That is, 617 + 295. Output: 9 -> 1 -> 2.That is, 912.

require '../node.rb'


class SumList
  ListSumDigitResult = Struct.new(:value, :carry) do
    def something?
      value + carry > 0
    end
  end

  def self.call(list1, list2)
    if list1.nil? || list2.nil?
      return list1.nil? ? list2 : list1
    end

    digit_sum = add_digits(list1&.value, list2&.value)
    head = result = Node.new(digit_sum.value)

    loop do
      list1 = list1&.next
      list2 = list2&.next

      digit_sum = add_digits(list1&.value, list2&.value, digit_sum.carry)
      return head unless digit_sum.something?
      result.next = Node.new(digit_sum.value)
      result = result.next
    end
  end

  def self.add_digits(digit1, digit2, carry = 0)
    digit1 ||= 0
    digit2 ||= 0

    sum = digit1 + digit2 + carry
    return ListSumDigitResult.new(sum % 10, sum / 10)
  end
end