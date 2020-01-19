print("****print")
print("****print")
a=123
print (a)

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

print('function - args')
#case 1
def multiple(*args):
	print(args)
multiple(1,2,3,4)

def star(*a):
	for x in a:
		print(x)

star(10,20,30)

#case 2
def star(car,*a):
	print(car)
	for x in a:
		print(x)
star("honda",10,20,30)

def star(*b,car):
	print(car)
	for x in b:
		print(x)
star(49,81,car='accord') #in this case, use keyword arguments 

#case 3
def star(name='ratan',*b):
	print(name)
	for x in b:
		print(x)
star(35,94,100)  # here name=35,and *a=94,100

#case 4
def star(name1,name='ratan',*b):
	print(name1)
	for x in b:
		print(x)
star(35,94,100,90)  #here name1=35,name=94 and *a=100,90

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

print("***to call function")
print("IMP: '()' this symbol call function")
def a1():
	print("a1")
a1() # this will call function a1

print("***IMP")
def akhil():
	print("akhil")
a3=akhil() # this will call akhil function
   
def a(x):
	print(x+10)
b=a
b(2) # this will call function a

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

print("***Return (IMP)")
def function_that_prints():
    print("I printed")

def function_that_returns():
    return "I returned"
    print("after return")

print("***The return statement terminates the execution of a function")
print("** function calling  will give only print values,not return values ")
f1 = function_that_prints() #this will call function_that_prints
f2 = function_that_returns() # this will call function_that_returns
print("***to access return values assign variable to function")
print("calling and print the variable because retuen assigns value") 
print("to function so we need to print calling function ")
print(f1) 
# or
print(function_that_prints()) 

print(f2)
# or
print(function_that_returns())
 
print("return example 2")
def no_return(x,y):
    c = x + y
    return c
print(no_return(4,5))

# Multiple return statement
def disp():
	print('good morning')
	return 10
	return 20			    #ignored
	print('good evening')	#ignored

disp()

# default return value is none


print("***variables")
a="bol bhai"
print(a)

print("***local & global variable")
#case 1       # all function can use global variable value

name='ratan'  # global variable
def disp1():
	print('good morning',name)

def disp2(value1,value2):
	print(value1+value2)        # local variable
	print('good afternoon',name)
disp1()
disp2(3,10)

#case 2 
# when local and global variable has same name then priority goes to local varibale
g,h=10,20
def sarvado(g,h):
	print(g+h)
sarvado(2,3)

#case 3 
# to use local variable as global variable
g,h=10,20
def sarvado(g,h):
	print(globals()['g']+h)  # here we use g variable as global variable
sarvado(2,3)

#case 4
# to declare global variable from inside function
def disp3():
	global s 
	s='ratan'
	print(s)
disp3()
print(s)


#case 5
b=100
print(b)
def scope():
	b=200
	print(b)
scope()
print(b)

#case 6 ( VV IMP)
# once we use global variable inside function we can not declare same variable as local variable
# below code will give error
'''
name='ratan'
def tution():
	print(name)  # used name as global variable
	name='durga'  # after using name as global variable we can not declare same vaiable as local
	print(name)
tution()
'''

print('Nonlocal keyword')
#case 7 - VV IMP
# to chnage parent function's variable value from child function use nonlocal keyword
# in below example we are chaning name1 variable value inside child function using nonlocal keyword
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
	inner()
	print(name1)
outer()
print(name)

# without Nonlocal
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

print("***arithmetic Operator")
x=10
y=20
print(x+y)
print(x*y)
print(y-x)
print(y/x)

print("***relation operator")
print('for number')
f=30
g=23
print(f<g)
print(f>g)
print(f==g)
print(f<=g)
print(f>=g)
print(f!=g)

print('for string') 			# compare based on ASCI value
print('ratan' > 'anu')
print('ratan' < 'anu')
print('ratan' >= 'anu')
print('ratan' <= 'anu')
print('ratan' == 'anu')
print('ratan' != 'anu')

print("**assignment operator**")

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

x/=y
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

print("**Logical operator**")
x=2
y=3
print(x>1 and y>2)
print(x==1 or y==3)
print(x==1 and y==3)

print("Membership operator")
x="california"
print('z' in x)
print('z' not in x)

x=['india','ab','ssss']
print ("ab" in x)

print("identity operator")
a=10
b=10
print(a is b)
print(a is not b)

print("Modulus")
a=10
b=3
c=2
print(a%b)  # a/b
print(a%c)  # a/c

