#fibonacci
#array rotation

# Program to print duplicates from a list of integers
# Break a list into chunks of size N in Python
# Program to accept the strings which contains all vowels
# Generating random strings until a given string is generated
# Python program to split and join a string
# Check if a given string is binary string or not
# Find all close matches of input string from a list
# Remove all duplicates from a given string in Python 
# Check for URL in a String
# regualr expression

# Find duplicate characters within string
s1='hi how are'

# to check if a string can become empty by recursive deletion
str1 = "GEEGEEKSKS"
str2 = "GEEKS"

str1 = "01010101010"
#print(type(str1))

#------------------------------------------------------------------
# Program to create grade calculator in Python
# Check order of character in string using OrderedDict( )
# K’th Non-repeating Character in Python using List Comprehension and OrderedDict
# Python counter and dictionary intersection example (Make a string using deletion and rearrangement)
# Python dictionary, set and counter to check if frequencies can become sa# Possible Words using given characters in Python
# Python Counter to find the size of largest subset of anagram words

# Print anagrams together in Python using List and Dictionary
# Check if binary representations of two numbers are anagram
# from collections import Counter
# arr = ['cat', 'dog', 'tac', 'god', 'act']

# to remove Nth occurrence of the given word
# list1= ["geeks", "for", "geeks","why"]
# word = 'geeks'
# N = 1
# count=0
# Q=list(range(len(list1)))
# print(Q)
# print(list1[0])
# print(list1[1])
# print(list1[2])
# print(list1[3])

# for x in Q:
# 	if (list1[x]=='geeks'):
# 		count=count+1
# 		if count==N:
# 			list1.pop(x)

# print(list1)

a1='lhello'
b=10
c=10.3
d=True
l1=(1,2,3,4)
l2=[45,84,99,9]
d1={1:'hi',2:'hi'}
l3=['ratan','anu','durga']		#decide by ASCI value
d2={'ratan':1,'durga':2,'anu':3,'surya':4}
eid,ename,esal=111,'ratan',100.45

T1=('a1','b2','c3','d4','5re')
print("Hello\nWorld!")


print('***MMIMP - deep copy and shallow copy')
print('*Shallow copy')
l1=[45,84,99,9]
l2=l1
l2.append(66)
print(l1)

print('*deep copy')
import copy
l3=copy.deepcopy(l1)
l3.append(60000)
print(l3)
print(l1)





print('*MRO (method resolution order)')
# MRO decideds hirarchy / priority level in python inheritance
class A:
    def process(self):
        print('A process()')

class B(A):
    pass

class C(A):
    def process(self):
        print('C process()')

class D(B,C):
    pass

#obj = D()
#obj.process()
print(D.mro())