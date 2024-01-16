List = [1, 2, 3, "GFG", 2.3]
print(List)

#Creating a Lists
ages =  [19, 26, 23]
print(ages)

# Output: [19, 26, 23]

#list1 = [1, "Hello", 3.4]
#list2 = [1, "Hello", 3.4, "Hello", 1]
#list3 = []

#Accessing List Elements
#languages = ["Python", "Swift", "C++"]
#print(languages[0])
#print(languages[2])

#Negative Indexing in Python Lists
#languages = ["Python", "Swift", "C++"]
#print(languages[-1])
#print(languages[-3])

#List Slicing in Python
#my_list = ['p','r','o','g','r','a','m','i','z']
#print(my_list[2:5])
#print(my_list[5:])
#print(my_list[:])

#Add Elements to a List
#Using append()
#numbers = [21, 34, 54, 12]
#print("Before Append:", numbers)

# using append method
#numbers.append(32)
#print("After Append:", numbers)

#Using extend()
#numbers = [1, 3, 5]
#even_numbers = [4, 6, 8]
#numbers.extend(even_numbers)
#print("List after append:", numbers)

#using insert()
#numbers = [10, 30, 40]
#numbers.insert(1,20)
#print(numbers)

#Change List Items
languages = ['Python','Swift','C++']
languages[2] = 'C'
print(languages)

#Removing an Item from a List
languages = ['Python','Swift','C++','C','Java','Rust','R']
#deleting the second item
del languages[1]
print(languages)

#deleting the last time
del languages[-1]
print(languages)

#deleting the first two items
del languages[0:2]
print(languages)

#Using remove
languages = ['Python','Swift','C++','C','Java','Rust','R']
languages.remove('Python')
print(languages)

#Some Key Points - Summary
#append() - add an item to the end of the list
#extend() - add all the items of an iterable to the end of the list
#insert() - inserts an items at the specified index
#remove() - removes item present at the given index
#pop() - returns and removes item present at the given index
#clear() - removes all items from the list
#index() - returns the index of the first matched item
#count() - returns the count of the specified item in the list
#sort() - sort the list in ascending/descending order
#reverse() - reverses the item of the list
#copy() - returns the shallow copy of the list

#Iterating through a List
languages = ['Python','Swift','C++']
for language in languages:
    print(language)

#Check if an Element Exists in a List
languages = ['Python','Swift','C++']
print('C' in languages)
print('Python' in languages)

#List Length
languages = ['Python','Swift','C++']
print("List: ", languages)
print("Total Elements: ",len(languages))

#List Comprehension
numbers = [n**2 for n in range(1,6)]
print(numbers)

#Python List Operations
List = ["Geeks","For","Geeks"]
print("\nList containing multiple values: ")
print(List)

List2 = [['Geeks','For'],['Geeks']]
print("\nMulti-Dimensional List: ")
print(List2)

print("Accessing element from the list")
print(List[0])
print[List[2]]

print("Acessing element using negative indexing")
print(List[-1])
print(List[-3])

#Python Dictionary Operations
Dict = {'Name': 'Geeks', 1: [1,2,3,4]}
print("Creating Dictionary: ")
print(Dict)

print("Accessing a element using key:")
print(Dict['Name'])

print('Accessing a element using get:')
print(Dict.get(1))

myDict = {x: x**2 for x in [1,2,3,4,5]}
print(myDict)

#Python Tuple Operations
Tuple = ('Geeks','For')
print("\nTuple with the use of String: ")
print(Tuple)

List1 = [1,2,3,4,5,6]
print("\nTuple using List: ")
Tuple = tuple(List1)
print("First element of tuple")
print(Tuple[0])
print("\nLast element of tuple")
print(Tuple[-1])
print("\nThird last element of tuple")
print(Tuple[-3])

#Python Set Operations
Set = set([1,2,'Geeks',4,'For',6,'Geeks'])
print("\nSet with the use of Mixed values")
print(Set)

print("\nElements of set: ")
for i in Set:
    print(i, end = " ")
print()
print("Geeks" in Set)

#Frozen Sets
normal_set = set(["a","b","c"])
print("Normal Set")
print(normal_set)

frozen_set = frozenset(["e","f","g"])
print("\nFrozen Set")
print(frozen_set)

#String Operations
string = "Welcome to GeeksforGeeks"
print("Creating String: ")
print(string)

print("\nFirst character of String is ")
print(string[0])

print("\nLast character of String is: ")
print(string[-1])

#Bytearray Operations
a = bytearray((12, 8, 25, 2))
print("Creating Bytearray:")
print(a)

print("\nAccessing ELements:", a[1])

a[1] = 3
print("\nAfter Modifying:")
print(a)
a.append(30)
print("\nAfter Adding Elements:")
print(a)

#Counter Operations
from collections import Counter
print(Counter(['B','B','A','B','C','A','B','B','A','C']))
count = Counter({'A':3, 'B':5, 'C':2})
print(count)
count.update(['A',1])
print(count)

#OrderedDict Operations
from collections import OrderedDict
print("Before deleting:\n")
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
for key, value in od.items():
    print(key, value)
print("\nAfter deleting:\n")
od.pop('c')
for key, value in od.items():
    print(key, value)

print("\nAfter re-inserting:\n")
od['c'] = 3
for key, value in od.items():
    print(key, value)

