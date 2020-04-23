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


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        out=[]
        y=None
        z=None
        list_len=list(range(len(nums)))
        #print(list_len)
        for x in list_len:
            if x%2 != 0:
                #global y
                y=list_len[x]
                print('y :',y)
            elif x%2 ==0:
                #global z
                z=list_len[x]
                print('z :',z)  
            for m in list(range(y)):
                out.append(z) 

        print(out)   


