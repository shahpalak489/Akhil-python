print("***how to get all keywords")
import keyword
print(keyword.kwlist)

''' for 2.x we dont need parenthesis to print while 3.x requires parenthesis
    because we can see in 2.x print is keyword while in 3.x print is not keyword'''

print("***print")
print('*print string,int and float')
eid,ename,esal=111,'ratan',100.45
print(eid)
print(ename)
print(esal)

print('* for string - to print in next line')
print("Hello\nWorld!")

print('*for variable - to print in next line')
a='hi'
b=10
print(a,b,sep='\n')

print('*print 2 lines together')
print(eid,end='') 				 # this will print next line, in same line
print(' ',ename)

print('*print hard coded value and variable together')
print('Emp id=',eid)
print('Emp name=',ename)
print('Emp sal=',esal)

print('Emp id=',eid,'Emp name=',ename,'Emp sal=',esal)

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

print('*what is output if we print duplicate keys,duplicate values')
d2={111:'ratan',111:'surya',222:'surya'}	  #duplicate keys will be override  	#duplicate values will be ok
print(d2)

print('***INPUT')

'''
print('* take input as string and then do concatenate')
a=input('A=')				#IMP:  Input takes all value as string
b=input('B=')				#thats why this example will give string as result (eg:1020)
print(a+b)

print('* convert input value to int')
eid= int(input('eid:'))			
ename=input('ename:')

print('* convert input value to float')
esal=float(input('esal:'))		

print('Example-1')
num1= input('Enter first num:')		
num2= input('Enter second num:')
total=num1+num2
print('total:',total)

# below example will give int as result

print('* take input as int and then do sum')
print('example-2')
num1= int(input('Enter first num:'))
num2= int(input('Enter second num:'))
total=num1+num2
print('total:',total)
'''

print("***arithmetic Operator")
print('+,-,*,/')
x=10
y=20
print(x+y)
print(x*y)
print(y-x)
print(y/x)

print('* absolute')
print(abs(-72.50))

print('* sum,averge,mean for list')
a=[12,52,52]

#sum
print(sum(a))

#average
print(sum(a)/len(a))

#mean
import statistics
b=statistics.mean(a)
print(b)

print('*** maximum and minimum values in list for integer')
l1=[10,20,30]
print(max(l1))
print(min(l1))

print('* maximum and minimum values in list for string')
l2=['ratan','anu','durga']		#decide by ASCI value
print(max(l2))		
print(min(l2))

l3=[10,'ratan']				#TypeError: '>' not supported between instances of 'str' and 'int'
#print(max(l3))				# can not compare heterogenous objects	
#print(min(l3))				# can not compare heterogenous objects

print('* get maximum and minimum values in dics')
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

print('* get maximum and minimum values between 2 numbers')
print(max(2,10))

print("* exponent")
#method 1
x=10
n=2
print(x**n)				# equal to 10 rest to 2

#method 2
x=10
n=2
print(pow(x,n))		# equal to 10 rest to 2

print('***get remaing value after division')				#Modulus
a=10
b=3
c=2
print(a%b)  			# a/b
print(a%c)  			# a/c

print('***after performing the division, get results in the lower integer close to result')
											#floor division 
