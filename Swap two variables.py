P = int(input("Please enter value for P: "))
Q = int(input("Please enter value for Q: "))
temp_1 = P
P = Q
Q = temp_1
print("The value of P after swapping: ",P)
print("The value of Q after swapping: ",Q)

#Using Comma Operator
P = int(input("Please enter value for P: "))
Q = int(input("Please enter value for Q: "))
P,Q = Q,P
print("The value of P after swapping: ".P)
print("The value of Q after swapping: ",Q)

#Using XOR method.
P =int(input("Please enter value for P: "))
Q = int(input("Please enter value for Q: "))
P = P^Q
Q = P^Q
P = P^Q
print("The value of P after swapping: ",P)
print("The value of Q after swapping: ",Q)

#Using Arithmetic Operators
P =int(input("Please enter value for P: "))
Q = int(input("Please enter value for Q: "))
P = P+Q
Q = P-Q
P = P-Q
print("The value of P after swapping: ",P)
print("The value of Q after swapping: ",Q)

#Using Multiplication and Division operator.
P =int(input("Please enter value for P: "))
Q = int(input("Please enter value for Q: "))
P = P*Q
Q = P/Q
P = P/Q
print ("The Value of P after swapping: ", P)  
print ("The Value of Q after swapping: ", Q)  

