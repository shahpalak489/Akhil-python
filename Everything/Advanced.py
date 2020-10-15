print("*** Comprehensions")

print("** convert Set comprehensions to others ")
List1=[1,2,3,4,5]
x={i for i in List1}
print(x)

print("** convert Dict  Comprehensions to others ")
List1={1,2,3,4,5}
x={i:i for i in List1}
print(x)

x={i:i*2 for i in List1}
print(x)

x={i:i*3 for i in List1 if (i*3)<12}
print(x)

print("**IMP: below comprehension examples can use for LIST, SET , DICTIONARY ")
print('* comprehension with for loop')
# for x in range(5):
#	print(x)

# same as
l1=[x for x in range(5)]
print(l1)

print('****')
# for x in range(5,15,3):
#	print(x+5)

#same as
l2=[x+5 for x in range(5,15,3)]
print(l2)

print('****')
# for i in range(5):
#	print(i*2)

# same as
x=[i*2 for i in range(5)]
print(x)

print('* multiple expressions in comprehension')
A=[4,2,5,7]
out1,out2=[],[]
# for x in range(len(A)):
#     out1.append(A[x])
#     out2.append(A[x])
# print(out1)
# print(out2)

#same as
[(out1.append(A[x]),out2.append(A[x])) for x in range(len(A))]
print(out1)
print(out2)

print('* if in comprehension')
# for a in range(10):
# 	if a>5:
# 		print(a)

#same as
p=[a for a in range(10) if a>5]
print(p)

x=[i*2 for i in tuple1 if i==4]
print(x)

x=[i*3 for i in tuple1 if (i*3)<12]
print(x)

print('* if....if  in comprehension')
# for i in range(10):
# 	if i%2==0:
# 		if i%4==0:
# 			print(i)

#same as
s=[i for i in range(10) if i%2==0 if i%4==0]
print(s)

print('*see- if....else in comprehension')
# for a in range(10):
# 	if a>5:
# 		print('a more 5')
# 	else:
# 		print('a less 5')

#same as
r=['a more 5' if a>5 else 'a less 5'for a in range(10)]
print(r)

# convert below in comprehenion  -------------------------------------------------------------------

# string='ABCDCXCDC'
# sub_string='CDC'
# y=0
# total=0
# for x in range(len(string)):
#     if string.find(sub_string,y,len(string)) == -1:
#         pass
#     else:
#         #print(string.find(sub_string,y,len(string)))
#         y = string.find(sub_string,y,len(string))+1
#         #print('y',y)
#         total += 1
# return total


# string='ABCDCXCDC'
# sub_string='CDC'
# y=0
# total=0
# total=['hi'(if string.find(sub_string,y,len(string)) == -1) else (y=string.find(sub_string,y,len(string))+1,total += 1) for x in range(len(string))]
# print(total)

#=----------------------------------------------------------------------------------------
print('*see- if ...break with comprehension')

print('* for...for loop with Comprehension')
a=['asa','dsa','dsd']
# for x in a:
# 	for y in x:
# 		print(y)

#same as
m=[y for x in a for y in x]
print(m)

print("*** Lambda- write function in 1 line")
print("** Lambda with function name")
# def akhil(x):
#    x+6

# same as
akhil=lambda x: x+6
print(akhil(10))

print('***')
# def akhil(a,b,c):
#     a+(2*b)+(3*c)

#same as
akhil=lambda a,b,c: a+(2*b)+(3*c)
print(akhil(2,3,5))

print("** Lambda as anonymus(function name not given)")
print("see-how a value is 1?")
#example 1
def myfunc(n):
  return lambda a : a-n
mytripler = myfunc(15)
print(mytripler(1))

#example 2
def testfunc(num):
    return lambda x : x * num
result1 = testfunc(10)
print(result1(9))

print("**see-Lambda as anonymus with filter**")
numbers_list = [2, 6, 8, 11, 4, 12, 7, 13, 17, 0, 3, 21,10]
filtered_list = list(filter(lambda num: (num > 7), numbers_list))
print(filtered_list)

print("**see-Lambda as anonymus with map**")
numbers_list = [2, 6, 8, 10, 11, 4, 12, 7, 13, 17, 0, 3, 21]
mapped_list = list(map(lambda num: num % 2, numbers_list))
print(mapped_list)

## mapper ?? see

print("*** Lambda by Ratan")

print('*ex 1 :one variable')
# def m1(x):
# 	print(2*x)
# m1(10)

#same as
a=lambda x: x*2
print(a(10))

print('*ex 2 : two variables')
# def m1(x,y):
# 	print(x*y)
# m1(10,20)

#same as
a=lambda x,y: x*y
print(a(10,20))

b=lambda x,y:'x is bigger' if x>y else 'y is bigger'
print(b(5,7))

print('* ex 3 :filter syntax: filter(logic,input)') 	
#use:it will return objects from input who satisfy given condition  
l1=[10,3,5,2,20]
# def m1(x):
# 	if x%2==0:
# 		return True
# 	else:
# 		return False
#print(list(filter(m1,l1)))

