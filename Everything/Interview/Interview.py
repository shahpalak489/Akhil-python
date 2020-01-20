#count 'ratan' in given string
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

print("average of list, sum of list, * of list, / of list")

'''
write a function that takes 2 strings as arguments and returns string containing
one copy of each character that occurs in both input arguments

common("book","kangaroo") --> "ok" or "ko"
common("apple","banana") --> "a"

'''

''' IMP
just to arrange by asc or desc ---> sort
to arrange with any other logic ---> sorted
'''
print("arrange in asc order")
a=[1,4,5,3,2]
a.sort()
print(a)

b=['a','e','b','d','c']
b.sort()
print(b)

print("arrange in desc order")
e=[1,4,5,3,2]
e.sort(reverse=True)
print(e)

f=['a','e','b','d','c']
f.sort(reverse=True)
print(f)

print("arrange given list by length")
i=['bcde','cd','def','a']
j=sorted(i,key=len)
print(j)

print("arraneg by function")
def func(x): 
    return x % 7
L = [15, 3, 11, 7] 
m = sorted(L, key = func)
print(m)

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