print("*** floor division") 
print("after performing the division, give results in the lower integer to the value")
a=10
b=3
print(a//b)

print("***String operator")
print("***slice of string")
a="india"
print (a[1])

print("***slice of list")
list1=['a1','b2','c3','d4','5re']
print(list1[2])
print(list1[2:7]) 
print(list1[10:]) 
print(list1[:10])
print(list1[1:4:2])

print("***MM IMP")
#https://www.quora.com/What-is-negative-index-in-Python
print(list1[-4:-2:-1])
print("***MM IMP")
print(list1[-4:-2:1])

print("***slice With tuple")
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

print("***split")
print("***split with string")
a="india"
print(a.split('d'))

print("***concatenate")
b=" is a Country"
print(a+b)

print("***Repeat")
print(a*2)

print("***Replace")
c=a.replace('a','a is country')
print(c)

print("***upper case")
print(a.upper())

print("***lower case")
print(a.lower())

#change data type

print("***Conditional statement")
x=3
y=3
z=5

print("***if")
if x==3 and y==3:
	print("x and y are 3")

print("***if..else")
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

#case 4
print('ratan'),print('ratan') if 10>20 else print('durga'),print('durga')

print("***if...elif...else")
if (y==z):
	print("y and z are same")
elif (x==z):
	print("x and z are different")
else:
	print("i dont know")	

print("**for Loop")
print("for loop with range")
for k in range(8):
	print(k) 
for u in range(13,19):
 	print(u)
for no in range (102,130,5):
 	print(no)

print("**for loop with List") 
fruit=["banana","apple","orange"]
for aki in fruit:
 	print(aki) 
 
print("**for ...break") #(it will stop 'for loop')
car=[2,15,19,20]
for x in car:
 	print(x)
 	if (x==15):
   		break
 
print("**for...in...continue")# ( this will not run remaining steps but will continue for loop)
for y in fruit:
	if (y=="apple"):
   	   continue
	print(y)
 
print("**for.....else**")
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

#Arrays
print("*** to convert int to string")
x=str(y)


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

print("**Tuple to Dics ")
Tuple1=('a','b','c','d')
Dict2={i:i*2 for i in Tuple1}
print(Dict2)

print("***to access Dictionary data (IMP)")
Dict3={1: 2, 2: 4, 3: 6, 4: 8, 'a': 10}
r=Dict3['a']
print(r)

r=Dict3.keys()
print(r)
r=Dict3.values()
print(r)
r=Dict3.items()
print(r)

for i in Dict3.keys():
	print(i)

for i in Dict3.values():
	print(i)

for i in Dict3.items():
	print(i)

for x,y in Dict3.items():
	print(x,'-',y)

print("exponent ")
x=10
n=2
print(x**2)
 
''' ratan '''
print('***PRINT')
eid,ename,esal=111,'ratan',100.45
print(eid)
print(ename)
print(esal)

print('Emp id=',eid)
print('Emp name=',ename)
print('Emp sal=',esal)

print('Emp id=',eid,'Emp name=',ename,'Emp sal=',esal)

print(eid,end='')  # this will print next line in same line
print(' ',ename)

print(10,20,30,sep='*')

print("***List of keyword")
import keyword
print(keyword.kwlist)

''' for 2.x we dont need parenthesis to print while 3.x requires parenthesis
    because we can see in 2.x print is keyword while in 3.x print is not keyword'''

print("***General Datatypes")
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

print(type(evalue))
print(type(ename))
print(type(esalary))
print(type(ebool))

print('***variable')
evalue,esalary,expect=10,20,30
evalue=esalary=expect=10

print('***concatenation')
'''
we can concatenate int and float because they both are numbers
we can concatenate int and float to boolean because boolean has assigned values 0 and 1
'''
print(10+10.5)
print(10+True)
print(10+False)
print(20.5+True)

print('***not able to concatenate string and number/float/bool')
'''
print(10+'ratan')
print(10.5+'tata')
'''

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
Input takes all value as string
thats why below example will give string as result (eg:1020)

print('Example-1')
num1= input('Enter first num: ')
num2= input('Enter second num: ')
total=num1+num2
print('total:',total)


below example will give int as result

print('example-2')
num1= int(input('Enter first num: '))
num2= int(input('Enter second num: '))
total=num1+num2
print('total:',total)
'''


print('Range')
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

print('ASCI value')
c=5
print(ord(c))

c=f
print(ord(c))

print('binary values')
c=112
print(bin(c))

print('octal values')
c=20
print(oct(c))

print('hexa deciaml values')
c=20
print(hex(c))


print('***Python identifiers - nomenclature of class,function rules')

'''
Rule 1 :a-z , A-Z , _    -should not start with numberic , should not alloe special characters

Class Myclass123 - valid
Class 123Myclass - Invalid
Class Myclass_123 - valid
Class Myclass*123 - invalid

Rule 2 : case sensitive

Rule 3 : No lenght limit

Rule 4 : Duplicates not allowed

Rule 5 : kewords not allowed
self=100 # not alloed

Rule 6 : Possible to take pre defined class names as identifiers but not recommended

'''


print('see video10:30..00 - difference between global and nonlocal')


print('***string***')

print('Indexing')

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

print('legth , remove space or characters')
s='    ratan IT   '
print(len(s))
print(s.strip()) 		#to remove space at begining and at the end
print(len(s.strip()))

s1='@@@ratan IT####'
print(len(s1))
print(s1.lstrip('@'))		# to remove @ at begining
print(s1.rstrip('#'))		# to remove # at the end
print(s1.rstrip('#').lstrip('@'))


print('id,=,!= ,is in')
'''
id() : print memory location
is, is not : memory comparison : return boolean    		#it compares data as well as memory location
== , !=  : data comparison : return boolean
in, not in : check data available or not : return boolean
'''
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


eid= int(input('eid: '))
ename=input('ename: ')
esal=float(input('esal: '))
print('emp id: ',eid)
print('emp name: ',ename)
print('emp salary: ',esal)


print('formatting data')
'''
int 	float		string    
%d 		%g   %f 	  %s

{}

'''
# for % , if %d is first its value must be first...so its sequence is important
print('emp id =%d emp name =%s emp sal=%g' %(eid,ename,esal))

# difference between %g and %f
# %f prints upto 12 digits while %g prints data upto 6 digits only
a=123.456879
print('value of a=%g'%(a)) 

a=123456.87958418641684888
print('value of a=%f'%(a)) 

#while {} is very flexible 
print('emp id ={} emp name ={} emp sal={}'.format(eid,ename,esal))
print('emp id ={2} emp name ={0} emp sal={1}'.format(eid,ename,esal))



















