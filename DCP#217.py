"""
This problem was asked by Oracle.
We say a number is sparse if there are no adjacent ones in its binary representation. 
For example, 21 (10101) is sparse, but 22 (10110) is not. 
For a given input N, find the smallest sparse number greater than or equal to N.

Do this in faster than O(N log N) time.
"""
inputed_number = int(input("Input a number: "))
binary_number = bin(inputed_number)
print(str(inputed_number) + " -> " + str(binary_number))

sparse = False
values_list = []

# This function checks the number of ones in the binary from the input
def maxConsecutiveOnes(x):
    count = 0
    # Count the number of iterations to
    # reach x = 0.
    while (x!=0):
        # This operation reduces length
        # of every sequence of 1s by one.
        # (x = (x & (x << 1))) == (x = (x & (2*x)))
        # & -> LOGICAL AND it can be denoted (x AND (2*x))
        x = (x & (2*x))
        count=count+1
     
    return count

#This function finds the closest sparse number according to the given number
def findClosestSparseNum(x):
    count = 0
    if len(str(inputed_number)) == 1:
        for i in range((int(inputed_number) - 1), (int(inputed_number) + 1)):
            if maxConsecutiveOnes(i) > 1:
                pass
            else:
                count = count + 1
                values_list.append(i)
    elif len(str(inputed_number)) >= 2:
        for i in range((int(inputed_number) - 5), (int(inputed_number) + 5)):
            if maxConsecutiveOnes(i) > 1:
                pass
            else:
                count = count + 1
                values_list.append(i)
    return count


if maxConsecutiveOnes(inputed_number) > 1:
    print("This is not Sparse")
    #Calling the findClosestSparseNum function
    findClosestSparseNum(int(inputed_number))
    if len(values_list) > 0:
        print("The closest sparse number are/is: ")
        for values in values_list:
            print(str(values) + " -> " + str(bin(values)))
    else:
        print("There is no closest sparse number.")
    
else:
    sparse = True
    print("WOW! You found a Sparse number!")