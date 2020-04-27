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

groupSizes=[3,3,3,3,3,1,3]
out1=[]
out2=[]
x=list(set(groupSizes))
#print(x)
for x1 in x:
    print(x1)
    for x2 in list(range(len(groupSizes))):
        print(x2)
        if groupSizes[x2]==x1:
            out2.append(x2)
            #print(out1)
    out1.append(out2)
    out2.pop()
    print(out1)

# out1=[]
# out2=[]
# a=5
# out2.append(a)
# out1.append(out2)
# print(out1)

# out2.pop()

# out2.append(0)
# print(out2)
# out1.append(out2)
# print(out1)



# l = []
# l.append([1,2,3])
# l.append([4,5,6])
# print(l)



#1221
# if s[x]=='R' ---> count1=1
# if s[x]=='L' ---> count2=1
# 			Add logic for last index
#		if s[x+1]=='R' :
#			if count1=count2:
#				count=count+1