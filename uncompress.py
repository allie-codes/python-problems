def uncompress(s):
  # use to check string for digits
  numbers = '1234567890'
  # empty result to put output into
  result = ""
  # one of the pointers
  i = 0
  # one of the pointers
  j = 0
  # while j < the entire length of the string
  while j < len(s):
    if s[j] in numbers:
      j += 1
    else:
      num = int(s[i:j])
      result += s[j] * num
      j += 1
      i = j
    
  return result

print(uncompress("4s2b"))
print("hello world")