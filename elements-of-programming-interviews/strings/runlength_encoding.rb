<<-DOC
  Strings with long blocks of repeating characters take much less space 
  if kept in a compressed representation. To obtain the compressed representation, 
  we replace each segment of equal characters in the string with the number of characters 
  in the segment followed by the character (for example, we replace segment "CCCC" with "4C"). 
  To avoid increasing the size, we leave the one-letter segments unchanged 
  (the compressed representation of "BC" is the same string − "BC").

  For example, the compressed representation of the string "ABBBCCDDCCC" is "A3B2C2D3C",
  and the compressed representation of the string "AAAAAAAAAAABXXAAAAAAAAAA" is "11AB2X10A".
  Observe that, in the second example, if we removed the "BXX" segment from the middle of the word,
  we would obtain a much shorter compressed representation − "21A". 
  In order to take advantage of this observation, we decided to modify our compression algorithm.
  Now, before compression, we remove exactly K consecutive letters from the input string.
  We would like to know the shortest compressed form that we can generate this way.
  Write a function: 
    def solution(s, k)
  that, given a string S of length N and an integer K, returns the shortest possible length of the compressed
   representation of S after removing exactly K consecutive characters from S.
DOC
def solution(s, k)
  # write your code in Ruby 2.2
  str_length = compress_string(s).length
  return str_length if s.size < k

  last_slice = ''
  (0...s.size - k).each do |index|
    slice = s[index..index + k - 1]
    next if slice == last_slice

    last_slice = slice
    new_string = s[0...index] + s[index + k...s.size]
    str_length = [str_length, compress_string(new_string).length].min
  end
  str_length
end

def compress_string(s)
  return s if s.size < 3

  i = 0
  result = ''
  while i < s.size
    j = i + 1
    j += 1 while s[j] == s[i] && j < s.size

    count = j - i
    result << (count == 1 ? s[i] : "#{count}#{s[i]}")

    i = j
  end
  result
end

p solution('AAAABBCD', 2)
p solution('AAAABBCDAAA', 2)

