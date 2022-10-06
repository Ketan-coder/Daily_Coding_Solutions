"""
This problem was asked by Microsoft.

Given a string and a pattern, find the starting indices of all occurrences of the pattern in the string. 
For example, given the string "abracadabra" and the pattern "abr", you should return [0, 7].
"""
string = "abracadabra"

pattern = "abr"

splited = string.split(pattern)

listToStr = ''.join(map(str, splited))
print(listToStr)

if string == listToStr:
    print('Same')
else:
    print('Different')