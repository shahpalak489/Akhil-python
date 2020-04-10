print('one list more than 30 , one list less than 30')
l1=[10,20,30,10.8,90,100,150]
l2=[]
l3=[]
for x in l1:
    if x <= 30:
        l2.append(x)
    elif x>30:
        l3.append(x)
print(l2)
print(l3)

print('count words in given string')
a='ratanit ratan'
b=a.split()
count=0
for x in b:
    if 'ratan' in x:
        count+=1
print(count)

print("first 10 numbers")
for x in range(10):
    print(x)

print("10 numbers with 3 increment")
for x in range(2,10,3):
    print(x)

print("first 10 odd numbers")
for x in range(10):
    if x%2 == 0:
        print(x)

print('create 2 lists(one list from 1st index and second list from second index) from one list ')
l1=[[1,2],['ratan','anu'],[10.5,50.9]]
l3=[]
l4=[]
for x,y in l1:
    l3.append(x)
    l4.append(y)
print(l3)
print(l4)

print("average of list, sum of list, * of list, / of list")

'''
write a function that takes 2 strings as arguments and returns string containing
one copy of each character that occurs in both input arguments

common("book","kangaroo") --> "ok" or "ko"
common("apple","banana") --> "a"

'''


#Revert Dictioanry mapping
map1={'a':1,'b':2}

map2={y:x for x,y in map1.items()}
print(map2)

print("***Palindrome(start to end and end to start is same")
# Input : malayalam
# Output : Yes

# Input : geeks
# Output : No
s = "malayalam"
rs = s[::-1]
#print(rs)
if s==rs:
	print("string is palindrome")
else:
	print("sorry")

print("***swap") 
x,y=10,20
x,y=y,x
print(x)

print("***Anagram( letters count same for 2 words")
from collections import Counter 
def isAnagram(s, t):
    if len(s) == len(t):
        print("anagram is possible")
        #print(Counter(s))
        #print(Counter(t))
        if Counter(s) == Counter(t): # counter comes from count
            print("it is a anagram")
        else:
            print("length is same but not anagram")
    else:
        print("length is different")
isAnagram('pal', 'lap')

print("***Fizzbuzz") 
#(if multiply by 3 print fizz, by 5 buzz , by 3 and 5 fizzbuzz)
#Python program to print Fizz Buzz 
#loop for 100 times i.e. range 
for i in range(20):  
    # number divisible by 15 (divisible  
    # by both 3 & 5), print 'FizzBuzz'
    if i % 15 == 0:  
        print("FizzBuzz")                                          
        continue
    # number divisible by 5, print 'Buzz' 
    elif i % 5 == 0:
        print("Buzz")
        continue
    # number divisible by 3, print 'Fizz'
    elif i % 3 == 0:  
        print("Fizz")                                   
        continue
    # print numbers 
    print(i)

print("***fibonacci")
# (aagad na 2 numbers no sarvado)
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, …….

def FibonacciNumbers(n): 
    f1 = 0
    f2 = 1
    if (n < 1): 
        return
    for x in range(0, n): 
        print(f2, end = " ") 
        next = f1 + f2 
        f1 = f2 
        f2 = next
print(FibonacciNumbers(7))

print("***first 15 numbers")
for i in range(0,15):
    print(i)

print("***all even numbers till 15")
for i in range(15):
    if i%2 ==0:
        print(i)
#even numbers without modules

#fibonnaci first 10 with generator

# sum of values
def sum(x,y):
	z=x+y
	print(z) 

#sum(10,15)

#factorial of n
n=4
fact=1
for x in range(1,n+1):
	fact=fact*x
print(fact)

#interest rate
def interest(x,y,z):
	a=(x*y*z)/100
	print(a)
#interest(100,5,5)

#armstrong number
def armstrong(a):
	b=str(a)
	c=len(b)
	x=eval(b[0])
	y=eval(b[1])
	z=eval(b[2])

	print(pow(x,c)+pow(y,c)+pow(z,c))
#armstrong(120)

#area of circle
def area(pi,r):
	redius=pi*(r*r)
	print(redius)

area(3.14,15)

#prime numbers
n=233
m=list(range(2,n))
#print(m)
for x in m:
	if (n%x) == 0:
		print(str(n)+' is not prime number with '+ str(x))
		break	