a=10
b=3
print(a//b)

print("***relation operator")
# <, >, <= ,>= !=
print('- for number')
f=30
g=23
print(f<g)
print(f>g)
print(f==g)
print(f<=g)
print(f>=g)
print(f!=g)

print('- for string') 		# compare based on ASCI value
print('ratan' > 'anu')
print('ratan' < 'anu')
print('ratan' >= 'anu')
print('ratan' <= 'anu')
print('ratan' == 'anu')
print('ratan' != 'anu')

print("***assignment operator")
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

print("***Datatypes")
'''
Number : int & float : 10,20 & 5.25, 10.29
string : str : 'ratan' "ratan"
Boolean : bool : True  False 
				   1    0
'''

evalue = 12
ename = 'ratan'
esalary = 100.92
ebool=True

print('*how to know its Datatypes (number, string ,boolean, List, tuple or Dics)')
print(type(evalue))
print(type(ename))
print(type(esalary))
print(type(ebool))

L1=[10,20,30,40]
print(L1)
print(type(L1))

d1={111:'ratan',222:'durga'}
print(type(d1))

print('***variable')
evalue,esalary,expect=10,20,30  
evalue=esalary=expect=10

print('*re assigning variable value')
a=10
print(a)

a=100
print(a)

print('*delete variable')
v=10
print(v)
del v

print('***formate specifier')		#mainly use to print varibles in statement
'''
Method:1 (recommended)
{}   

Method:2
int -->%d ,	%g	  			#see -  %g is for int or float?
float-->%f	
string-->%s 
'''

eid,ename,esal=111,'ratan',100.45

#Method:1 (recommended)
print('*print int,string,float with {} format specifier')		
#{} is very flexible 
print('emp id ={} emp name ={} emp sal={}'.format(eid,ename,esal))
print('emp id ={2} emp name ={0} emp sal={1}'.format(eid,ename,esal))

#Method:2
print('*print int,string,float with % format specifier')
# for % , if %d is first its value must be first...so its sequence is important
print('emp id =%d emp name =%s emp sal=%g' %(eid,ename,esal))	#real time example

# difference between %g and %f
# %f prints upto 12 digits while %g prints data upto 6 digits only
a=123.456879
print('value of a=%g'%(a)) 

a=123456.87958418641684888
print('value of a=%f'%(a)) 

d1={1:'ratan',3:'anu',4:'surya',2:'durga'}
for key in sorted(d1.keys()):
	print("key=%d values=%s"%(key,d1[key]))

print("***function")
print('*give function syntax')
def aki():
	print("this is not right")
aki()

print('*function with argument')
def square(x):
	print(x*x)
square(2)	
 
def addition (x,y):
	print(x+y)
addition(3,5)

print('*function with default argument')
print('variable value priority: variable value while calling > variable default value')
def default(x,y=25,z=5):  
	print(x+y+z)

default(10)   #here y=25,z=5 default value and x=10 because we gave x value while calling  
default(10,20) #here z=5 because while calling we gave x=10,y=20
default(y=10,x=2) #if we change sequence of variable then we need to specify x=2 

print('*VIMP:first give non-default value then default value')
#default(20,y=40,30) 			#Invalid : once we give y=40 then rest of all argument must be 
								#z=something we can not put 30 after y=40

default(50,60,z=10)  			# valid

print("***to call function")
#IMP: '()' this symbol call function
print('VVV IMP: always call funcation after its defined')

#method 1 (all methods are important)
def a1():
	print("a1")
a1() 							# this will call function a1

#method 2
print("***IMP")
def akhil():
	print("akhil")
a3=akhil() 						# this will call akhil function

#method 3   
def a(x):
	print(x+10)
b=a
b(2) 					 		# this will call function a

print("*to call 1 function inside another function")
def outside():
	def inside():
		print("i am inside") #step2
	print("i am outside") #step1
	inside() # this will call function inside
outside() # this will call function outside

print("*to call 2 different functions same time")
def g():
    print("Hi, it's me 'g'")
    print("Thanks for calling me")
def f(func):
    print("Hi, it's me 'f'")
    print("I will call 'func' now")
    func() 						#func=g  #step2: this will call function g
f(g) 							#step 1: this will call function f

print("*see - why it will Not call?")
def inner1(): 
    print("Hello, this is before function execution") 
    func() 						# this will not call func unction
    print("This is after function execution")
    return inner1

print('*function with n number of arguments')
def multi(*a):					# for n number of arguments use *
	print(a)
multi(1,2,3,4)

def star(*ar):
	for x in ar:
		print(x)
star(10,20,30)

print('*function with n arguments at begining,at end')
def star(car,*arg):
	print(car)
	for x in arg:
		print(x)
star("honda",10,20,30)

def star(*b,car):
	print(car)
	for x in b:
		print(x)
star(49,81,car='accord') 			#in this case, use keyword arguments 

def star(name='ratan',*b):
	print(name)
	for x in b:
		print(x)
star(35,94,100)  					#here name=35,and *b=94,100

def star(name1,name='ratan',*b):
	print(name1)
	for x in b:
		print(x)
star(35,94,100,90)  				#here name1=35,name=94 and *b=100,90

def star(name1,*b,name='ratan'):
	print(name1)
	for x in b:
		print(x)
star(35,94,100,90)  				#here name1=35 and *b=94,100,90

def star(name1,*b,name='ratan'):
	print(name1)
	for x in b:
		print(x)
	print(name)
star(35,94,100,90,name='tata')  			#here name1=35 and *b=94,100,90 and name='tata'

print("***Return (IMP)")
def function_that_prints():
    print("I printed")

def function_that_returns():
    return "I returned"
    print("after return")

print("*MMIMP - The return statement terminates the execution of a function")
print("IMP - function calling  will give only print values,not return values ")
f1 = function_that_prints() 				#this will call function_that_prints
f2 = function_that_returns() 				# this will call function_that_returns

print("*IMP - to access return values assign function calling to variable")
print("and print the variable because return assigns value to function") 
print("so we need to print calling function ")

print(f1) 
print('**')
print(function_that_prints())			#see its answer 

print('**')
print(f2)
print('**')
print(function_that_returns())			#see its answer
 
print("example 2")
def no_return(x,y):
    c = x + y
    return c
h1=no_return(4,5)
print(h1)

print('* Multiple return statement')
def disp():
	print('good morning')
	return 10
	return 20			    			#ignored
	print('good evening')		    	#ignored
disp()

print('*default return value is none')

print("***local & global variable")
#case 1
print('*all function can access global variable value and local var just for that function')
name='ratan'  					# global variable
def disp1():
	print('good morning',name)
disp1()

def disp2(value1,value2):
	print(value1+value2)        # local variable
	print('good afternoon',name)
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
print('* how local variables get global variable value when both variables are same name?')
#example 1
g,h=10,20
def sarvado(g,h):
	print(globals()['g']+h)  			#here we get g=10 value as global variable
sarvado(2,3)

#example 2
a=15
def m1():
	a=20
	print(globals()['a'])
m1()

#case 4
print('*to declare global variable, inside function')
def disp3():
	global s 
	s='ratan'
	print(s)
disp3()						#IMP: function must be executed to declare global variable
print(s)

#Case 5 
print('* to update Global variable value, inside function')
name='ratan'
def outer():
	name1='durga'
	def inner():
		name1='sunny'			#IMP: this will not update global variable value
		global name
		name='ratan IT'			#IMP: this will update global variable value
	print(name1) 
	inner()
	print(name1)
outer()
print(name)

#case 6 (VV IMP)
print('*once we use global variable,inside function we can not declare same variable as local variable')
# below code will give error
'''
name='ratan'
def tution():
	print(name)  	# used 'name' as global variable
	name='durga'  	# after using name as global variable we can not declare same vaiable as local
	print(name)		# UnboundLocalError: local variable 'a' referenced before assignment
tution()
'''

#case 7
print('*once we declare variable as local variable we canot declare/update same variable as global variable')

# below code will give error
'''
AKI=123
def aki9():
	AKI=789				#used AKI as local variable
	global AKI          # can not declare/ update same variable as global variable within function
	AKI=456

aki9()
print(AKI)
'''

# case 8 - VV IMP
print('*to change parent function variable value, from child function' )
# example 1
def m1():
	a=20
	def m2():
		nonlocal a
		a=30
	m2()				#this function calling is must to update value of a
	print(a)
m1()
# example 2
# in below example we are changing name1 variable value inside child function, using nonlocal keyword
# because of this name1 value changes foreever
name='ratan'
def outer():
	name1='durga'
	def inner():
		nonlocal name1  	# this will update parent name1 variable
		name1='sunny'
		global name
		name='ratan IT'		# this will update global variable value
	print(name1) 
	inner()					#this function calling is must to update value of name1
	print(name1)
outer()
print(name)

print('*see video10:30.00 - difference between global and nonlocal')

print('***to get few alphabets of string // to get few objects from list/set/tuple without for loop')
print('*** MMIMP: slice')
print('- for string')

# -7 -6 -5 -4 -3 -2 -1  		#negative indexing
s= 'ratanIT'
# 0 1 2 3 4 5 6 				#positive indexing

#starting point:end point:if starting point to end point is moving left this value should be negative otherwise it will return []  
#starting point:end point:if starting point to end point is moving right this value should be positive otherwise it will return []  

print('#use slice to get below commented answers with positive indexing')
#t
#ta
#aa
#rata
#tanIT
#ratanIT

print(s[2])
print(s[2:4])
print(s[1:4:2])
print(s[:4])			#MMIMP: start point not given so it will start from all the way left
print(s[2:])			#MMIMP: end point not given so it will end all the way right
print(s[:])
# print(s[9])  			#Indexerror: string out of range

s= 'ratanIT'
print('#use slice to get below commented answers with negative indexing')
# I
# tanI
# ratanI
# tanIT
# ratanIT

print(s[-2])
print(s[-5:-1])
print(s[:-1])
print(s[-5:])
print(s[:])
# print(s[-8])  			#Indexerror: string out of range

print('- For List')
  # -5 -4 -3 -2 -1
L1=[10,20,30,40,50]
  # 0  1  2  3  4
print('#use slice to get below commented answers with positive indexing')
# 40
# [20, 30]
# [10, 30]
# [20, 30, 40, 50]
# [10, 20]
# [10, 20, 30, 40, 50]

print(L1[3])
print(L1[1:3])
print(L1[:3:2])
print(L1[1:])
print(L1[:2])
print(L1[:])
#print(L1[8])	Indexerror: list index out of range

print('#use slice to get below commented answers with negative indexing')
# 40
# [20, 30]
# [10, 20, 30]
# [30, 40, 50]
# [10, 20, 30, 40, 50]

print(L1[-2])
print(L1[-4:-2])
print(L1[:-2])
print(L1[-3:])
print(L1[:])

print('*** VV IMP - negative indexing')
list1=['a1','b2','c3','d4','5re']
#https://www.quora.com/What-is-negative-index-in-Python
#starting point:end point:if starting point to end point is moving left this value should be negative otherwise it will return []  

# ['d4', 'c3']
# []

print(list1[-2:-4:-1])
print(list1[-2:-4:1])

print("*** MM IMP")
#starting point:end point:if starting point to end point is moving right this value should be positive otherwise it will return []  
# ['b2', 'c3']
# []

print(list1[-4:-2:1])
print(list1[-4:-2:-1])

print("- for tuple")
list1=('a1','b2','c3','d4','5re')
# c3
# ('c3', 'd4', '5re')
# ()
# ('a1', 'b2', 'c3', 'd4', '5re')
# ('b2', 'd4')

print(list1[2])
print(list1[2:7])
print(list1[10:])
print(list1[:10])
print(list1[1:4:2])

#starting point:end point:if starting point to end point is moving left this value should be negative otherwise it will return []  
# ()

print(list1[-4:-2:-1])

print("*** MM IMP")
#starting point:end point:if starting point to end point is moving right this value should be positive otherwise it will return []  
# ('b2', 'c3')

print(list1[-4:-2:1])

#slice With dics -- not possible
#slice with set -- not possible

print('***index with variable -list')		#SEE
x=2
arr=[17,18,5,4,6,1]
a=list(range(len(arr)-1))
out=[]
for x in a:
    out.append(max(arr[x+1:]))
out.append('-1')
print(out)

print('*** index with variable - string')		#SEE
arr='ratanIT'
x=2
a=list(range(len(arr)-1))
out=[]
for x in a:
    out.append(max(arr[x+1:]))
out.append('-1')
print(out)

print('*** to break string')		#split
a="india"
print(a.split('d'))

print('*** to break string with '+' separator')
print('+'.join(a.split('d')))	

print('- for list: to break list in middle')
list1=[10,20,30,40]
length=len(list1)
length_avg=length//2
list2=list1[:length_avg]
print(list2)

print('***how to know length ')
print('- for string')
s='    ratan IT   '
print(len(s))

print('- for list')
l1=[10,'ratan',10.5]
print(len(l1))

print('***to remove space')
print('*to remove space at begining')
s='    ratan IT   '
print(s.lstrip())

print('*to remove space at end')
s='    ratan IT   '
print(s.rstrip())

print('*to remove space at begining and at end together')
s='    ratan IT   '
print(s.strip()) 		
print(len(s.strip()))

print('***how to remove characters at begining or at end')
s1='@@@ratan IT####'		#characters can be remove at begining or end.. not from middle
print(len(s1))
print(s1.lstrip('@'))		# to remove @ at begining
print(s1.rstrip('#'))		# to remove # at the end
print(s1.rstrip('#').lstrip('@'))
print(s1.lstrip('IT'))		# i can not remove IT here because its in middle of string

print('***see- to check memory location and data comparison #why same location?  why different location when we run everytime')
'''
id() : print memory location
is, is not : memory comparison : return boolean    		#it compares data as well as memory location
== , !=  : data comparison : return boolean
in, not in : check data available or not : return boolean
'''

print('- For string')
name1='ratan'
name2='anu'
name3='ratan'

print(id(name1))
print(id(name2))
print(id(name3))

print('**')
print(name1 is name2)				
print(name1 is name3)			#string value equal-->save at same memory location thats why here its true
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

print('- For List')
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

print('- for Dics')
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

print("***Logical operator")
x=2
y=3
print(x>1 and y>2)
print(x==1 or y==3)
print(x==1 and y==3)

print('***to check given data present or not and gets True/false')
x="california"												# Membership operator
print('z' in x)
print('z' not in x)

x=['india','ab','ssss']
print ("ab" in x)

print('***to check given value present or not and gets its index')
# difference between in and Find --> 'in' returns true / false , while 'find' returns 
# indexing of given word if avaiable else returns -1

print('- for string')
a='welcome to RatanIT'
print(a.find('Ratan'))
print(a.find('anu')) 
print(a.find('t',10,15))		# return index of 't' between 10 to 15 index

#for string find is recommended bcoz if search object not available it will return '-1'
#for string index is not recommended bcoz if search object is not available it will throw an error

print('- for List')
l1=['ratan','anu','durga','ratan']
print(l1.index('ratan'))		# by default search first 'ratan'
print(l1.index('ratan',2))		# search 'ratan' from index 2
print(l1.index('ratan',2,4))	# search 'ratan' from index 2 to 4

print('***see- to check if data is alpha ,numeric or alpha-numeric') 
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

print('***check if string is upper case, lower case or it has space')
string1='hellopython'
print(string1.islower())

string2='HelloPython3.7'
print(string2.islower())

string3='HELLO FRIENDS'
print(string3.isupper())

string4='home123'
print(string4.isupper())

string5=' '									#see- why it works only for ' '
print(string5.isspace())
 
string6='RatanIT'				
print(string6.isspace())

print('***to check if 2 variables are same or not without using =')
a=10
b=10
print(a is b)
print(a is not b)

print("***concatenate")
print('-two string')
b=" is a Country"
print(a+b)

print('-Int and Float')
'''
we can concatenate int and float because they both are numbers
we can concatenate int and float to boolean because boolean has assigned values 0 and 1
'''
print(10+10.5)
print(10+True)
print(10+False)
print(20.5+True)

print('- string and number/float/bool')
'''
print(10+'ratan')				not able to concatenate string and number/float/bool
print(10.5+'tata')
'''

print('- two list')
l1=[10,20,30]
l2=[40,50,60]
l3= l1+l2
print(l3)

# what is this?
print("***Replication")
print('- for string')
a='Hi'
print(a*2)

print('- for list')
l1=[10,20,30]
l2=l1*2
print(l2)

print('***to replace few alphabets with other alphabets in string')
print('- for string')
c=a.replace('a','a is country')
print(c)

print('*** to replace alphabets by location')
a='abcdabcd'
b=a[4:].replace('a','x',1)			# here 1 is occurance
print(b)

print('*** to delete characters in string')
# use replace

print('***to make upper case')
print('- for string')
print(a.upper())

print('***to make lower case')
print('- for string')
print(a.lower())

print('***to make uppercase lower case and lower case to upper case')
print('- For String')
print(a.swapcase())

print('***see - to make all capital letters')
print('- for string')
#print(a.Capitalize())

print('***to give corresponding number to string')
print(list(enumerate(a)))
print(tuple(enumerate(a)))

print('*to get values of enumerate')
S = "loveleetcode"
for x,y in enumerate(S):
	print(x,y)

print('*** how many times given alphabet present in string')
print('- for string')
a='ratanratan'
print(a.count('r'))				#count 'r' in a
print(a.count('ratan'))			#count 'ratan' in a
print(a.count('a',1,7))			#count 'a' between 1 and 7 position
print(a.count('ratan',2,7))		#count 'ratan' between 2 and 7 position

print('***how many times given object present in list/set/tuple')
print('- for list')
l1=[10,20,30,10,10]
print(l1.count(10))

print('***to check if string start/end with given alphabets')
string1='Welcome to RatanIT'
print(string1.startswith('Welcome'))
print(string1.endswith('IT'))

print('* to check if string start/end with given alphabets in given range')
print(string1.startswith('come',3,10))
print(string1.endswith('IT',10,18))
print(string1.endswith('IT',10,17))

print('***to arrange by ACS/Desc')
print('*** to arrnage by any logic')
''' IMP
just to arrange by asc or desc ---> sort 			#it chnages object itself
to arrange with any other logic ---> sorted 		#it crates new object with changes
'''
print('-For List')
print('*arrange number in asc order')
a=[1,4,5,3,2]
a.sort()		
print(a)

print('*arrange alphabet in asc order')
b=['a','e','b','d','c']
b.sort() 	
print(b)

print('*arrange number in desc order')
e=[1,4,5,3,2]
e.sort(reverse=True) 		
print(e)

print('*arrange alphabet in desc order')
f=['a','e','b','d','c']
f.sort(reverse=True)		
print(f)

print('***IMP: if we declare 2 lists same then if we sort any one it will sort both in this case use sorted')

print('***sorted')
print('* arrange in ascending by sorted')
f=['a','e','b','d','c']
f1=sorted(f)
print(f1)

print('* arrange in descending by sorted')
f=['a','e','b','d','c']
f1=sorted(f,reverse=True)
print(f1)

print('*arrange given list by length')
i=['bcde','cd','def','a']
j=sorted(i,key=len)
print(j)

print('*arraneg by function')
def func(x): 
    return x % 7
L = [15, 3, 11, 7] 
m = sorted(L, key = func)
print(m)

print('*do sorting of heterogenous data')
l3=[10,20.85,'ratan']
#l3.sort() 					#heterogenous sorting not supported

print('-for Dics')
print('*arrange Dictionary ascending by key,value and items')
d1={1:'ratan',2:'durga',3:'anu',4:'surya'}
print(sorted(d1.keys()))
print(sorted(d1.values()))
print(sorted(d1.items()))

print('***arrange list in reverse order without using sort')
l1=[10,20,30]
l1.reverse()
print(l1)

print('-for list of Dictionary')  # almost same as list
from operator import itemgetter
list1=[ {'name':'akhil','year':1987, 'age':32},
        {'name':'palak','year':1993, 'age':27},
		{'name':'shiv','year':1985, 'age':39}
	  ]

list2=sorted(list1,key=itemgetter('year'))
print(list2)

print("***Conditional statement")
x=3
y=3
z=5

print("*if")
if x==3 and y==3:
	print("x and y are 3")

print("*if..else")
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

print("* if...elif...else")
if (y==z):
	print("y and z are same")
elif (x==z):
	print("x and z are different")
else:
	print("i dont know")	

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

print("***for Loop")
print("*for range")
for k in range(8):
	print(k) 
for u in range(13,19):
 	print(u)
for no in range (102,130,5):
 	print(no)

print("*for List") 
fruit=["banana","apple","orange"]
for aki in fruit:
 	print(aki) 

L1=[10,20,30,40]
for x in L1[1:3]:
	print(x)

L2=[[1,2,3],['ratan','anu','tata']]
for x,y,z in L2:
	print(x,y,z)

print("*for ...break") #(it will stop 'for loop')
car=[2,15,19,20]
for x in car:
 	print(x)
 	if (x==15):
   		break
 
print("*for...in...continue")# ( this will not run remaining steps but will continue for loop)
for y in fruit:
	if (y=="apple"):
   	   continue
	print(y)
 
print("*for.....else")
for z in range (5,10):
	print(z)
else:
 	print("Finally finished!")

print('*IMP: For ...loop - increment 2 variables at same time')
a=3
b=5
c=7
for x in range(a):
    for y,z in zip(range(b), range(c)):				#MMIMP: to loop 2 variables at same time
        print('x:',x,' y:',y,' z:',z)

print("***while loop")
n = 25
while n > 20:
    print (n)
    n = n-1

print("*While...break**") #it will stop the while execution
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

print("*while...continue**") 
#it will start exceution from begining like here when i=3 its not printing i value
a=1
while a<5:
	a+= 1
	if a==3:
		continue
	print(a)

print('* while... multiple condition')
n=4102
if n==2:
    print([1,1])
else:
    A=1
    B=0
    while '0' in str(B) or '0' in str(A):
        A+=1
        B=n-A
    print([A,B])

print("***for vs while")
# for when we have starting value , ending value by incremental / decremental
# while is to check if condition is true or not

print('***packing')
print('*convert 2 list into dics')
l1=[1,2,3,4]							 
l2=['ratan','durga','anu','ratanIT']
x=zip(l1,l2)			
d=dict(x)
print(d)

print('*convert 2 tuple into dics')
l1=(1,2,3,4)							 
l2=('ratan','durga','anu','ratanIT')
x=zip(l1,l2)			
d=dict(x)
print(d)

print('*convert 2 set into dics')
l1={1,2,3,4}							 
l2={'ratan','durga','anu','ratanIT'}
x=zip(l1,l2)			
d=dict(x)
print(d)

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

print('*see - advanced')
L2=[[1,2,'ratan'],[3,'tata']]
a,b=L2
print(type(a))
print(b)
print(b[1])

print('***convert Datatypes')
print("*to convert int/float to string")
#x=str(y)

print("*to convert List to Tuple")
List1=['a','b','c','d']
Tuple1=tuple(List1)
print(Tuple1)

print("*To convert Tuple to List")
Tuple1=('a','b','c','d')
List1=list(Tuple1)
print(List1)

print("*to convert List to set")
List1=['a','b','c','d']
set1=set(List1)
print(set1)

print("*to convert set to list")
set1={'a','b','c','d'}
List1=list(set1)
print(List1)

print("*to convert Tuple to set")
Tuple1=('a','b','c','d')
set1=set(Tuple1)
print(set1)

print("*to convert Tuple to Dics ")
Tuple1=('a','b','c','d')
Dict2={i:i*2 for i in Tuple1}
print(Dict2)

print('* to convert int to string')
a=234
b=str(a)
print(type(b))

print('*to convert int to list')

print('*to convert string to list')
a='abc'
b=list(a)
print(type(b))

print('*to convert list to string')
a=['a','b','c']
b=str(a)
print(type(b))
print(b)

print('***to access all keys,values,items from Dictionary')
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

print('*to access value by keys in Dictionary ')

d1={111:'ratan',222:'anu',333:'durga',444:'ratanIT'}
#method 1  		#MM IMP
d1.get(111,'hi')		#get the value of 111 and if 111 not available in dict, return 'hi'

print(d1.setdefault(333,'jj')) 
#IMP: get the value of 333 key and if 333 key not present in dict create new key 333 with value 'jj'

#method 2
a,b,c,d=d1
print(a,b,c,d)

#method 3 (least preferable) (because if 444 is not present in dict it will throw error)
r=d1[444]
print(r)

print('*to access value in list of Dictionary')
from operator import itemgetter
list1=[ {'name':'akhil','year':1987, 'age':32},
        {'name':'palak','year':1993, 'age':27},
		{'name':'shiv','year':1985, 'age':39}
	  ]

print(list1[0]['age'])

print('* to access values in list of list')
a=[[1,2],[3,4],[5,6]]
print(a[0][1])

print('***to access data in (Nested/sub list/Multi dimension) List,tuple,set')
'''
IMP
to access data In dataframe use loc, iloc
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

print('***create another copy of list')
l1=[10,20,30]
l2=l1.copy()
print(l2)

print('-For list')
print('*add one entire list into another list')
l1=[10,20,30]
l2=[40,50,60]
l1.extend(l2)
print(l1)

print('*to add object at the end')
l1=[10,20,30]
l1.append(40)
print(l1)

print('*to add object by specific location')
l1=['ratan','anu']
l1.insert(1,'aaa')		#this will add at index 1
print(l1)
l1.insert(6,'bbb')		#this will add at index6 but we dont have index5 so it will add at the end
print(l1)

print('*to delete by object location')
l1=['ratan','durga',10,10.5]
l1.pop()			# by default it will remove last one
print(l1)
l1.pop(1)			# this will remove index 1 object
print(l1)
#l1.pop(10)			# pop index out of range

print('*to delete by object value')
l1=[10,20,30]
l1.remove(20)
print(l1)

print('*in list to delete more than one objects same time')
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

print('*in list to delete all objects') 
l1=[10,20,30]
l1.clear()
print(l1)

print('-for Dict')
print('*in dict to add object at the end')
d3={}
d3[111]='ratan'
d3[222]='anu'
d3[333]='ratan'
print(d3)

print('*to remove last key/particular key from dics')
d1={1:'aaa',2:'bbb',3:'ccc'}
d1.popitem()	# this will remove last item fron dics
print(d1)
d1.pop(2)		#this will remove key 2 from dics
print(d1)

print('*to remove all objects from dics')
d1={1:'aaa',2:'bbb',3:'ccc'}
d1.clear()
print(d1)

print('*to add one dict into another dict')
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

print('***override')
print('-Dics')
d3={}
d3[111]='ratan'
d3[222]='anu'
d3[333]='ratan'
d3[111]="repeat"		# if we try to enter same key again it will override that key and value
print(d3)

print('***None')			# None allowed in keys and values both
d2={None:None}
print(d2)

print('***matrix')
print('*to create multi dimension matrix')
# val = [0] * n  								#n is row
# for x in range (n):
#     val[x] = [0] * m  						#m is column
# print(val)

# print('*to access value in matrix')
# val[1][2] 				# row 1, column 2

# print('*to add 1 to all rows')
# for m1 in list(range(m)):
#     val[a][m1]=val[a][m1]+1

# for n1 in list(range(n)):
#     val[n1][b]=val[n1][b]+1

print('*to find no of rows and columns')
a=[[1,1,0,1],[1,0,1,0],[0,0,0,1]]
print(len(a))						# to find no of rows
print(len(a[0]))					# to find no of columns

print('***to find max/min in row and column')
matrix = [[7,8],[1,2]]
x=len(matrix)
y=len(matrix[0])
col=[]
col1=[]
for a in range(x):
    print(min(matrix[a]))			#get min value in row

for b in range(y):
    for a in range(x):
        col1.append(matrix[a][b])
    col.append(max(col1))
	#get max value in column
    col1=[]
print(col)

print('*calendar')
import calendar
c=calendar.TextCalendar(calendar.MONDAY)
str=c.formatmonth(2019,8)
#print(str)

print('*string to timestamp - strptime')
from datetime import datetime
str = '9/15/18'
x = datetime.strptime(str, '%m/%d/%y')
print(x)

str='02,aug,2010'
x=datetime.strptime(str,'%d,%b,%Y')
print(x)

#datetime(year,month,day)
import datetime
y=datetime.datetime(2020,6,18)
print(y)

print('*to convert timestamp in different format')
import datetime
y=datetime.datetime(2020,6,18).strftime('%A')
y=datetime.datetime(2020,6,18).strftime('%b/%d/%Y')
print(y)

print('*to convert from one date format to another')
from datetime import datetime
x=datetime.strptime("2013-1-25", '%Y-%m-%d').strftime('%m/%d/%y')
print(x)

print('*todays date')
from datetime import datetime
y=datetime.today().strftime('%c')
print(y)

print('***List datatype properties')
'''
1. represent group of objects :homogenus(same data type of objects) & heterogrnous( different data types of object)
example: homogenous L1=[10,20,30]  heterogenous L2=[10,'ratan',10.05]
2. indexing : forward and backward
3. duplicate objects allowed
4. mutabale: modifications are allowed
5. insertation order : e1,e2,e3 --> e1 e2 e3
'''

print('***Dics properties') 
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

print('*** regular expression')
'''
**functions
finditer  =
match  = search in first word only  
search  = search in entire string and return first match
findall = search in entire string and return all matches in list

*  =  zero or more 
+  =  one or more
?  =  zero or one

[a-z]  = all chars from a-z
[abc]  = a,b,c only
[0-9]  = all digits from 0-9
  ^    = except
^abc   = except a,b,c  
'''

import re
a='test.email+a+lex@leetcode.com'
print(re.sub('@','*',a))					#to replace

#Return a list containing every occurrence of "ai":
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

import re

# match - search only at first word
x=re.match('ratan','ratan sir')
print(x.group())

x=re.match('ratan','hi ratan sir')
print(x)

#search - search entire string anf return only first occurance
x=re.search('ratan','ratan sir')
print(x.group())

x=re.search('ratan','hi ratan sir')
print(x.group())

#findall - search entire string and return all occurance in list
x=re.findall('ratan','ratan sir ratan')
print(x)

x=re.findall('ratan','hi ratan sir')
print(x)

#symbols
print('#1- * applies to [^abc]')
#find 'soft' and before that zero or more occurance of anything other than a,b or c 
result1= re.search("[^abc]*soft","ratan sir xx yysoft are you?")
print(result1.group())

result1= re.findall("[^abc]*soft","ratan sir xx yysoft are you?")
print(result1)

print('#2- * applies to [a-j]')
#find 'w' and before that zero or more occurance of a-j and space')
result2= re.search("[a-z ]*w","ratan sir howy dabsoft are you?")
print(result2.group())

print('#3 - ? applies to [^abc]')
#find 'soft' and befor that zero or one occurance of anything other than a,b or c')
result3= re.search("[^abc]?soft","ratan sir how axyzsoft are you?")
print(result3.group())

print('#4 ')
#find 'soft' and after that zero or one occurance of anything other than a,b or c')
result4= re.findall("[^abc]*soft","ratan sir how aghsoft are ssoft are you?")
print(result4)

print('---4a -output start from 1st soft from left side')
result4= re.findall("soft[^abc]*","ratan sir how aghsoft soft are you?")
print(result4)

print('---4b - output start from 1st soft from right side')
#find 'soft' and after that zero or one occurance of anything other than a,b or c')
result4= re.findall("soft[^abc]*","ratan sir how softer ssoft why are you?")
print(result4)

print('---4c')
#first charatter must be [a-k] second character must be [0369] and 
#after than zero or more characters of [a-zA-Z0-9#] that means * applies to [a-zA-Z0-9#]')
result5= re.findall("[a-k][0369][a-zA-Z0-9#]*","hi how are a9hjhsshbh why")
print(result5)

print('IMP---')
# below also accept space so it goes all the way right
result5= re.findall("[a-k][0369][a-zA-Z0-9# ]*","hi how are a9you hsshbh")
print(result5)

print('IMP---')
# below also accept space so it goes all the way right
result5= re.findall("[a-zA-Z][a-zA-Z0-9_][a-zA-Z0-9_][a-zA-Z0-9_]*[^_]","D8fh_")
print(result5)

print('----')
result6=re.findall(r"_\B","hi_")
print(result6)

#https://www.geeksforgeeks.org/password-validation-in-python/
reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
     

print('*** Threading')
# check video 39 @ 7.00 - which shows 3 things run parallel - main code, thread1 and thread2

# We need threadig to perform multiple tasks same time parellaly
# example: video game multiplayers

# Advantage: it will reduce Processor load and performance will iprove

print('*Example:1 create and execute thread')
# Creating Thread
import threading

def print_square(num):
	print(num*num)

def print_cube(num):
	print(num*num*num)

t1=threading.Thread(target=print_square,args=(10,))
t2=threading.Thread(target=print_cube,args=(5,))

# starts the thread
t1.start()
t2.start()

print('*Example:2 short cut of example 1')
from threading import Thread
def print_square(num):
	print(num*num)

t1=threading.Thread(target=print_square,args=(10,))

# starts the thread
t1.start()

print('*Example 3')
import threading
def disp1():
	for x in range(10):
		print("Ratan world Thread")

def disp2():
	for x in range(10):
		print("Anu Thread")

#create the thread
t1=threading.Thread(target=disp1)
t2=threading.Thread(target=disp2)

#start the thread
t1.start()
t2.start()

print('*Example 4 - Main thread and how to get status of created threads')
import threading
# Main thread = default thread (where we run all code by dfault. every code has 1 main thread)
# user defined thread = thread1 , thread2 ....
#to get main thread
print(threading.main_thread())

#new thread created - Thread 1
t1=threading.Thread()
#to get status of thread 1
print(t1)

t1.start()
#to get statu of thread 1
print(t1)

print('*example 5 - threads can only be started once')
# below example will give error bcoz running same thread twice
# import threading

# t1=threading.Thread()
# t1.start()
# t1.start()				

print('*Example 6 - printing after 3 sec')
def disp():
	print(' it is printing after 3 sec')

t1=threading.Timer(3,disp)
t1.start()

print('*Example 7 - give user defined name to thread ')
import threading
print(threading.main_thread())

def f1():
	print('Thread-name',threading.currentThread())

def f2():
	print('Thread-name',threading.currentThread())

#default thread name are thread1, thread2 see below
t1=threading.Thread(target=f1)
t2=threading.Thread(target=f2)

t1.start()
t2.start()

# give user defined name to thread
t1=threading.Thread(target=f1,name='ratan')
t2=threading.Thread(target=f2,name='durga')

t1.start()
t2.start()

print('*Example 8 - to stop/wait execution')
import threading , time

def disp():
	print('good morning...')
	time.sleep(2)
	print('good evening')

t1=threading.Thread(target=disp)
t1.start()

print('*Example 9 - multiple thread')
import threading, time

def disp():
	print('good morning..')
	time.sleep(2)
	print('good night')

for x in range(5):
	t=threading.Thread(target=disp)
	t.start()

print('*Example 10 - create list of thread')
import threading, time

def disp():
	print('good morning..')
	time.sleep(2)
	print('good night')

threads=[]
for x in range(5):
	t=threading.Thread(target=disp)
	threads.append(t)
	t.start()

time.sleep(3)
print(threads)			

print('*example 11 - to halt threading execution')
import threading, time

def disp1():
	for x in range(10):
		print("Thread 1 running")
		time.sleep(1)

def disp2():
	for x in range(10):
		print("Thread 2 running")
		time.sleep(1)

#create the thread
t1=threading.Thread(target=disp1)
t2=threading.Thread(target=disp2)

#case 1
t1.start()
t1.join()	  #this will run only thread t1 and it will hold rest of all threads(main,t2) till t1 finish
t2.start()
print('rest app')  #IMP:as soon as t1 thread complete t2 and main will strat at same time

#create the thread
t1=threading.Thread(target=disp1)
t2=threading.Thread(target=disp2)

#case 2
t1.start()
t1.join()	#this will run only thread t1 and it will hold rest of all threads(main,t2) till t1 finish
t2.start()
t2.join()	#this will run only thread t2 and it will hold rest of all threads(main) till t2 finish
print('rest app')

#create the thread
t1=threading.Thread(target=disp1)
t2=threading.Thread(target=disp2)

#case 3 MMIMP
t1.start()
t1.join(2)	# this will hold rest of all threads(main,t2) for 2 seconds and after that 
			# all threads(main,t1,t2) will run together again
t2.start()
print('rest app')

print('*example 12: get name and count of running threads')
import threading, time
def disp1():
	for x in range(5):
		print("ratan IT")
		time.sleep(10)

def disp2():
	print("Durga soft")

t1=threading.Thread(target=disp1)
t2=threading.Thread(target=disp2)

t1.start()
t2.start()

print(threading.active_count()) 	#gives no of threads running this time
for x in threading.enumerate():
	print("running threads:",x.getName()) #gives name of threads running this time

print('*example 13 - threading with class')
import threading
class MyThread(threading.Thread):
	def run(self):
		for x in range(10):
			print('hi sir')

t=MyThread()
t.start()

print('*example 14 - ')
import threading
class MyThread(threading.Thread):
	def run(self):
		for x in range(3):
			print('hi sir')

t1=MyThread()
t2=MyThread()
t3=MyThread()
t1.start()
t2.start()
t3.start()

print(threading.active_count())

print('*example 15 - ')
import threading
class MyThread1(threading.Thread):
	def run(self):
		print('good morning')

class MyThread2(threading.Thread):
	def run(self):
		print('good evening')

class MyThread3(threading.Thread):
	def run(self):
		print('good night')

t1=MyThread1()
t2=MyThread2()
t3=MyThread3()
t1.start()
t2.start()
t3.start()

print('*example 16 - ')
import threading
class MyThread1(threading.Thread):
	def run(self):
		print('good morning:',threading.currentThread().getName())

class MyThread2(threading.Thread):
	def run(self):
		print('good evening',threading.currentThread().getName())

class MyThread3(threading.Thread):
	def run(self):
		print('good night',threading.currentThread().getName())

MyThread1(name='ratan').start()
MyThread2(name='durga').start()
MyThread3(name='sravya').start()

print('*** exception handling')
# default except - if we have default except than why we create except with specific erro type in video 32

print('* it will check exception from top to bottom')
print('*example 1')
try:
	print(' i am try block')	# this will be executed as normal
	print(10/0)			# if we have error in try block it will move to except block
except:
	print(10/5)
print('rest of app')

print('* example 2  #if the except block not matched')
# try:
# 	print('i am try block')	# this will be executed as normal
# 	print(10/0)		#if we have error in 'try block' it will move to 'except block'
# except TypeError as e:
# 	print(10/5)		#except block will give error becaue we asked it to support 'TypeError' and we got ZerDivisionError
# print('rest of app') 

print('* example 3   #if no error it will not execute "except block"')
try:
	print(' i am try block')	# this will be executed as normal
except:
	print(10/5)
print('rest of app')

print('* exaple 4   #only try block not allowed')
# try:
# 	print(' i am try block')	# this will give an error

print('* example 5 - #in between blocks statments not possible ')
# try:
# 	print(' i am try block')	# this will be executed as normal
# print('hi')					#invalid
# except:
# 	print(10/5)
# print('rest of app')

print('*example 6 #once we have error in try block rest of try block will not execute')
try:
	print(10+'ratan')
	print('annu')
except:
	print('ratanIT.com')
print('rest of app')

print('*example:7  #try - except - else block  #if no error in try block it will execute else block')
#scenario 1    # below else block will execute
try:
	print(10/2)
except ArithmeticError as e:
	print('ratanit.com')
else:
	print(' no exception in try block')
print('rest of app')

#scenario 2 	#below else block will not execute bcoz try block has error
try:
	print(10/0)
except ArithmeticError as e:
	print('ratanit.com')
else:
	print(' no exception in try block')
print('rest of app')

#scenario 3 	try block with no error and break statement
# here else block will execute bcoz there is no error in try block
try:
	print(10/2)
	for x in range(10):
		if x==2:
			break
except ArithmeticError as e:
	print('ratanit.com')
else:
	print(' no exception in try block')
print('rest of app')

print('*example 8 # univeral except block')
try:
	print(10/'ratan')	
except ArithmeticError as e: 		#error not matching so this will not be executed
	print('ratanit.com')
except ValueError as f:		 		#error not matching so this will not be executed
	print(' durgasoft.com')
except:				#this default except block will be excuted as its universal except block
	print('i am default except block')
else:
	print('no exception in try block')
print('rest of app')

print('* example 9  # we can combine 2 error code as well')
try:
	print(10/'ratan')	
except (ArithmeticError,ValueError) as e: 			#2 error codes are combined here
	print('ratanit.com')
except:			
	print('i am default except block')
else:
	print('no exception in try block')
print('rest of app')

print('* example 10 	#MMIMP #Baseexception - this will accept all exception' )
try:
	print(10/'ratan')	
except BaseException as e: 			#this will handle all exceptions
	print('ratanit.com')
else:
	print('no exception in try block')
print('rest of app')

print('*example 11    #child excpet error must be first and parent except error at the end')

try:
	print(10/'ratan')	
except ArithmeticError as e: 	# its child exception error so it must be before parent exception error
	print('ratanit.com')
except BaseException as f:		# Baseexception is parent exception errro , it must be last
	print(' durgasoft.com')
else:
	print('no exception in try block')
print('rest of app')

print("*example 12 - nested try block")

# try:
# 	print('outer try block')
# 	n=int(input('enter a number :'))
# 	print(10/n)
# 	try:
# 		print('inner try')
# 		print('ratan'+10)
# 	except BaseException as a:
# 		print('durgasoft.com')
# 	else:
# 		print('inner else block')
# except BaseException as b:
# 	print('ratanIT.com')
# else:
# 	print("outer else block")
# print('rest of the applications.....')

print('*example 13 - handling exception while calling function')
def m1():
	print(10/0)

try:
	m1()
except BaseException as a:
	print(10/5)

print('* example 14 - finally block = always executed')
#case1
try:
	print(10/2)
except BaseException as a:
	print('except')
finally:
	print('finally')

#case 2
try:
	print(10/0)
except BaseException as a:
	print('except')
finally:
	print('finally')

#case 3				#finally will be executed eventhough in code error
# try:
# 	print(10/0)
# except ValueError as a:
# 	print('except')
# finally:
# 	print('finally')

#case 4				#in this case also finally will be executed
# try:
# 	print(10/0)
# except ValueError as a:
# 	print(10/0)
# finally:
# 	print('finally')

#case 5 			# only try block with finally block allowed
# try:
# 	print(10/2)
# finally:
# 	print('finally')

print('*example 15 - when finally block will not execute')
#case 1				#here code get error before try block so finally block will not execute
# print(10/0)
# try:
# 	print(10/2)
# finally:
# 	print('finally')

#case 2    			#see - exit will stop execution of all remaining code
# import os
# try:
# 	print(10/2)
# 	os._exit(0)
# finally:
# 	print('finally')

print('* interview question')
def hi():
	try:
		return 10
	except:
		return 20
	finally:
		return 30
hi()
#ans is 30

print('*example 16 - Raise - to create user defined exception ')
#Excepttion
#system defined exceptions are TypeError,BaseException ...
#to create user defined errors use 'Raise'

#step 1: create the user defined exception
class InvalidAgeException(Exception):
	def __init__(self,msg):
		self.msg=msg

#step 2: use the user defined exception in our project
# def status(age):
# 	if age>20:
# 		print('eligible for marriage')
# 	else:
# 		raise InvalidAgeException("not eligible for marriage")
# status(10)


# Treenode
# Listnode 
# length?
#SQL pivot