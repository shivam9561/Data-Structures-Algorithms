a = float(input('Enter first side of triangle: '))
b = float(input('Enter second side of triangle: '))
c = float(input('Enter third side of triangle: '))

#Calculating semi perimeter formula.
s = (a+b+c)/2

#Calculating Area of Triangle.
area = (s*(s-a)*(s-b)*(s-c))**0.5
print('The area of the triangle is %0.2f' %area)