print('***absolute')
print(abs(-72.50))


print("***print")
print('*print string,int and float')
eid,ename,esal=111,'ratan',100.45
print(eid)
print(ename)
print(esal)

print('* to print next line')
print("Hello\nWorld!")

print('*print 2 lines together')
print(eid,end='') 				 # this will print next line, in same line
print(' ',ename)

print('*print hard code value and variable together')
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

print('***formate specifier')		#mainly use as variable in print statement
'''
Method 1
int 		float		string    #make sure %g is for int or float?
%d 	%g   	%f 	  		%s

Method 2
{}
'''

eid,ename,esal=111,'ratan',100.45

print('*print int,string,float with formate specifier')
# for % , if %d is first its value must be first...so its sequence is important

print('%d %s %g' %(eid,ename,esal))								#format
print('emp id =%d emp name =%s emp sal=%g' %(eid,ename,esal))	#real time example

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

print('*how to know which Datatypes (number, string ,boolean, List, tuple or Dics)')
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
#IMP:first give non-default value then default value

def default(x,y=25,z=5):  
	print(x+y+z)

default(10)   #here y=25,z=5 default value and x=10 because we gave w value while calling  
default(10,20) #here z=5 because while calling we gave x=10,y=20
default(y=10,x=2) #if we change sequence of variable then we need to specify x=2 

#VVIMP
#default(20,y=40,30) # Invalid : once we give y=40 then rest of all argument must be z=something.
																	#we can not put 30 after y=40

default(50,60,z=10)  # valid

print("***to call function")
#IMP: '()' this symbol call function
#VVV IMP: always call funcation after its defined

def a1():
	print("a1")
a1() 					# this will call function a1

print("***IMP")
def akhil():
	print("akhil")
a3=akhil() 						# this will call akhil function
   
def a(x):
	print(x+10)
b=a
b(2) 					 		# this will call function a

print("*to call 1 function inside another function")
def g():
    print("Hi, it's me 'g'")
    print("Thanks for calling me")
def f(func):
    print("Hi, it's me 'f'")
    print("I will call 'func' now")
    func() 						#func=g  #step2: this will call function g
f(g) 							#step 1: this will call function f

print("*function within function")
def outside():
	def inside():
		print("i am inside") #step2
	print("i am outside") #step1
	inside() # this will call function inside
outside() # this will call function outside

print("*No call")
def inner1(): 
    print("Hello, this is before function execution") 
    func() # this will not call func unction
    print("This is after function execution")
    return inner1

print('*function with n number of arguments')
print('*function with n arguments alone,at begining,at end')
#case 1
def multi(*a):					# for n number of arguments use *
	print(a)
multi(1,2,3,4)

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

#case 3
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
star(35,94,100,90,name='tata')  			#here name1=35 and *b=94,100,90 and name='tata'

print("***Return (IMP)")
def function_that_prints():
    print("I printed")

def function_that_returns():
    return "I returned"
    print("after return")

print("IMP - The return statement terminates the execution of a function")
print("IMP - function calling  will give only print values,not return values ")
f1 = function_that_prints() 				#this will call function_that_prints
f2 = function_that_returns() 				# this will call function_that_returns

print("IMP - to access return values assign variable to function calling")
print("and print the variable because retuen assigns value to function") 
print("so we need to print calling function ")

print(f1) 
# or
print(function_that_prints())			#see its answer 

print(f2)
# or
print(function_that_returns())			#see its answer
 
print("example 2")
def no_return(x,y):
    c = x + y
    return c
print(no_return(4,5))

print('* Multiple return statement')
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
print('* how to update Global variable value, inside function?')
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

print("***arithmetic Operator")
# +,-,*,/
x=10
y=20
print(x+y)
print(x*y)
print(y-x)
print(y/x)

print('* sum,averge,mean')
a=[12,52,52]

#sum
print(sum(a))

#average
print(sum(a)/len(a))

#mean
import statistics
b=statistics.mean(a)
print(b)

print("* exponent")
#method 1
x=10
n=2
print(x**2)				# equal to 10 rest to 2

#method 2
x=10
n=2
print(pow(10,2))		# equal to 10 rest to 2

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

print("***Logical operator")
#and,or
x=2
y=3
print(x>1 and y>2)
print(x==1 or y==3)
print(x==1 and y==3)

print('***to check given value present or not and gets True/false')
x="california"							# Membership operator
print('z' in x)
print('z' not in x)

x=['india','ab','ssss']
print ("ab" in x)

print('***to check given value present or not and gets its index')
# difference between in and Find --> in returns true / false , find returns indexing of given word
# if avaiable returns index else returns -1

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

print('***string-regular expression')

print('***get remaing value after division')
											#Modulus
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

