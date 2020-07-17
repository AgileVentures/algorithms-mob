require 'rspec'
require_relative 'sum_list'
require_relative 'shared_examples/sums_two_node_lists.rb'

RSpec.describe SumList do
  include_examples 'sums two node lists of number digits in inverse order'
end