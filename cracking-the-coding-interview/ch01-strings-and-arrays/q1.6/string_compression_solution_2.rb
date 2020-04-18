# String compressions
# Implement a basic method to perform a basic string compression using the counts of repeated characters. 
# For example the string "aabcccccaaa" would become a2b1c5a3
# If the "compressed" string would not become smaller than the original string, 
# you should return the original string
# you can assume that the string has only uppercase and lowercase letters

class StringPress
    def compress(string)
      result = +''
      return string if string.size < 3
      i = 0
      j = 1
      count = 1
      while i < string.size
        current_char = string[i]
        next_char    = string[j]
        while next_char == current_char
          count += 1
          j     += 1
          next_char = string[j]
        end
        result << "#{current_char}#{count}"
        return string if result.size >= string.size
        i     = j
        count = 0
      end
      result.size < string.size ? result : string
    end
    
    def compress_word(string)
      return string if string.length < 3
      counter = 1
      new_string = +''
      previous_character = string[0]
      i = 1
      while i < string.length
        while previous_character == string[i]
          counter += 1
          i += 1
        end
        new_string << "#{previous_character}#{counter}"
        counter = 1
        previous_character = string[i]
        i += 1
        return string if new_string.length >= string.length
      end
      return new_string
    end
  end
