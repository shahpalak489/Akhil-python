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
#slice
a="india"
print (a[1])
#split
print(a.split('d'))
#Range
print(a[1:3])
#Membership
print("d" in a)
print("x" not in a)
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


#Dataframe

#Pip install pandas

import pandas as pd

#To create 1 column without column name
lst=["shah","patel"]
df=pd.DataFrame(lst)
print(df)

#To create 1 column with column name
lst= {"city":["baroda","bangalore"]}
df=pd.DataFrame(lst)
print(df)

#To make multiple column with column names
lst= {"city":["baroda","bangalore"],
		"state":["GJ","KA"]}
df=pd.DataFrame(lst)
print(df)

lst={"city":["baroda","surat"],
		"zip":["06","05"]}
df=pd.DataFrame(lst)
print(df)

print("-------1")
lst2= {"city":["baroda","bangalore","surat","mang"],
		"state":["GJ","KA","GJ","KA"]}
df2=pd.DataFrame(lst2)
print(df2)
print("-------2 not possible ")
#print(df2.loc[2,1]) # row-2 :col-1   
print("-------3")
print(df2.iloc[2,1]) # row-2 :col-1 
print("-------4")
print(df2.ix[2,1]) # row-2 :col-1 
print("-------5")
print(df2.loc[2,"city"]) # row - 2 :col- city
print("-------6")
print(df2.ix[2,"city"]) # row - 2 :col- city
print("-------7")
print(df2.loc[:2,"city"]) # row - 0,1,2 :col- city ( see)
print("-------8")
print(df2.ix[:2,"city"]) # row - 0,1,2 :col- city (see)
print("-------9")
print(df2.iloc[:2,:1]) # row - 0,1 :col- 0   (see)
print("-------10")
print(df2.ix[:2,:1]) # row - 0,1,2 :col- 0  (see)
print("-------11")
