class TwoNumberSum:
    def __init__(self):
        pass
    def get_two_sum_with_n_squared_time(self, array, total_sum):
        
        for i in range(len(array)):
            diff = total_sum - array[i]
            if diff in array[:i] or diff in array[i+1:]:
                return [array[i], diff]
        return []