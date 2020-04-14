# Write a function that takes two non empty arrays of integers,
# finds the pair(one from each array) whose absolute difference is closest to zero
# and returns an array containing the two numbers,
# with the number from the first array in the first position. 
# You can assume there will only be one pair of numbers with the smallest difference

class SmallestDifference:
    
    def __init__(self):
        pass
    
    def smallest_difference(self, arr_1, arr_2):
        arr_1.sort()
        arr_2.sort()
        current_diff = min_diff = float('inf')
        arr_1_index = arr_2_index = 0
        closest_pair = []

        while arr_1_index < len(arr_1) and arr_2_index < len(arr_2):
            first_array_element = arr_1[arr_1_index]
            second_array_element = arr_2[arr_2_index]
            current_diff = first_array_element - second_array_element
            if current_diff < min_diff:
                    min_diff = current_diff
                    closest_pair = [first_array_element, second_array_element]
            if  first_array_element < second_array_element:
                arr_1_index += 1
            
            elif second_array_element < first_array_element:
                arr_2_index += 1
            
            else:
                return [first_array_element, second_array_element]
        
        return closest_pair


