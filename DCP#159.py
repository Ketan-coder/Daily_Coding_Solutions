"""
This problem was asked by Google.
Given a string, return the first recurring character in it, or null if there is no recurring character.
For example, given the string "acbbac", return "b". Given the string "abcdef", return null.
"""

given_recuring_string = str(input("Input string to compare: "))

string_length = len(given_recuring_string)
i = 0
string_list = []
y = []

for string_length in given_recuring_string:
    string_list.append(given_recuring_string[i])
    i = i + 1

b = set([x for x in string_list if string_list.count(x) > 1])
print("\n")
print(b)

def check_duplicate(l):
    mySet = set(l)
    if len(mySet) == len(l):
        print("\nString has no duplicate elements.\n")
    else:
        print("\nThe String contains duplicate elements\n")

check_duplicate(string_list)