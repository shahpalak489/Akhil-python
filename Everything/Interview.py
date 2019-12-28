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
#(assign x value to y and y value to x)
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

print("Revert Dictioanry mapping")
map1={'a':1,'b':2}

map2={y:x for x,y in map1.items()}
print(map2)


