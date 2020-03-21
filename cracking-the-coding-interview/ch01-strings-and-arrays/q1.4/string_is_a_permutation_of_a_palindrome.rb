## Palindrome Permutation:
	#Given a string, write a function to check if it is a permutation of a palindrome.
	#A palindrome is a word or phrase that is the same forwards and backwards.
	#A permutation is a rearrangement of letters. 
	#The palindrome does not need to be limited to just dictionary words.
	#Input: "Tact Coa"
	#Output: True (permutations: "taco cat", "atco eta"

def is_a_permutation_of_a_palindrome(s) # lengh(s) = n
    character_hash = {}
    s.downcase! # n loops
    s.tr(' ', '').split(//).each do |char| # 3*n loops
        if character_hash.key?(char) # constant
            character_hash[char] += 1 # constant
        else
            character_hash[char] = 1 # constant
        end
    end
    odd = 0

    character_hash.values.each do |val| # less or equal n loops
        if val % 2 == 1 # constant
            odd += 1  # constant
        end
    end
    p character_hash
    
    if odd > 1 # constant
        return false # constant
    end
    return true
end

# 4*n loops => it's linear (length of the string)

p is_a_permutation_of_a_palindrome('aabb')
p is_a_permutation_of_a_palindrome('aabba')
p is_a_permutation_of_a_palindrome('aab ba')
p is_a_permutation_of_a_palindrome('aab bba')
p is_a_permutation_of_a_palindrome('Tact Coa')

# Test : if there are more than two charecters with an odd number of instance => not a permutation of a palindrom


