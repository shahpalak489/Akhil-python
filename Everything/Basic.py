print("****print")
print('*print string,int and float')
eid,ename,esal=111,'ratan',100.45
print(eid)
print(ename)
print(esal)

print('*print hard code value and variable together')
print('Emp id=',eid)
print('Emp name=',ename)
print('Emp sal=',esal)

print('Emp id=',eid,'Emp name=',ename,'Emp sal=',esal)

print('*print 2 lines together')
print(eid,end='') 				 # this will print next line, in same line
print(' ',ename)

print('*print with separator')
print(10,20,30,sep='*')

print('*print List')
L2=[]
print(L2)

L3=list('ratan') 			#this will create list of 'ratan' string
print(L3)

print('*print Dics')
d1={111:'ratan',222:'anu',333:'durga'}
print(d1)

print('*print duplicate keys,duplicate values')
d2={111:'ratan',111:'surya',222:'surya'}	  #duplicate keys will be override  	#duplicate values will be ok
print(d2)

print('***formate specifier')		#mainly use as variable in print statement
'''
Method 1
int 	float		string    
%d 	%g   %f 	  %s

Method 2
{}
'''

eid,ename,esal=111,'ratan',100.45

print('*print int,string,float with formate specifier')
# for % , if %d is first its value must be first...so its sequence is important

print('%d %s %g' %(eid,ename,esal))					#format
print('emp id =%d emp name =%s emp sal=%g' %(eid,ename,esal))

# difference between %g and %f
# %f prints upto 12 digits while %g prints data upto 6 digits only
a=123.456879
print('value of a=%g'%(a)) 

a=123456.87958418641684888
print('value of a=%f'%(a)) 

print('*print {} python specifier example')
#{} is very flexible 
print('emp id ={} emp name ={} emp sal={}'.format(eid,ename,esal))
print('emp id ={2} emp name ={0} emp sal={1}'.format(eid,ename,esal))

d1={1:'ratan',3:'anu',4:'surya',2:'durga'}
for key in sorted(d1.keys()):
	print("key=%d values=%s"%(key,d1[key]))
	
print("***Datatypes")
'''
Number : int float : 10,20   5.25, 10.29
string : str : 'ratan' "ratan"
Boolean : bool : True  False 
				   1    0
'''
evalue = 12
ename = 'ratan'
esalary = 100.92
ebool=True

print('* how to know who is number, string ,boolean, List, tuple or Dics')
print(type(evalue))
print(type(ename))
print(type(esalary))
print(type(ebool))

L1=[10,20,30,40]
print(L1)
print(type(L1))

d1={111:'ratan',222:'durga'}
print(type(d1))

print("***function")
def aki():
	print("this is not right")
aki()

print('function - required argument')
def square(x):
	print(x*x)
square(2)	
 
def addition (x,y):
	print(x+y)
addition(3,5)

print('function - keyword argument')
def default(x,y=25,z=5):  #IMP:first give non-default value then default value
	print(x+y+z)

default(10)   #here y=25,z=5 default value and x=10 because we gave w value while calling  
default(10,20) #here z=5 because while calling we gave x=10,y=20
default(y=10,x=2) #if we change sequence of variable then we need to specify x=2 
#default(20,y=40,30) # Invalid : once we give y=40 then rest of all argument must be z=something .we can not put just 30 
default(50,60,z=10)  # valid

print("***to call function")
print("IMP: '()' this symbol call function")
def a1():
	print("a1")
a1() 					# this will call function a1

print("***IMP")
def akhil():
	print("akhil")
a3=akhil() 				# this will call akhil function
   
def a(x):
	print(x+10)
b=a
b(2) 					 # this will call function a

print("***to call 1 function inside another function")
def g():
    print("Hi, it's me 'g'")
    print("Thanks for calling me")
def f(func):
    print("Hi, it's me 'f'")
    print("I will call 'func' now")
    func() #func=g  #step2: this will call function g
f(g) #step 1: this will call function f

print("***function within function")
def outside():
	def inside():
		print("i am inside") #step2
	print("i am outside") #step1
	inside() # this will call function inside
