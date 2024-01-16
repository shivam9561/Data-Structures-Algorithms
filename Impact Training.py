#l = input().split()
''''print(l)
d = {}
for i in range(0,len(l),2):
    d[l[i]] = l[i+1]
key=input()
value=input()
d.update({key:value})
#print(d)

dic = input().split()
to_find = input()
b = len(dic)
present = 0
for i in range(0, b, 2):
    if dic[i] == to_find:
        present = 1
        break
    else:
        present = 0
if present:
    print("Key is present")
else:
    print("key is not present")
#print()


def merge_dictionaries(dict1,dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict
def get_dictionary_from_user():
    dictionary = {}
    while True:
        key = input("Enter a key (or 'q' to quit): ")
        if key == 'q':
            break
        value = input("Enter a value: ")
        dictionary[key] = value'''
#  return dictionary

'''s = {1,2,3,4,5,6}
s1 = {1,2,3,7,8,9}
print(s|s1) #union
print(s&s1) #intersection
print(s-s1) #difference
print(s^s1) #symmetric difference
#print(s.intersection(s1))  
# print(s)
#print(s.symmetric_difference(s1))'''

'''s = {1,2,3,4,5,6}
s1 = {4,5,6,7,8,9}
print(s|s1)'''

'''s = 'Parul'
s = 'Pietclg'
#s[3]='1'
print(s)'''

'''import string
#print(string.ascii_letters)
#print(string.ascii_lowercase)
#print(string.ascii_uppercase)
#print(string.punctuation)
#print(string.digits)
#print(string.hexdigits)
#print(string.octdigits)'''

'''s = 'Parul'
#print(s.endswith('l'))
#print(s.startswith('P'))
#print(s.replace('a','i'))'''

#s = '1000'
#print('100'.isdigit())
#print('abc'.isalpha())
#print('ab12'.isalnum())
#print('Hello World'.istitle())
#print('hello'.upper())
#print('python'.partition('t'))
#print('hello'.index('l'))
#print('hello'.rindex('l'))
#print('py\nth\non'.splitlines())

#print('python programming'.capitalize())
#print('python cython'.find('th'))
#print('python cython'.rfind('th'))
#print('python cython'.count('th'))

#print(len('python'))
#print(max('python'))
#print(min('python'))

'''def sort_characters_and_numbers(string):
    characters = []
    numbers = []
    for char in string:
        if char.isalpha():
            characters.append(char)
        elif char.isdigit():
            numbers.append(char)
    characters.sort()
    numbers.sort()
    sorted_string = ''.join(characters + numbers)
    return sorted_string
input_string = input("Enter a string containing characters and numbers: ")
sorted_string = sort_characters_and_numbers(input_string)
print("Sorted string:", sorted_string)'''

'''def replace_vowels_with_asterisks(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    replaced_string = ""

    for char in string:
        if char in vowels:
            replaced_string += "*"
        else:
            replaced_string += char

    return replaced_string
def replace_consonants_with_at(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    replaced_string1 = ""

    for char in string:
        if char not in vowels:
            replaced_string1 += "@"
        else:
            replaced_string1 += char

    return replaced_string1
input_string = input("Enter a string: ")
replaced_string1 = replace_consonants_with_at(input_string)
print(replaced_string1)
input_string2 = input("Enter a string2:")
replaced_string = replace_vowels_with_asterisks(input_string2)
print(replaced_string)
input_string3 = input("Enter a string3:")
x=input_string3.upper()
print(x)
print(replaced_string+replaced_string1+x)'''


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        '''
        the key of this problem is, for a specific grid,
        find out its max left/right boundry,
        so the first thought is to scan from left to right and 
        right to left to get them.
        leftMaxHeights[x] represents max left boundary height for index x
        rightMaxHeights[x] represents max right boundary height for index x
        please note that len(leftMaxHeights) and len(rightMaxHeights)
        are both equal to len(height)-2 since the beginning and ending block
        cannot contain any water per problem description
        '''
'''class Solution(object):
    def trap(self, height):
        leftMaxHeights = []
        rightMaxHeights = []
        totalLen = len(height)
        if (totalLen < 3):
            return 0
        maxLeftHeight = height[0]
        for i in range(1, totalLen-1):
            leftMaxHeights.append(maxLeftHeight)
            if maxLeftHeight < height[i]:
                maxLeftHeight = height[i]            
        maxRightHeight = height[-1]
        for i in range(totalLen-2, 0, -1):
            rightMaxHeights.insert(0, maxRightHeight)
            if maxRightHeight < height[i]:
                maxRightHeight = height[i]
        
        waterVol = 0
        for i in range(1, totalLen-1):
            possibleVol = min(leftMaxHeights[i-1], rightMaxHeights[i-1]) - height[i]
            if possibleVol > 0:
                waterVol += possibleVol
        return waterVol'''