#same as
print(list(filter(lambda x:x%2==0,l1))) #means each l1's object is x and if x%2==0 satisy return x

print('* ex 4 - filter')
l1=['ratan','anu','durga','ratan']

# def m1(x):
# 	if x=='ratan':
# 		return True
# 	else:
# 		return False
# a=list(filter(m1,l1))			#use filter when we wants to aply logic on input
# print(a)

# same as
b=list(filter(lambda x:x=='ratan',l1))		#this means each l1's object is x and if x=ratan returns x
print(b)

print('* ex 5 :map')
#use map when we wants to apply logic on all objects input
l1=[2,3,4]
def m1(x):
	return x*5
print(list(map(m1,l1)))

#same as
print(list(map(lambda x:x*5,l1))) 	#this means each l1's object is x, apply x*5 and return x*5  

print('*ex 6')
l1=['ratan','durga']
# def m1(x):
# 	return x+'it'
# print(list(map(m1,l1)))

#same as
print(list(map(lambda x:x+'it',l1)))	#this means each l1's object is x,apply x+'it' and returns x+'it'

print('* ex 7')					#map with more than 1 inputs
l1=[1,2,3,4]
l2=[10,20,30,40]
l3=[100,200,300,400]

print(list(map(lambda x,y:x+y,l1,l2)))	
#this means l1 and l2 objects consider as x and y respectively and apply 
# x+y and returns x+y

print(list(map(lambda x,y,z:x+y+z,l1,l2,l3)))  #this means each 

print('* ex 8')
s='hi ratan sor how are you ?'
# def m1(x):
# 	y=x.split(' ')
# 	print(y)
# 	for z in y:
# 		print(len(z))
# m1(s)

# same as
words=s.split()
print(list(map(lambda x:len(x),words)))		#means words object consider as x and returns len(x)

##see -  how to apply 2 logic in lambda function??

# video 19 - 32.00
# example 9
# see - reduce 


# example 10


print("***Iterators ")
''' list is inbuilt Iteraotr because we can use For..In Loop, iter() and __next__() on List.
	that's why List , Tuple , set, disctionary are inbuilt iterators
'''

print("* for on In-built Iterators")
num=[7,8,9,5] 
for i in num:
	print (i)

print("* next on In-built Iterator")
it=iter(num)
print(it.__next__())
print(it.__next__()) 

print("***IMP: Generator/custom Iterators with yield")
print("* on custom Generator/iterator we can crate loop with for")
def akhil():
	yield 1
	yield 2
	yield 3
for i in akhil():
	print (i)

print("* on custom Generator/iterate we can create loop with __next__")
def palak():
	yield 'a'
	yield 'b'
	yield 'c' 
x=palak()
print(x.__next__())
print(x.__next__())

print("** to create custom iterator(on which we can use for..in,iter() and next function")
print("* NOT IMP:custom iterator from scratch ")
class Topten:
	def __init__(self):
		self.num=50

	def __iter__(self):
		return self

	def __next__(self):
		if self.num <= 55:
			val=self.num
			self.num += 1
			return val
		else:
			raise StopIteration

values=iter(Topten())
print(values.__next__())
print(values.__next__())
print(values.__next__())

print("** Decorator ")
print("* if 2 names are equal their functions are equal")
def succ(x):
	return x + 1

successor = succ
successor(10)
succ(10)

'''
foo = our_decorator(foo)
same as 
@our_decorator
def foo()
'''

print('*** Binary tree')
# https://www.geeksforgeeks.org/binarytree-module-in-python/

# first run on GITbash: pip install binarytree
from binarytree import Node 
root = Node(3) 
root.left = Node(6) 
root.right = Node(8) 

# Getting binary tree 
print('Binary tree :', root) 

# Getting list of nodes 
print('List of nodes :', list(root)) 

# Getting inorder of nodes 
print('Inorder of nodes :', root.inorder) 

# Checking tree properties 
print('Size of tree :', root.size) 
print('Height of tree :', root.height) 

# Get all properties at once 
print('Properties of tree : \n', root.properties) 

from binarytree import Node 
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 

# Getting binary tree 
print('Binary tree :', root) 

# Getting list of nodes 
print('List of nodes :', list(root)) 

# Getting inorder of nodes 
print('Inorder of nodes :', root.inorder) 

# Checking tree properties 
print('Size of tree :', root.size) 
print('Height of tree :', root.height) 

# Get all properties at once 
print('Properties of tree : \n', root.properties) 
  

#to create tree from list
from binarytree import build
nodes =[3, 6, 8, 2, 11, None, 13] 
  
# Builidng the binary tree 
binary_tree = build(nodes) 
print('Binary tree from list :\n', 
      binary_tree) 
  
# Getting list of nodes from
print('\nList from binary tree :',  
      binary_tree.values) 

print('Binary tree from list :\n', 
      binary_tree.properties)





