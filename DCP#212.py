"""
This problem was asked by Dropbox.

Spreadsheets often use this alphabetical encoding for its columns: "A", "B", "C", ..., "AA", "AB", ..., "ZZ", "AAA", "AAB", ....

Given a column number, return its alphabetical column id. For example, given 1, return "A". Given 27, return "AA".
"""
Alphabets = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

choice = int(input("Enter a number: "))

if choice >= 54:
    print(Alphabets[(choice - 54)] + Alphabets[(choice - 54)] + Alphabets[(choice - 54)])
elif choice >= 27:
    print(Alphabets[(choice - 27)] + Alphabets[(choice - 27)])
else:
    print(Alphabets[(choice - 1)])
## It needs a lit bit of refactoring