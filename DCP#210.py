"""
This problem was asked by Apple.

A Collatz sequence in mathematics can be defined as follows. Starting with any positive integer:

if n is even, the next number in the sequence is n / 2
if n is odd, the next number in the sequence is 3n + 1
It is conjectured that every such sequence eventually reaches the number 1. Test this conjecture.

Bonus: What input n <= 1000000 gives the longest sequence?
"""

num = int(input("Enter a number: "))

for i in range(0, int(num)):
    print(str(i))
    if i % 2 == 0:
        print(str(i/2) + "\n")
    else:
        print(str((3*i)+1) + "\n")