outside() # this will call function outside

print("***No call")
def inner1(): 
    print("Hello, this is before function execution") 
    func() # this will not call func unction
    print("This is after function execution")
    return inner1

print('function with n number of arguments')
#case 1
def multiple(*a):					# for n number of arguments use *
	print(a)
multiple(1,2,3,4)

def star(*ar):
	for x in ar:
		print(x)
star(10,20,30)

#case 2
def star(car,*arg):
	print(car)
	for x in arg:
		print(x)
star("honda",10,20,30)

def star(*b,car):
	print(car)
	for x in b:
		print(x)
star(49,81,car='accord') #in this case, use keyword arguments 

#case 3.
def star(name='ratan',*b):
	print(name)
	for x in b:
		print(x)
star(35,94,100)  # here name=35,and *b=94,100

#case 4
def star(name1,name='ratan',*b):
	print(name1)
	for x in b:
		print(x)
star(35,94,100,90)  #here name1=35,name=94 and *b=100,90

#case 5
def star(name1,*b,name='ratan'):
	print(name1)
	for x in b:
		print(x)
star(35,94,100,90)  #here name1=35 and *b=94,100,90

#case 3
def star(name1,*b,name='ratan'):
	print(name1)
	for x in b:
		print(x)
	print(name)
star(35,94,100,90,name='tata')  #here name1=35 and *b=94,100,90 and name='tata'

print("***Return (IMP)")
def function_that_prints():
    print("I printed")

def function_that_returns():
    return "I returned"
    print("after return")

print("IMP - The return statement terminates the execution of a function")
print("IMP - function calling  will give only print values,not return values ")
f1 = function_that_prints() #this will call function_that_prints
f2 = function_that_returns() # this will call function_that_returns

print("IMP - to access return values assign variable to function calling")
print("and print the variable because retuen assigns value to function") 
print("so we need to print calling function ")
print(f1) 
# or

print(function_that_prints()) 

print(f2)
# or
print(function_that_returns())
 
print("example 2")
def no_return(x,y):
    c = x + y
    return c
print(no_return(4,5))

# Multiple return statement
def disp():
	print('good morning')
	return 10
	return 20			    #ignored
	print('good evening')		    #ignored

disp()

# default return value is none

print("***local & global variable")
#case 1
print('*all function can use global variable value')
name='ratan'  					# global variable
def disp1():
	print('good morning',name)

def disp2(value1,value2):
	print(value1+value2)        # local variable
	print('good afternoon',name)
disp1()
disp2(3,10)

#case 2 
print('*when local and global variable has same name then priority goes to local varibale')
#Example 1
b=100
print(b)
def scope():
	b=200
	print(b)
scope()
print(b)

#Example 2
g,h=10,20
def sarvado(g,h):
	print(g+h)
sarvado(2,3)

#case 3 
print('*inside function for local variables get global variable value when both variables are same name')
#example 1
g,h=10,20
def sarvado(g,h):
	print(globals()['g']+h)  #here we get g=10 value as global variable
sarvado(2,3)
#example 2
a=15
def m1():
	a=20
	print(globals()['a'])
m1()

#case 4
print('*to create global variable inside function')
def disp3():
	global s 
	s='ratan'
	print(s)
disp3()				#function must be executed to declare global variable
print(s)

#Case 5 
print('to update Global variable value')
name='ratan'
def outer():
	name1='durga'
	def inner():
		name1='sunny'
		global name
		name='ratan IT'
	print(name1) 
	inner()
	print(name1)
outer()
print(name)

#case 6 (VV IMP)
print('*once we use global variable inside function we can not declare same variable as local variable')
# below code will give error
'''
name='ratan'
def tution():
	print(name)  	# used 'name' as global variable
	name='durga'  	# after using name as global variable we can not declare same vaiable as local
	print(name)		# UnboundLocalError: local variable 'a' referenced before assignment
tution()
'''

#case 7 - VV IMP
print('*to chnage parent function variable value from child function' )
#example 1
def m1():
	a=20
	def m2():
		nonlocal a
		a=30
	m2()				#this function calling is must to update value of a
	print(a)