print('***to get few alphabets of string // to get few objects from list/set/tuple without for loop')
print('*** MMIMP: slice')
print('- for string')

# -7 -6 -5 -4 -3 -2 -1  		#negative indexing
s= 'ratanIT'
# 0 1 2 3 4 5 6 				#positive indexing

#starting point:end point:if starting point to end point is moving left this value should be negative otherwise it will return []  
#starting point:end point:if starting point to end point is moving right this value should be positive otherwise it will return []  

print(s[2])
print(s[2:4])
print(s[1:4:2])
print(s[:4])			#MMIMP: start point not given so it will start from all the way left
print(s[2:])			#MMIMP: end point not given so it will end all the way right
print(s[:])
# print(s[9])  			#Indexerror: string out of range

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

print('*** VV IMP - negative indexing')
list1=['a1','b2','c3','d4','5re']
#https://www.quora.com/What-is-negative-index-in-Python
#starting point:end point:if starting point to end point is moving left this value should be negative otherwise it will return []  
print(list1[-2:-4:-1])
print(list1[-2:-4:1])

print("*** MM IMP")
#starting point:end point:if starting point to end point is moving right this value should be positive otherwise it will return []  
print(list1[-4:-2:1])
print(list1[-4:-2:-1])

print("- for tuple")
list1=('a1','b2','c3','d4','5re')
print(list1[2])
print(list1[2:7])
print(list1[10:])
print(list1[:10])
print(list1[1:4:2])

#starting point:end point:if starting point to end point is moving left this value should be negative otherwise it will return []  
print(list1[-4:-2:-1])
print(list1[-4:-2:-1])

print("*** MM IMP")
#starting point:end point:if starting point to end point is moving right this value should be positive otherwise it will return []  
print(list1[-4:-2:1])
print(list1[-4:-2:1])

#slice With dics -- not possible
#slice with set -- not possible

print('* index with variable -list')		#SEE
x=2
arr=[17,18,5,4,6,1]
a=list(range(len(arr)-1))
out=[]
for x in a:
    out.append(max(arr[x+1:]))
out.append('-1')
print(out)

print('* index with variable - string')		#SEE
arr='ratanIT'
x=2
a=list(range(len(arr)-1))
out=[]
for x in a:
    out.append(max(arr[x+1:]))
out.append('-1')
print(out)

print('*to break string')		#split
a="india"
print(a.split('d'))

print('* to break string with '+' separator')
print('+'.join(a.split('d')))	

print('- for list: to break list in middle')
list1=[10,20,30,40]
length=len(list1)
length_avg=length//2
list2=list1[:length_avg]
print(list2)

print("***concatenate")
print('-two string')
b=" is a Country"
print(a+b)

print('-Numbers(Int and Float)')
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

print('*replace by location')
a='abcdabcd'
b=a[4:].replace('a','x',1)			# here 1 is occurance
print(b)

print('* to delete characters in string')
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
print('***to check if string start/end with given alphabets in given range')
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


''' ratan '''
print("***how to get all keywords")
import keyword
print(keyword.kwlist)

''' for 2.x we dont need parenthesis to print while 3.x requires parenthesis
    because we can see in 2.x print is keyword while in 3.x print is not keyword'''

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

print('***INPUT')

'''
print('* take input as string and then do concatenate')
a=input('A=')				#IMP:  Input takes all value as string
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

print('***how to know length ')
print('- for string')
s='    ratan IT   '
print(len(s))

print('- for list')
l1=[10,'ratan',10.5]
print(len(l1))

print('***how to remove space')
print(s.strip()) 		#to remove space at begining and at the end
print(len(s.strip()))

print('***how to remove characters')
s1='@@@ratan IT####'					#characters can be remove at begining or end.. not from middle
print(len(s1))
print(s1.lstrip('@'))		# to remove @ at begining
print(s1.rstrip('#'))		# to remove # at the end
print(s1.rstrip('#').lstrip('@'))
print(s1.lstrip('IT'))		# i can not remove IT here because its in middle of string

print('***to check memory location and data comparison')
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


print('***List datatype properties')
'''
1. represent group of objects :homogenus(same data type of objects) & heterogrnous( different data types of object)
example: homogenous L1=[10,20,30]  heterogenous L2=[10,'ratan',10.05]
2. indexing : forward and backward
3. duplicate objects allowed
4. mutabale: modifications are allowed
5. insertation order : e1,e2,e3 --> e1 e2 e3
'''
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
l1.pop(1)			# this will remobe index 1 object
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

print('***get maximum and minimum values in list')
l1=[10,20,30]
print(max(l1))
print(min(l1))

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

#regular expression
import re
a='test.email+a+lex@leetcode.com'
print(re.sub('@','*',a))					#to replace

# Treenode



# Listnode 
# length?


#SQL pivot


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


