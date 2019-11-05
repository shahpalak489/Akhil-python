#print
a=123
print (a)

# comment

#function
def aki():
	print("this is not right")
aki()

def square(x):
	print(x*x)
square(2)	

def addition (x,y):
	print(x+y)
addition(3,5)

def default(x,y=5):
	print(x+y)
default(10)

default(10,y=10)

default(y=10,x=2)

def multiple(*args):
	print(args)
multiple(1,2,3,4)

#variables
a="bol bhai"
print(a)

#variable scope
b=100
print(b)

def scope():
	b=200
	print(b)
scope()
print(b)

#arithmetic Operator
x=10
y=20
print(x+y)
print(x*y)
print(y-x)
print(y/x)

#comparison operator
f=30
g=23
print(f<g)
print(f>g)
print(f==g)
print(f<=g)
print(f>=g)
print(f!=g)

#assignment operator
a=1
c=2

c+= a
print(c)

c-=a
print(c)

c*=a
print(c)

c/=a
print(c)

#Logical operator
x=2
y=3
print(x>1 and y>2)
print(x==1 or y==3)
print(x==1 and y==3)

#Membership operator
x="california"
print('z' in x)
print('z' not in x)

#identity operator
a=10
b=10
print(a is b)
print(a is not b)

#Modulus
a=10
b=3
c=2
print(a%b)  # a/b
print(a%c)  # a/c 

#String operator
#slice with string
a="india"
print (a[1])

#slice with list
list1=['a1','b2','c3','d4','5re']

print(list1[2])
print(list1[2:10])
print(list1[10:])

#slice With tuple
list1=('a1','b2','c3','d4','5re')
print(list1[2])
print(list1[2:10])
print(list1[10:])

#slice With dics -- not possible
#slice with set -- not possible

#split
print(a.split('d'))
#Range
print(a[1:3])

#concatenate
b=" Is Country"
print(a+b)
#Repeat
print(a*2)
#Reverse string
print(a[::-1])
#Replace
c=a.replace('a','a is country')
print(c)
#upper case
print(a.upper())
#lower case
print(a.lower())

#change data type



#Conditional statement
x=3
y=3
z=5
if (x==y):
	print("x and y are same")

if (x==z):
	print("x and z are same")
else:
	print("x and z are different")

if (y==z):
	print("y and z are same")
elif (x==z):
	print("x and z are different")
else:
	print("i dont know")	

#switch statement


#for Loop
for k in range(0,8):
	if (k<5):
		print("k<5")
	else:
		print("k>5")

#for ...in
car=["honda","acura","benz"]
for x in car:
 print (x)
 
fruit=["banana","apple","orange"]
for aki in fruit:
 	print(aki) 
 
#for ...in...break ( it will stop for loop)
car=[2,15,19,20]
for x in car:
 	print(x)
 	if (x==15):
   		break
 
#for...in...continue ( this will not run remaining steps but will continue for loop)
for y in fruit:
	if (y=="apple"):
   	   continue
	print(y)
 
#for...in range
for x in range(4):
 	print(x)
 
for u in range(13,19):
 	print(u)
 
for no in range (102,130,5):
 	print(no)
 
#for...in...else
for no in range (5,10):
 print(no)
else:
 	print("Finally finished!")

# while loop
n = 25
while n > 20:
    print (n)
    n = n-1

#While...break
# it will stop the while execution
i = 200
while i < 215:
 print(i)
 if i == 206:
   break
 i += 2

#while...continue
#it will start exceution from begining like here when i=3 its not printing i value
for x in range(1,11,2):
    if (x == 3 or x==7):
        continue
    print(x)

#Arrays


print("**Lambda")
print("** Lambda with function name given")
akhil=lambda a: a+6
# same as def akhil(x)
#			  x+6
print(akhil(10))

akhil=lambda a,b: a+b
print(akhil(2,5))


akhil=lambda a,b,c: a+(2*b)+(3*c)
print(akhil(2,3,5))

print("**Lambda as anonymus(function name not given)")
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

print("**Lambda as anonymus with filter**")
numbers_list = [2, 6, 8, 11, 4, 12, 7, 13, 17, 0, 3, 21,10]
filtered_list = list(filter(lambda num: (num > 7), numbers_list))
print(filtered_list)

print("**Lambda as anonymus with map**")
numbers_list = [2, 6, 8, 10, 11, 4, 12, 7, 13, 17, 0, 3, 21]
mapped_list = list(map(lambda num: num % 2, numbers_list))
print(mapped_list)

print("**Comprehensions**")
print("**List Comprehensions**")
List1=(1,2,3,4,5)
x=[i for i in List1]
# same as for i in List1:
#             if....
#			print(i)
print(x)

x=[i*2 for i in List1]
print(x)

x=[i*2 for i in List1 if i==4]
print(x)

x=[i*3 for i in List1 if (i*3)<12]
print(x)

print("**Set comprehension**")
List1=[1,2,3,4,5]
x={i for i in List1}
print(x)

x={i*2 for i in List1}
print(x)

print("**see**")
x={i*2 for i in list1 if i==4}
print(x)

x={i*3 for i in List1 if (i*3)<12}
print(x)

print("**Dict  Comprehensions**")
List1={1,2,3,4,5}
x={i:i for i in List1}
print(x)

x={i:i*2 for i in List1}
print(x)

x={i:i*2 for i in List1 if i==4}
print(x)

x={i:i*3 for i in List1 if (i*3)<12}
print(x)

print("** to convert List to Tuple")
List1=['a','b','c','d']
Tuple1=tuple(List1)
print(Tuple1)

print("** To convert Tuple to List")
Tuple1=('a','b','c','d')
List1=list(Tuple1)
print(List1)

print("**to convert List to set")
List1=['a','b','c','d']
set1=set(List1)
print(set1)

print("** to convert set to list")
set1={'a','b','c','d'}
List1=list(set1)
print(List1)

print("**Tuple to set")
Tuple1=('a','b','c','d')
set1=set(Tuple1)
print(set1)

print("**Tuple to Dics")
Tuple1=('a','b','c','d')

