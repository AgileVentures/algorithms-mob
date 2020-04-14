
# Write an algrithm that takes a non empty array and an integer representing target sum
#  The function should find all triplets in the array that sum up to the targetSum
#  and return a two dimensional array of all these triplets
# The numbers on each triplet shoi=uld be ordrered in an ascending order 
#  And the triplets themselves should be ordered in an ascending order with respect to the values they hold
#  If no three elements sum up to the target sum the function should return an empty array

## Example
# Sample input 
#     array = [12, 3, 1, 2, -6, 5, -8, 6]
#     target_sum = 0

# Sample output
# [12, 3, 1, 2, -6, 5, -8, 6]
class ThreeNumberSum():

    def __init__(self):
        pass

    def three_number_sum_using_dict(self, array, targetSum):
        target_operands = []
        for i in range(len(array)):
            outer_diff = targetSum - array[i]
            lookup_dict = {}
            for j in range(len(array)):
                if j==i:
                    continue
                inner_diff = outer_diff - array[j]
                if inner_diff in lookup_dict:
                    result = sorted([array[i], array[j], inner_diff])
                    if result not in target_operands:
                        target_operands.append(result)
                else:
                    lookup_dict[array[j]] = True
        k = lambda m: m[:]
        sorted_target_operands = sorted(target_operands, key = k)
        return sorted_target_operands

    def three_number_sum_by_first_sorting_the_list(self, array, targetSum):
        array.sort()
        result = []
        
        for i in range(len(array)):
            outer_diff = targetSum - array[i]
            start_index = i
            end_index = len(array) - 1
            
            
            while start_index < end_index:
                if start_index == i:
                    start_index += 1
                    continue
                if end_index == i:
                    end_index -=1
                    continue
                    
                current_sum = array[start_index] + array[end_index]
                if current_sum == outer_diff:
                    result.append([array[i], array[start_index], array[end_index]])
                    print()
                    end_index -= 1
                    start_index +=1
                elif current_sum > outer_diff:
                    end_index -= 1
                    
                else:
                    start_index += 1
            start_index += 1
        return result
