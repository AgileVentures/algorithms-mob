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
