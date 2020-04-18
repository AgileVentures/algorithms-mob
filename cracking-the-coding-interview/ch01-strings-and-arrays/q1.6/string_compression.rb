# String compressions
# Implement a basic method to perform a basic string compression using the counts of repeated characters. 
# For example the string "aabcccccaaa" would become a2b1c5a3
# If the "compressed" string would not become smaller than the original string, 
# you should return the original string
# you can assume that the string has only uppercase and lowercase letters

def string_compression(to_compress)
    if to_compress.length < 3
        return to_compress
    end
    counter = 1
    compressed_string = ''
    curr_char = ''
    to_compress.each_char do |c|
        if c != curr_char 
            if curr_char != ''
                compressed_string << "#{curr_char}#{counter}"
            end
            counter = 1
            curr_char = c
        else
            counter += 1
        end
        return to_compress if compressed_string.length >= to_compress.length 
    end
    if curr_char != ''
        compressed_string << "#{curr_char}#{counter}"
    end
    compressed_string
end



