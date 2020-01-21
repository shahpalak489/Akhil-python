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

print('count ratan in given string')
a='ratanit ratan'
b=a.split()
count=0
for x in b:
    if 'ratan' in x:
        count+=1
print(count)

print(" python in built methods")

print("first 10 numbers")
for x in range(10):
    print(x)

print(" 10 numbers with 3 increment")
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
