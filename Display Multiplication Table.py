#Using for loop.
number = int(input("Enter the number of which the user wants to print the multiplication table: "))
print ("The Multiplication Table of: ", number)    
for count in range(1, 11):      
   print (number, 'x', count, '=', number * count)    

#Using While Loop.
number = int(input("Enter the number of which user wants to print the multiplication table: "))
count = 1
print("The multilication Table of: ",number)
while count <= 10:
   number = number*1
   print(number,'x',i,'=',number*count)
   count += 1