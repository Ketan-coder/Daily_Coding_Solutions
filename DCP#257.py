"""
This problem was asked by WhatsApp.

Given an array of integers out of order, 
determine the bounds of the smallest window that must be sorted in order for the entire array to be sorted. 
For example, given [3, 7, 5, 6, 9], you should return (1, 3).
"""
numbers = []
choice =  int(input("Enter the n numbers: "))

for i in range(0, choice):
    num = int(input("Enter the numbers: "))
    numbers.append(num)

print(numbers)

# number_list = []
sorted_list = sorted(numbers)

if sorted_list[2] and sorted_list[3] != "":
    if (sorted_list[1] - sorted_list[0]) == (sorted_list[2] - sorted_list[3]):
        print("this is a sequence = ( " +  str(sorted_list[1] - sorted_list[0]) + "," + str(sorted_list) + " )")
    else:
        print("it is not a sequence")
else:
    print("Give more values to calculate if it is a sequence or not.")

# for number1 in numbers:
#     for number2 in numbers:
#         if number1 > number2:
#             sorted_list.append(number2)
#             sorted_list.append(number1)
#         elif number2 > number1:
#             sorted_list.append(number1)
#             sorted_list.append(number2)
#         else:
#             sorted_list.append(number1)

print(sorted_list)