#DefaultDict Operations
from collections import defaultdict
d = defaultdict(int)
L = [1,2,3,4,2,4,1,2]
for i in L:
    d[i] += 1
print(d)

#ChainMap Operations
from collections import ChainMap
d1 = {'a': 1, 'b':2}
d2 = {'a': 3, 'b':4}
d3 = {'a': 5, 'b':6}

c = ChainMap(d1, d2, d3)
print(c)
print(c['a'])
print(c['g'])

#Nameduple Operations
from collections import Nametuple
student = Nametuple('Student',['name','age','DOB'])
S = student('Nandini','19','2541997')
print("The student age using index is : ", end = "")
print(S[1])
print("The student name using keyname is: ",end ="")
print(S.name)

#Deque (Doubly Ended Queue) Operations
import collections
de = collections.deque([1,2,3])
de.append(4)
print("The deque after appending at right is : ")
print(de)
de.appendleft(6)
print("The deque after appending at left is : ")
print(de)
de.pop()
print("The deque after deleting from right is : ")
print(de)
de.popleft()
print("The deque after deleting from left is : ")
print(de)

#UserDict Operations
from collections import UserDict
 
# Creating a Dictionary where
# deletion is not allowed
class MyDict(UserDict):
     
    # Function to stop deletion
    # from dictionary
    def __del__(self):
        raise RuntimeError("Deletion not allowed")
         
    # Function to stop pop from
    # dictionary
    def pop(self, s = None):
        raise RuntimeError("Deletion not allowed")
         
    # Function to stop popitem
    # from Dictionary
    def popitem(self, s = None):
        raise RuntimeError("Deletion not allowed")
     
# Driver's code
d = MyDict({'a':1,
    'b': 2,
    'c': 3})
 
print("Original Dictionary")
print(d)
 
d.pop(1)

#UserList Operations
from collections import UserList
class MyList(UserList):
    def remove(self, s = None):
        raise RuntimeError("Deletion not allowed")
    
    def pop(self, s = None):
        raise RuntimeError("Deletion not allowed")
    
L = MyList([1,2,3,4])
print("Orignal List")
print(L)

L.append(5)
print("After Insertion")
print(L)
L.remove()

#UserString Operations
from collections import UserString
class Mystring(UserString):
    def append(self,s):
        self.data += s

    def remove(self, s):
        self.data = self.data.replace(s, "")

s1 = Mystring("Geeks")
print("Orignal String:", s1.data)

s1.append("s")
print("String After Appending:", s1.data)

s1.remove("e")
print("String after Removing:", s1.data)

#Linked List Operations 
#Defining Linked List in Python
class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

#Creating a simple linked list with 3 nodes.
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

if __name__=='__main__':
    list = LinkedList()
    list.head = Node(1)
    second = Node(2)
    third = Node(3)
    list.head.next = second;    #Linking first node with second
    second.next = third;        #Linking second node with the third node

#LinkedList Traversing Operation
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

if __name__=='__main__':
    list = LinkedList()
    list.head = Node(1)
    second = Node(2)
    third = Node(3)

    list.head.next = second;        #Link first node with second
    second.next = third;            #Link second node with the third node
    
    list.printList()

#Stack Operations
stack = []
stack.append('g')
stack.append('f')
stack.append('g')

print('Initial stack')
print(stack)

print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nStack after elements are popped:')
print(stack)

#Implementation using collections.deque
from collections import deque
stack = deque()
stack.append('g')
stack.append('f')
stack.append('g')
print('Initial stack:')
print(stack)
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())
print('\nStack after elements are popped:')
print(stack)

#Stack Implementation using queue module
from queue import LifoQueue
stack = LifoQueue(maxsize = 3)
print(stack.qsize())
stack.put('g')
stack.put('f')
stack.put('g')
print("Full: ", stack.full())
print("Size: ", stack.qsize())
print('\nElements popped from the stack')
print(stack.get())
print(stack.get())
print(stack.get())
print("\nEmpty: ", stack.empty())

#Stack Implementation using list
queue = []
queue.append('g')
queue.append('f')
queue.append('g')

print("Intitial queue")
print(queue)

print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print("\nQueue after removing elements")
print(queue)

#Stack Implementation using collections.deque
from collections import deque
q = deque()
q.append('g')
q.append('f')
q.append('g')

print("Initial queue")
print(q)

print("\nElements dequeued from the queue")
print(q.popleft())
print(q.popleft())
print(q.popleft())

print("\nQueue after removing elements")
print(q)

#Stack Implementaton using the queue.Queue
from queue import Queue

q = Queue(maxsize = 3)

print(q.qsize())

q.put('g')
q.put('f')
q.put('g')

print("\nFull: ", q.full())

print("\nElements dequeued from the queue")
print(q.get())
print(q.get())
print(q.get())

print("\nEmpty: ", q.empty())
print("Full: ", q.full())

#Priority Queue Implementations
class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def insert(self, data):
        self.queue.append(data)

    def delete(self):
        try:
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max]:
                    max = i 
            item = self.queue[max]
            del self.queue[max]
            return item
        except IndexError:
            print()
            exit()

if __name__== '__main__':
    myQueue = PriorityQueue()
    myQueue.insert(12)
    myQueue.insert(1)
    myQueue.insert(14)
    myQueue.insert(7)
    print(myQueue)
    while not myQueue.isEmpty():
        print(myQueue.delete())