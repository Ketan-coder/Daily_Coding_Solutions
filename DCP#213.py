"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Snapchat.

Given a string of digits, generate all possible valid IP address combinations.

IP addresses must follow the format A.B.C.D, where A, B, C, and D are numbers between 0 and 255. 
Zero-prefixed numbers, such as 01 and 065, are not allowed, except for 0 itself.

For example, given "2542540123", you should return ['254.25.40.123', '254.254.0.123'].
"""
given_number = "2542540123"

# with open("IPAddress.txt","w") as file:
for k in range(0, int(given_number[3:6])):
    for i in range(0 , int(given_number[5:7])):
        for j in range(0, int(given_number[7:11])):
            A = int(given_number[0:3])
            B = int(k)
            C = int(i)
            D = int(j)
            # D = int(given_number[7:11])
            print(str(A) + "." + str(B) + "." + str(C) + "." + str(D))
                # file.writelines(str(A) + "." + str(B) + "." + str(C) + "." + str(D) + "\n")

# file.close()