m1()

#example 2
# in below example we are chaning name1 variable value, inside child function using nonlocal keyword
# because of this name1 value changes foreever
name='ratan'
def outer():
	name1='durga'
	def inner():
		nonlocal name1  # this will update parent name1 variable
		name1='sunny'
		global name
		name='ratan IT'
	print(name1) 
	inner()					#this function calling is must to update value of name1
	print(name1)
outer()
print(name)

print("***arithmetic Operator")
# +,-,*,/
x=10
y=20
print(x+y)
print(x*y)
print(y-x)
print(y/x)

print("***exponent")
x=10
n=2
print(x**2)

print("***relation operator")
# <, >, <= ,>= !=
print('for number')
f=30
g=23
print(f<g)
print(f>g)
print(f==g)
print(f<=g)
print(f>=g)
print(f!=g)

print('for string') 		# compare based on ASCI value
print('ratan' > 'anu')
print('ratan' < 'anu')
print('ratan' >= 'anu')
print('ratan' <= 'anu')
print('ratan' == 'anu')
print('ratan' != 'anu')

print("***assignment operator**")
# +=, -=, *= ,/=
x += y
#Example-1
x=10
y=20
x+=y
print(x)
#example-2
x=0
for y in [1,2,3]:
	x += y
print(x)

#explanation
'''
x=0+1=1
x=1+2=3
x=3+3=6
'''

x-=y
#Example 
x=0
for y in [1,2,3]:
	x -= y
print(x)

#explanation
'''
x=0-1=-1
x=-1-2=-3
x=-3-3=-6
'''

x*=y
#Example
x=2
for y in [1,2,3]:
	x *= y
print(x)

#explanation
'''
x=2*1=2
x=2*2=4
x=4*3=12
'''

x/=y0
#Example
x=4
for y in [1,2,3]:
	x /= y
print(x)

#explanation
'''
x=4/1=4
x=4/2=2
x=2/3=0.6
'''

print("***Logical operator")
#and,or
x=2
y=3
print(x>1 and y>2)
print(x==1 or y==3)
print(x==1 and y==3)

print('*to check given value present or not and gets True/false')
print("Membership operator")
x="california"
print('z' in x)
print('z' not in x)

x=['india','ab','ssss']
print ("ab" in x)

print('*to check given value present or not and gets its index')
# difference between in and Find --> in returns true / false , find returns indexing of given word
print('***Find')		# if avaiable returns index else returns -1
print('for string')
a='welcome to RatanIT'
print(a.find('Ratan'))
print(a.find('anu')) 

print('*to get index of alphabet/string')
print('***Index')			#returns index of given word
print('For string')
print(a.index('come'))

#to get index of alphabet/string in given range
print(a.index('t',10,15))		# return index of 't' between 10 to 15 index
#print(a.index('anu'))			#this will return error bcoz 'anu' is not in a

print('- for List')
l1=['ratan','anu','durga','ratan']
print(l1.index('ratan'))		# by default search first 'ratan'
print(l1.index('ratan',2))		# search 'ratan' from index 2
print(l1.index('ratan',2,4))	# search 'ratan' from index 2 to 4

print('*see- to check if data is alpha ,numeric or alpha-numeric') 
print('*see- why alpha numberic doesnt work with space') 	
string1='HelloPython'		
print(string1.isalpha())

string2='HelloPython3.7'
print(string2.isalpha())

string3='2454546'
print(string3.isdigit())

string4='home123'
print(string4.isdigit())

string5='Ratan1980'
print(string5.isalnum())

string6='RatanIT'				#see - why its true?
print(string6.isalnum())

#check if string is upper case, lower case or it has space
print('***Upper case, lower case , space') 	
string1='hellopython'
print(string1.islower())

string2='HelloPython3.7'
print(string2.islower())

string3='HELLO FRIENDS'
print(string3.isupper())

string4='home123'
print(string4.isupper())

string5=' '					#see- why it works only for ' '
print(string5.isspace())
 
string6='RatanIT'				
print(string6.isspace())

