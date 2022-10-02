"""
This problem was asked by Facebook.
Given a number in Roman numeral format, convert it to decimal.
The values of Roman numerals are as follows:
{
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}
In addition, note that the Roman numeral system uses subtractive notation for numbers such as IV and XL.
For the input XIV, for instance, you should return 14.
"""
Roman_dic ={
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}

choices = input("Enter Character: ").upper()
print(choices)
choice_list =[]
value_list = []

def checkForCharacters(x):
    addedValue = sum(value_list)
    if len(value_list) >= 2:
        if str(choice_list[-2]) == "I" and str(choice_list[-1]) == "V":
            print("The sum of Roman Numbers: " + str(int(addedValue-2)))
        elif str(choice_list[-2]) == "I" and str(choice_list[-1]) == "X":
            print("The sum of Roman Numbers: " + str(int(addedValue -2)))
        elif str(choice_list[-2]) == "X" and str(choice_list[-1]) == "L":
            print("The sum of Roman Numbers: " + str(int(addedValue -20)))
        elif str(choice_list[-2]) == "L" and str(choice_list[-1]) == "C":
            print("The sum of Roman Numbers: " + str(int(addedValue -60)))
        elif str(choice_list[-2]) == "C" and str(choice_list[-1]) == "D":
            print("The sum of Roman Numbers: " + str(int(addedValue -200)))
        elif str(choice_list[-2]) == "C" and str(choice_list[-1]) == "M":
            print("The sum of Roman Numbers: " + str(int(addedValue -200)))
        else:
            print("The sum of Roman Numbers: " + str(addedValue))
    else:
        print("The sum of Roman Numbers: " + str(addedValue))

for choice in choices:
    if len(choices) >= 1:
        if str(choice) in Roman_dic:
            value_list.append(int(Roman_dic[str(choice)]))
            choice_list.append(choice)
        else:
            print("Please pass valid Roman Number")

checkForCharacters(choice_list)