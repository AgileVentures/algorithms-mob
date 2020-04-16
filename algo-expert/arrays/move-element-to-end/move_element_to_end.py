class MoveElementToEnd:

    def __init__(self):
        pass

    def move_element_to_end(self, array, to_move):
        start_index = 0 
        end_index = len(array) - 1

        while start_index < end_index:
            while start_index < end_index and array[to_move] == array[end_index]:
                end_index -= 1
            if array[start_index] == array[to_move]:
                array[start_index], array[end_index] = array[end_index], array[start_index]
            start_index += 1
        
        return array
