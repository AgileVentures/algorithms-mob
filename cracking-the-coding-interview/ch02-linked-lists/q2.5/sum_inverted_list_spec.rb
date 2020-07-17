require 'rspec'
require_relative 'sum_inverted_list'
require_relative 'shared_examples/sums_two_node_lists.rb'

RSpec.describe SumInvertedList do
  include_examples 'sums two node lists of number digits in normal order'
end
