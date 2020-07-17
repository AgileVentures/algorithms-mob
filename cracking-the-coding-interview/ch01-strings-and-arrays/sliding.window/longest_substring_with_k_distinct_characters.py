# Given an array arr and an integer k, find the longest substring with k distinct characters in

# Examples

#  input ['A', 'A', 'A', 'H', 'H', 'I', 'B', 'C'], 2 output: 5

def longest_substring_with_k_distinct_characters(arr, k):
    max_len = 0
    start_index = 0
    from collections import defaultdict
    character_dict = defaultdict(0)

    for i in arr:
        character_dict[i] =+ 1
        while 