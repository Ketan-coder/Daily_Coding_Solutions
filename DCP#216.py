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

def checkForCharacters(x:list):
    # for choices in choice_list:
    #     for secondChoice in choice_list:
    #         if choices == "I" and secondChoice == "V":
    #             print(Roman_dic[str(secondChoice)] - Roman_dic[str(choice)])
    print(choice_list[-2])
    if choice_list[-2] == "I" and choice_list[-1] == "V":
        print(sum(value_list)-1)


for choice in choices:
    if len(choices) >= 1:
        if str(choice) in Roman_dic:
            # print(Roman_dic[str(choice)])
            value_list.append(int(Roman_dic[str(choice)]))
            choice_list.append(choice)
        else:
            print("Please pass valid Roman Number")

checkForCharacters(choice_list)

# print()
print(choice_list)