print("*identity operator")
print('*to check if 2 variables are same or not without using =')
a=10
b=10
print(a is b)
print(a is not b)

print('*get remaing value after division')
print("*Modulus")
a=10
b=3
c=2
print(a%b)  			# a/b
print(a%c)  			# a/c

print('*after performing the division, get results in the lower integer close to result')
print("*floor division") 
a=10
b=3
print(a//b)

print('*to get few alphabets of string // to get few objects from list/set/tuple without for loop')
print("***slice")
print('- for string')

# -7 -6 -5 -4 -3 -2 -1  		#negative indexing
s= 'ratanIT'
# 0 1 2 3 4 5 6 				#positive indexing

print(s[2])
print(s[2:4])
print(s[1:4:2])
print(s[2:])
print(s[:4])
print(s[:])
# print(s[9])  			#Indexerror: string out of range

print(s[-2])
print(s[-5:-1])
print(s[:-1])
print(s[-5:])
print(s[:])
# print(s[-8])  			#Indexerror: string out of range

print("- for list")
list1=['a1','b2','c3','d4','5re']
print(list1[2])
print(list1[2:7]) 
print(list1[10:]) 
print(list1[:10])
print(list1[1:4:2])				#	starting point:end point:move right if its positive and move left if its negative

print('* VV IMP - negative indexing')
#https://www.quora.com/What-is-negative-index-in-Python
print(list1[-4:-2:-1])		#	starting point:end point:move right if its positive and move left if its negative
print("***MM IMP")
print(list1[-4:-2:1])		#	starting point:end point:move right if its positive and move left if its negative

print("- for tuple")
list1=('a1','b2','c3','d4','5re')
print(list1[2])
print(list1[2:7])
print(list1[10:])
print(list1[:10])
print(list1[1:4:2])

print("***MM IMP")
print(list1[-4:-2:-1])
print("***MM IMP")
print(list1[-4:-2:1])

#slice With dics -- not possible
#slice with set -- not possible

print('For List')
  # -5 -4 -3 -2 -1
L1=[10,20,30,40,50]
  # 0  1  2  3  4
print(L1[3])
print(L1[1:3])
print(L1[:3:2])
print(L1[1:])
print(L1[:2])
print(L1[:])
#print(L1[8])	Indexerror: list index out of range

print(L1[-2])
print(L1[-4:-2])
print(L1[:-2])
print(L1[-3:])
print(L1[:])

print('*to break string')
print("***split")

print('- for string')
a="india"
print(a.split('d'))

print('*to break string with separator')
print('+'.join(a.split('d')))			# this will split and place '+' in between

print("***concatenate")
print('for string')
b=" is a Country"
print(a+b)

print('*to concatenate Int and float')
print('- for Numbers(Int and Float)')
'''
we can concatenate int and float because they both are numbers
we can concatenate int and float to boolean because boolean has assigned values 0 and 1
'''
print(10+10.5)
print(10+True)
print(10+False)
print(20.5+True)

print('*concatenate string and number/float/bool')
'''
print(10+'ratan')				not able to concatenate string and number/float/bool
print(10.5+'tata')
'''

print('*concatenate list')
l1=[10,20,30]
l2=[40,50,60]
l3= l1+l2
print(l3)

# what is this?
print("***Replication")
print('*replication for string')
a='Hi'
print(a*2)

print('*replication for list')
l1=[10,20,30]
l2=l1*2
print(l2)

print('*to replace few alphabets with other alphabets in string')
print("***Replace")
print('- for string')
c=a.replace('a','a is country')
print(c)

print('*to make upper case')
print("***upper case")
print('for string')
print(a.upper())

print('*to make lower case')
print("***lower case")
print('for string')
print(a.lower())

print('*to make uppercase lower case and lower case to upper case')
print('***swapcase')
print('- For String')
print(a.swapcase())

print('***see - Capitalize')
print('for string')
#print(a.Capitalize())

print('*to give corresponding number to string')
print('***Enumarate')				
print(list(enumerate(a)))
print(tuple(enumerate(a)))

# how many times given alphabet present in string
print('***count')			# return count of character in given string
print('for string')
a='ratanratan'
print(a.count('r'))				#count 'r' in a
print(a.count('ratan'))			#count 'ratan' in a
print(a.count('a',1,7))			#count 'a' between 1 and 7 position
print(a.count('ratan',2,7))		#count 'ratan' between 2 and 7 position

# how many times given object present in list/set/tuple
print('for list')
l1=[10,20,30,10,10]
print(l1.count(10))

# to check if string start/end with given alphabets
print('start with and end with')
string1='Welcome to RatanIT'
print(string1.startswith('Welcome'))
print(string1.startswith('come',3,10))
print(string1.endswith('IT'))
print(string1.endswith('IT',10,18))
print(string1.endswith('IT',10,17))

print("***Conditional statement")
x=3
y=3
z=5

print("- if")
if x==3 and y==3:
	print("x and y are 3")

print("- if..else")
#case 1
if (x==z):
	print("x and z are same")
else:
	print("x and z are different")

#case 2
if True:
	print('true Condition')
else:
	print('false condition')

#case 3
if 0:
	print('true condition')
else:
	print('false condition')

#case 4							#this kind of if structure we can use in lambda
print('ratan'),print('ratan') if 10>20 else print('durga'),print('durga')

print("- if...elif...else")
if (y==z):
	print("y and z are same")
elif (x==z):
	print("x and z are different")
else:
	print("i dont know")	

print("**for Loop")
print("for range")
for k in range(8):
	print(k) 
for u in range(13,19):
 	print(u)
for no in range (102,130,5):
 	print(no)

print("for List") 
fruit=["banana","apple","orange"]
for aki in fruit:
 	print(aki) 

L1=[10,20,30,40]
for x in L1[1:3]:
	print(x)

L2=[[1,2,3],['ratan','anu','tata']]
for x,y,z in L2:
	print(x,y,z)

print("- for ...break") #(it will stop 'for loop')
car=[2,15,19,20]
for x in car:
 	print(x)
 	if (x==15):
   		break
 
print("- for...in...continue")# ( this will not run remaining steps but will continue for loop)
for y in fruit:
	if (y=="apple"):
   	   continue
	print(y)
 
print("- for.....else**")
for z in range (5,10):
	print(z)
else:
 	print("Finally finished!")

print("**while loop**")
n = 25
while n > 20:
    print (n)
    n = n-1

print("**While...break**") #it will stop the while execution
i = 200
while i < 215:
 print(i)
 if i == 206:
   break
 i += 2

#example 2
a=1
while a<10:
	print(a)
	if a==5:
		break
	a+= 1 

print("**while...continue**") 
#it will start exceution from begining like here when i=3 its not printing i value
a=1
while a<5:
	a+= 1
	if a==3:
		continue
	print(a)

print('*to access objects from Dictionary')
d1={111:'ratan',222:'anu',333:'durga',444:'ratanIT'}

print(d1.keys())
print(d1.values())
print(d1.items())

for x in d1:
	print(x)

for x in d1:
	print(x,d1[x])

# to access all keys from dict
for i in d1.keys():
	print(i)

# to access all values from dict
for i in d1.values():
	print(i)

#to access all items from dict
for i in d1.items():
	print(i)

for x,y in d1.items():
	print(x,'-',y)

print(d1.get(111))

print('*to access objects from Dictionary without for loop and without keys,items,values')
#method 1
r=d1[444]
print(r)

#method 2
a,b,c=d1
print(a.b.c)

''' ratan '''
print("***how to get all keywords")
import keyword
print(keyword.kwlist)

''' for 2.x we dont need parenthesis to print while 3.x requires parenthesis
    because we can see in 2.x print is keyword while in 3.x print is not keyword'''

print('***variable')
evalue,esalary,expect=10,20,30  
evalue=esalary=expect=10

print('***re assigning')
a=10
print(a)

a=100
print(a)

print('***delete')

v=10
print(v)
del v

print('***INPUT')

'''
print('* take input as string and then do concatenate')
a=input('A=')				#Input takes all value as string
b=input('B=')				#thats why this example will give string as result (eg:1020)
print(a+b)

eid= int(input('eid:'))			# convert input value as int
ename=input('ename:')
esal=float(input('esal:'))		# convert input value as float

print('Example-1')
num1= input('Enter first num:')		
num2= input('Enter second num:')
total=num1+num2
print('total:',total)

# below example will give int as result

print('* take input as int and then do concatenate')
print('example-2')
num1= int(input('Enter first num:'))
num2= int(input('Enter second num:'))
total=num1+num2
print('total:',total)
'''

print('***Range')						# logic same as index
'''
Rule: start from first value upto second value and if third value is 
	  positive move left to right and if third value is negative then
	  move right to left 
'''
for x in range(5):
	print(x)

for x in range(6,10):
	print(x)

for x in range(14,20,3):
	print(x)

for x in range(22,14,-3):
	print(x)

for x in range(-10,-1,4):
	print(x)

for x in range(-15,-27,-5):
	print(x)

print("***for vs while")
# for when we have starting value , ending value by incremental / decremental
# while is to check if condition is true or not

print('*** types of error')
'''
Type Error: concat not possible
valueerror : conversion 
Name error: name is not defined
unbounded local error: related to local and global variable
'''

print('***Number systems')
'''
binary : base 2
octal  : base 8
decimal : base 10
Hexa decimal : base 16

binary system: allows 0 and 1
octal form: allows 0 to 7
decimal : allows 0 to 9
hexa decimal: allows 0 to 9 and a to f
'''

print('* to get ASCI values')
print('see-ASCI value')
c=5
#print(ord(c))

c=f
#print(ord(c))

print('*to get binary value')
print('binary values')
c=112
print(bin(c))

print('*to get octal value')
print('octal values')
c=20
print(oct(c))

print('*to get hexa decimal value')
print('hexa deciaml values')
c=20
print(hex(c))

print('***Python identifiers - nomenclature of class,function rules')
'''
Rule 1 :a-z , A-Z , _    -should not start with numberic , should not allow special characters
Class Myclass123 - valid
Class 123Myclass - Invalid
Class Myclass_123 - valid
Class Myclass*123 - invalid

Rule 2 : case sensitive

Rule 3 : No lenght limit

Rule 4 : Duplicates not allowed				# duplicates allowed only in variable

Rule 5 : kewords not allowed
self=100 									#not allowed

Rule 6 : Possible to take pre defined class names as identifiers but not recommended
'''

print('see video10:30.00 - difference between global and nonlocal')

print('*how to know length ')
print('for string')
s='    ratan IT   '
print(len(s))

print('for list')
l1=[10,'ratan',10.5]
print(len(l1))

print('*how to remove space or characters')
print(s.strip()) 		#to remove space at begining and at the end
print(len(s.strip()))

s1='@@@ratan IT####'					#characters can be remove at begining or end.. not from middle
print(len(s1))
print(s1.lstrip('@'))		# to remove @ at begining
print(s1.rstrip('#'))		# to remove # at the end
print(s1.rstrip('#').lstrip('@'))
print(s1.lstrip('IT'))		# i can not remove IT here because its in middle of string

print('***id,=,!=,is in')
'''
id() : print memory location
is, is not : memory comparison : return boolean    		#it compares data as well as memory location
== , !=  : data comparison : return boolean
in, not in : check data available or not : return boolean
'''

print('For string')
name1='ratan'
name2='anu'
name3='ratan'

print(id(name1))
print(id(name2))
print(id(name3))

print('**')
print(name1 is name2)				
print(name1 is name3)				#same string value-->save at same memory location thats why here its true
print(name1 is not name2)
print(name1 is not name3)

print('**')
print(name1==name2)
print(name1==name3)
print(name1!= name2)
print(name1!= name3)

print('**')
print('ra' in name1)
print('durga' in name1)
print('ra' not in name1)
print('durga' not in name1)

print('For List')
L1=[10,20,30]
L2=[40,50,60]
L3=L1
L4=[40,50,60]

print(id(L1))
print(id(L2))
print(id(L3))
print(id(L4))

print('**')
print(L1 is L2)
print(L1 is L3)
print(L1 is not L2)
print(L1 is not L3)

print('**')
print(L1==L2)
print(L1==L3)
print(L2==L4)
print(L1!=L2)
print(L1!=L3)
print(L2!=L4)

print('**')
print(10 in L1)
print(100 in L1)
print(10 not in L1)
print(100 not in L1)

print('for Dics')
d1={111:'ratan',222:'anu'}
d2={333:'ratan',444:'anu'}
d3=d1
d4={111:'ratan',222:'anu'}

print(id(d1))
print(id(d2))
print(id(d3))
print(id(d4))

print(d1 is d2)
print(d1 is d3)
print(d1 is not d2)
print(d1 is not d3)

print(d1==d2)		#data caomparison: compares both key,value
print(d1==d4)
print(d1!=d2)
print(d1!=d4)

print(111 in d1)	#check only keys avaiable or not
print(11 in d1)
print(111 not in d1)
print(11 not in d1)

print('***Unpacking') 
print('-for list')		#List --> variables #it will break list and assigns values to variables
L1=[10,10.4,'ratan']
a,b,c=L1
print(a,b,c)
print(type(a),type(b),type(c))

#IMP
L2=[10,20,30]
#a,b=L2		#this will give an error, need exact number of variables for unpacking 

print('-for dics')
d1={1:'aaa',2:'bbb'}
a,b=d1
print(a,b)				# dics will unpack only keys

d2={1:'aaa'}
c=d2
print(c)

print('***packing')
print('convert list/set/tuple into dics')
l1=[1,2,3,4]							 
l2=['ratan','durga','anu','ratanIT']
x=zip(l1,l2)			
d=dict(x)
print(d)

l1=(1,2,3,4)							 
l2=('ratan','durga','anu','ratanIT')
x=zip(l1,l2)			
d=dict(x)
print(d)

l1={1,2,3,4}							 
l2={'ratan','durga','anu','ratanIT'}
x=zip(l1,l2)			
d=dict(x)
print(d)

print('*** sort/sorted')

''' IMP
just to arrange by asc or desc ---> sort
to arrange with any other logic ---> sorted
'''

print('For List')
#arrange number in asc order
a=[1,4,5,3,2]
a.sort()		
print(a)

#arrange alphabet in asc order
b=['a','e','b','d','c']
b.sort() 	
print(b)

#arrange number in desc order
e=[1,4,5,3,2]
e.sort(reverse=True) 		
print(e)

#arrange alphabet in desc order
f=['a','e','b','d','c']
f.sort(reverse=True)		
print(f)

#arrange given list by length
i=['bcde','cd','def','a']
j=sorted(i,key=len)
print(j)

#arraneg by function
def func(x): 
    return x % 7
L = [15, 3, 11, 7] 
m = sorted(L, key = func)
print(m)

l3=[10,20.85,'ratan']
#l3.sort() 					#heterogenous sorting not supported

print('-for dics')
d1={1:'ratan',2:'durga',3:'anu',4:'surya'}
print(sorted(d1.keys()))
print(sorted(d1.values()))
print(sorted(d1.items()))

print('***reverse')
print('for list')
l1=[10,20,30]
l1.reverse()
print(l1)

print('***List info')
'''
1. represent group of objects :homogenus(same data type of objects) & heterogrnous( different data types of object)
example: homogenous L1=[10,20,30]  heterogenous L2=[10,'ratan',10.05]
2. indexing : forward and backward
3. duplicate objects allowed
4. mutabale: modifications are allowed
5. insertation order : e1,e2,e3 --> e1 e2 e3
'''
print('***For Nested List/sub list/Multi dimension List')
'''
to access data In dataframe use loc, iloc
to access data in multi dimension list, tuple,set use like below
'''
#      0	   1
L1=[[10,20],['ratan','tata']]
#    0  1    0  1 
print(type(L1[0]))
print(L1[0])
print(L1[1])

print(type(L1[1][1]))
print(L1[0][1])
print(L1[1][1])

print('***unpacking')
L2=[[1,2,'ratan'],[3,'tata']]
a,b=L2
print(type(a))
print(b)
print(b[1])

print('copy')
l1=[10,20,30]
l2=l1.copy()
print(l2)

print('***modification')
print('- For list')
print('extend') 	#this will add whole list into another list
l1=[10,20,30]
l2=[40,50,60]
l1.extend(l2)
print(l1)

print('append') 	#to add at end
l1=[10,20,30]
l1.append(40)
print(l1)

print('Insert')		#to add by specific location
l1=['ratan','anu']
l1.insert(1,'aaa')		#this will add at index 1
print(l1)
l1.insert(6,'bbb')		#this will add at index6 but we dont have index5 so it will add at the end
print(l1)

print('remove') 	#to delete by object value
l1=[10,20,30]
l1.remove(20)
print(l1)

print('pop')		#to delete by object index
l1=['ratan','durga',10,10.5]
l1.pop()			# by default it will remove last one
print(l1)
l1.pop(1)			# this will remobe index 1 object
print(l1)
#l1.pop(10)			# pop index out of range

print('del')		# to delete more than one objects same time
l1=[10,20,30,40,50,60,70,80,90,100,110,120,130,140,150]
del l1[2]
print(l1)
del l1[1:4]
print(l1)
del l1[1:4:2]
print(l1)
del l1[:2]
print(l1)
del l1[:]
print(l1)

print('clear')			#to delete all objects 
l1=[10,20,30]
l1.clear()
print(l1)

print('-for Dict')
print('to add object at the end in dics')
d3={}
d3[111]='ratan'
d3[222]='anu'
d3[333]='ratan'
print(d3)

print('to add one dict into another dict')
#method 1
d1={1:'aaa',2:'bbb'}
d2={3:'ccc',4:'ddd'}
d1.update(d2)
print(d1)

#method 2
d1={1:'aaa',2:'bbb'}
d2={3:'ccc',4:'ddd'}
x={**d1,**d2}
print(x)

print('to remove last object/particular object from dics')
d1={1:'aaa',2:'bbb',3:'ccc'}
d1.popitem()		# this will remove last item fron dics
print(d1)
d1.pop(2)		#this will remove key 2 from dics
print(d1)

print('to remove all objects from dics')
d1={1:'aaa',2:'bbb',3:'ccc'}
d1.clear()
print(d1)

print('***Max Min')		#give maximum and minimum values
print('for string')

l1=[10,20,30]
print(max(l1))
print(min(l1))

l2=['ratan','anu','durga']		#decide by ASCI value
print(max(l2))		
print(min(l2))

l3=[10,'ratan']				#TypeError: '>' not supported between instances of 'str' and 'int'
#print(max(l3))				# can not compare heterogenous objects	
#print(min(l3))				# can not compare heterogenous objects

print('-for dics')
d1={1:'ratan',2:'durga',3:'anu',4:'surya'}
print(max(d1))
print(min(d1))

d2={'ratan':1,'durga':2,'anu':3,'surya':4}
print(max(d2))
print(min(d2))

#doest work with heterogenous dics
d3={1:'ratan',2:'durga','anu':3,'surya':4}	#TypeError: '>' not supported between instances of 'str' and 'int'
#print(max(d3))
#print(min(d3))

print('***Dics***') 
'''
key:value    key=obj  	value=obj   :both together called item
{key:value,key:value}
keys:unique		values:duplicated
mutable: it allows modification
'''
print('Dict keys must be immutable(tuple,number,string) data type')
print('Dict values can be any data type')

#d1={[1,2]:'ratan',222:'anu',333:'durga'}		#list not allowed as dict key
print(d1)
#TypeError: unhashable type: 'list'

d1={111:['ratan','tata'],222:'anu',333:'durga'}		#list allowed as dict values
print(d1)

print('override')
d3={}
d3[111]='ratan'
d3[222]='anu'
d3[333]='ratan'
d3[111]="repeat"		# if we try to enter same key again it will override that key and value
print(d3)

print('None')			# None allowed in keys and values both
d2={None:None}
print(d2)