else:
	print(str(n)+' is prime number')

#split list and add first section to end
list1=[10,20,30,40]
length=len(list1)
length_avg=length//2
list2=list1[:length_avg]
list3=list1[length_avg:]

list3.extend(list2)
print(list3)

#Monotonic
a=[-10,-20,-30]
l=len(a)
m=list(range(l-1))

if a[0]-a[1] < 0:
	for x in m:
		if a[x]-a[x+1] > 0:
			print('no Monotonic')
			break
	else:
		print('Monotonic')

if a[0]-a[1] > 0:
	for x in m:
		if a[x]-a[x+1] < 0:
			print('no Monotonic')
			break
	else:
		print('Monotonic')

#multiply all numbers
lis1=[1,3,4,5]
y=1
for x in lis1:
	y=x*y
print(y)

#second biggest interger
list1=[1,3,4,5,2,5]
list2=set(list1)
list3=list(list2)
#print(list2)
l=len(list3)
print(list3[l-2])

#Python program to find sum of elements in list
list1=[10,20,30,40]
a=0
for x in list1:
	a=a+x
print(a)

#find odd and even number
list1=[2,15,20,78]
list2=[]
list3=[]
for x in list1:
	if x%2 == 0:
		list2.append(x)
	if x%2 != 0:
		list3.append(x)
print(list2)
print(list3)

#find positive and negative number
list1=[2,15,-20,-78]
list2=[]
list3=[]
for x in list1:
	if x > 0:
		list2.append(x)
	if x < 0:
		list3.append(x)
print(list2)
print(list3)


#count odd and even number
list1=[2,15,20,78]
odd_count=0
even_count=0
for x in list1:
	if x%2 == 0:
		odd_count=1+odd_count
	if x%2 != 0:
		even_count=1+even_count
print(odd_count)
print(even_count)

# Python program to find Cumulative sum of a list
List1=[10,20,30,40]
list2=[]
a=0
for x in List1:
	a=a+x
	list2.append(a)
print(list2)

# list: to deltete by values
tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'), 
                  ('krishna', 'akbar', '45'), ('',''),()]

for x in tuples:
	if x==():
		tuples.remove(())
print(tuples)

# Reverse words in a given String in Python
s='hi how are you'
s1=s.split(' ')
s1=s1[::-1]
print(s1)
str1=''
for x in s1:
	str1+= x
	str1+= ' '
print(str1)

# to remove Nth character from string 
s='palindrome'
n=1
l=list(range(len(s)))
res=''
for x in l:
	if x==n:
		continue
	else:
		a=s[x]
		res= res+a
print(res)

#print even length words in a string
s='hey hi how are you?'
s1=s.split(' ')
#print(s1)
s2=''
for x in s1:
	if len(x)%2 == 0:
		s2=s2+x
print(s2)

# swap characters in a String
i=5
j=9
s='palin/dro.me'
sl=list(s)
sl[i],sl[j]=sl[j],sl[i]
s2=''
for x in sl:
	s2=s2+x
print(s2)

# Count the Number of matching characters in a pair of string
s1='akhil%$'
s2='palak@$'

count=0
for x in s1:
	if x in s2:
		count=count+1
print(count)

#Permutation
#string: all possible combination
a='abc'
for x in a:
	for y in a:
		for z in a:
			b=x+y+z
			print(b)

#string : all possible combination without repeation
a='abc'
for x in a:
	for y in a:
		for z in a:
			if x==y:
				continue
			elif y==z:
				continue
			elif x==z:
				continue
			else:
				b=x+y+z
			print(b)

# Python program to find uncommon words from two Strings
s1='hi how are you?'
s2='hi i am fine how abt you?'
s1=list(s1.split(' '))
s2=list(s2.split(' '))

for x in s2:
	if x not in s1:
		print(x)

# Execute a String of Code in Python
code =  '''
a = 6+5
print(a)
'''
exec(code)

# rotate a string
# move characters left / right
s = "GeeksforGeeks"
d = 2
left_rotate=s[d:]+s[:d]
print(left_rotate)
right_rotate=s[-2:]+s[:-2]
print(right_rotate)