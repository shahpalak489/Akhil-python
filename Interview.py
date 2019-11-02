# Palindrome ( start to end and end to start is same)
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


#swap ( assign x value to y and y value to x)
	#Method 1 (Using Arithmetic Operators) (without temp var )
x = 5
y = 10
# x now becomes 15 
x = x + y   # x= 15
# y becomes 10 
y = x - y  # y = 5
# x becomes 5 
x = x - y   # x = 10
print("After Swapping: x =", x, " y =", y)

	#Method 2 - temp var
x = 10
y = 5
'''z temp var'''
z = x # Z = 10
x = y # x = 5
y = z # y = 10
print("After Swapping: x =", x, " y =", y)


#Anagram( letters count same for 2 words)
from collections import Counter 
def isAnagram(s, t):
    if len(s) == len(t):
        print("anagram is possible")
        #print(Counter(s))
        #print(Counter(t))
        if Counter(s) == Counter(t):
            print("it is a anagram")
        else:
            print("length is same but not anagram")
    else:
        print("length is different")

isAnagram('pal', 'lap')


#Fizzbuzz ( if multiply by 3 print fizz, by 5 buzz , by 3 and 5 fizzbuzz)
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


#fibonacci (aagad na 2 numbers no sarvado)
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..

## Method 1 (Use recursion) :
def Fibonacci(n): 
    if n < 0: 
        print("Incorrect input") 
    # First Fibonacci number is 0 
    elif n == 1: 
        return 0
    # Second Fibonacci number is 1 
    elif n == 2: 
        return 1
    else: 
        return Fibonacci(n-1) + Fibonacci(n-2) #n=4, 3, 2
print(Fibonacci(3)) 

## method:2 Space Optimized: without recursion
def fibonacciSecond(n): 
    a = 0
    b = 1
    print("n: "+str(n))
    if n < 0: 
        print("Incorrect input") 
    elif n == 0: 
        return a # 0
    elif n == 1: 
        return b # 1
    else:
        for i in range(2,n): #2, 3, 4
            print("n: "+str(n))
            print("i: "+str(i))
            c = a + b   # c = 1, 2, 3
            a = b       # a = 1, 1, 2
            b = c       # b = 1, 2, 3
            print(c,a,b)
        return b 
print(fibonacciSecond(3))