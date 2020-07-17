require_relative '../node'
require_relative 'sum_list'

class SumInvertedList < SumList
  def self.call(list1, list2)
    super(invert(list1), invert(list2))
  end

  private

  def self.invert(list)
    Node.from_array(list.to_a.reverse!)
  end
end