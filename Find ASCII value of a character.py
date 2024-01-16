'''K = input("Please enter a character:")
print ("The ASCII value of '" + K + "' is ", ord(K)) '''

#Example 2
print("Please enter the String: ",end = "")
string = input()
string_length = len(string)
for K in string:
    ASCII = ord(K)
    print(K,"\t",ASCII)