'''#Linked List front operation performed.
    class Node:
    def __init__(self, data):
        self.data = data
        self.next_address = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_front(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next_address = self.head
            self.head = new_node

    def display(self):
        if self.head is None:
            print("Empty Linked List")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data, end=' -> ')
                temp = temp.next_address
            print("None")

obj = LinkedList()
obj.insert_front('Laxman')
obj.insert_front('Ram')
obj.insert_front('Sita')
obj.display()'''

'''#Linked List End operation performed.
    class Node:
    def __init__(self, data):
        self.data = data
        self.next_address = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next_address is not None:
                temp = temp.next_address
            temp.next_address = new_node

    def insert_front(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next_address = self.head
            self.head = new_node

    def display(self):
        if self.head is None:
            print("Empty Linked List")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data, end=' -> ')
                temp = temp.next_address
            print("None")

obj = LinkedList()
obj.insert_front('Laxman')
obj.insert_front('Ram')
obj.insert_front('Sita')
obj.insert_end('Ravan')
obj.display()'''

'''class Node:
    def __init__(self, data):
        self.data = data
        self.next_address = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next_address is not None:
                temp = temp.next_address
            temp.next_address = new_node

    def insert_front(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next_address = self.head
            self.head = new_node

    def insert_after(self, prev_data, new_data):
        if self.head is None:
            print("Empty Linked List")
            return

        temp = self.head
        while temp is not None:
            if temp.data == prev_data:
                new_node = Node(new_data)
                new_node.next_address = temp.next_address
                temp.next_address = new_node
                return
            temp = temp.next_address

        print(f"{prev_data} not found in the Linked List")

    def display(self):
        if self.head is None:
            print("Empty Linked List")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data, end=' -> ')
                temp = temp.next_address
            print("None")

# Usage
obj = LinkedList()
obj.insert_front('Laxman')
obj.insert_front('Ram')
obj.insert_front('Sita')
obj.insert_end('Ravan')
obj.insert_after('Ram', 'Hanuman')
obj.display()'''

'''class Node:
    def __init__(self, data):
        self.data = data
        self.next_address = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next_address is not None:
                temp = temp.next_address
            temp.next_address = new_node

    def insert_front(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next_address = self.head
            self.head = new_node

    def insert_after(self, prev_data, new_data):
        if self.head is None:
            print("Empty Linked List")
            return

        temp = self.head
        while temp is not None:
            if temp.data == prev_data:
                new_node = Node(new_data)
                new_node.next_address = temp.next_address
                temp.next_address = new_node
                return
            temp = temp.next_address

        print(f"{prev_data} not found in the Linked List")

    def delete_front(self):
        if self.head is None:
            print("Empty Linked List")
        else:
            self.head = self.head.next_address

    def display(self):
        if self.head is None:
            print("Empty Linked List")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data, end=' -> ')
                temp = temp.next_address
            print("None")
obj = LinkedList()
obj.insert_front('Laxman')
obj.insert_front('Ram')
obj.insert_front('Sita')
obj.insert_end('Ravan')
obj.insert_after('Ram', 'Hanuman')
obj.display()

obj.delete_front()
obj.display()'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next_address = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next_address is not None:
                temp = temp.next_address
            temp.next_address = new_node

    def insert_front(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next_address = self.head
            self.head = new_node

    def insert_after(self, prev_data, new_data):
        if self.head is None:
            print("Empty Linked List")
            return

        temp = self.head
        while temp is not None:
            if temp.data == prev_data:
                new_node = Node(new_data)
                new_node.next_address = temp.next_address
                temp.next_address = new_node
                return
            temp = temp.next_address

        print(f"{prev_data} not found in the Linked List")

    def delete_end(self):
        if self.head is None:
            print("Empty Linked List")
        elif self.head.next_address is None:
            self.head = None
        else:
            temp = self.head
            prev = None
            while temp.next_address is not None:
                prev = temp
                temp = temp.next_address
            prev.next_address = None

    def display(self):
        if self.head is None:
            print("Empty Linked List")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data, end=' -> ')
                temp = temp.next_address
            print("None")
obj = LinkedList()
obj.insert_front('Laxman')
obj.insert_front('Ram')
obj.insert_front('Sita')
obj.insert_end('Ravan')
obj.insert_after('Ram', 'Hanuman')
obj.display()

obj.delete_end()
obj.display()







