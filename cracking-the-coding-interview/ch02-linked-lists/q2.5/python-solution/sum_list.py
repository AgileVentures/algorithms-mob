
class Node:
    def __init__(self, val, next_node = None):
        self.val = val
        self.next_node = next_node
    
    def __str__(self):
        node = self
        result = [str(node.val)]
        while(node.next_node is not None):
            node = node.next_node
            result.append(str(node.val))
        return ''.join(result)

class ListUtils:
    class __SumPartialResult:
        def __init__(self, result_list, carry):
            self.result_list = result_list
            self.carry = carry

    def add(self, list_1, list_2):
        len_list_1 = self.__length(list_1)
        len_list_2 = self.__length(list_2)

        if len_list_1 > len_list_2:
            list_2 = self.__pad_list(list_2, len_list_1 - len_list_2)
        elif len_list_1 < len_list_2:
            list_1 = self.__pad_list(list_1, len_list_2 - len_list_1)

        result = self.__sum_lists(list_1, list_2)
        if(result.carry > 0):
            return self.__add_head(result.result_list, Node(result.carry))
        
        return result.result_list

    def __sum_lists(self, l1, l2):
        if l1 is None and l2 is None:
            return self.__SumPartialResult(result_list = None, carry = 0)

        partial_result = self.__sum_lists(l1.next_node, l2.next_node)
        partial_sum = partial_result.carry + l1.val + l2.val
        carry, partial_sum = divmod(partial_sum, 10)
        
        new_digit = Node(partial_sum)
        return self.__SumPartialResult(result_list = self.__add_head(partial_result.result_list, new_digit), carry = carry)

    def __length(self, l):
        node = l
        result = 0
        while(node is not None):
            result += 1
            node = node.next_node
        return result
    
    def __pad_list(self, l, length):
        for i in range(length):
            l = self.__add_head(l, Node(0))
        return l

    def __add_head(self, l, new_head):
        new_head.next_node = l
        return new_head

    
def test(l1, l2):
    utils = ListUtils()
    print(utils.add(l1,l2))

l1 = Node(1, Node(0, Node(1)))
l2 = Node(9)
test(l1, l2)

l1 = Node(1)
l2 = Node(9)
test(l1, l2)

l1 = Node(1)
l2 = Node(1)
test(l1, l2)