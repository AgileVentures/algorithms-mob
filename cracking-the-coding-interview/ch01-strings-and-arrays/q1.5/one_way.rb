# One way
# There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character.
# Given two strings, write a function to check that they are one edit(or zero edits) away
# EXAMPLES:

# pale, ple returns true

# pales, pale returns true

# pale, bale returns true

# pale, bake returns false
def one_way(str1, str2)
    return true if str1 == str2 # constant time k
    changes = 0 # constant time

    return false if (str1.length - str2.length).abs > 1 # constant
    str1.split(//).each_with_index do |char, index| # 2 order(n)
        next if char == str2[index]
        break if changes == 1
        if str1.length < str2.length
            if str1[(index)..-1] != str2[(index + 1)..-1] # o(n)
                changes += 1
            end
        elsif str1.length > str2.length
            if str1[(index + 1)..-1] != str2[(index)..-1] # o(n)
                changes += 1
            end 
        else
            if str1[(index + 1)..-1] != str2[(index + 1)..-1] # o(n)
                changes += 1
            end
        end
    end

    return true if changes < 1 # k
    false
end
