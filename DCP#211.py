"""
This problem was asked by Microsoft.

Given a string and a pattern, find the starting indices of all occurrences of the pattern in the string. 
For example, given the string "abracadabra" and the pattern "abr", you should return [0, 7].
"""
string = "abracadabra"

pattern = "abr"

splited = string.split(pattern)
print(splited[0])

for i in string:
    for j in pattern:
        if i == j:
            print(i + "==" + j)
            print("Yes")