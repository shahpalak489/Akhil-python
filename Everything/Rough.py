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

# groupSizes=[3,3,3,3,3,1,3]
# out1=[]
# out2=[]
# x=list(set(groupSizes))
# #print(x)
# for x1 in x:
#     print(x1)
#     for x2 in list(range(len(groupSizes))):
#         print(x2)
#         if groupSizes[x2]==x1:
#             out2.append(x2)
#             #print(out1)
#     out1.append(out2)
#     out2.pop()
#     print(out1)

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
# x=list(range(len(s)))
#         print(x)
#         z=len(s)
#         count=0
#         for y in x:
#             if y==z-1 and s[y]=='R':
#                 count=count+1
#             elif s[y]=="R":
#                 if s[y+1]=='R':
#                     pass
#                 else:
#                     count=count+1
#         return count
        
#      #"RLRRRLLRLL" 

# if s[x]=='R' ---> count until s[x]=L  --> count1
# if s[x]=='L' ---> count until s[x]=r  --> count2
#			if count1=count2:
#				count=count+1



# s="RLLLLRRRLR"
# s_len=list(range(len(s)))
# t=len(s)
# count1=0
# count2=0
# count=0
# for x in s_len:
#     if s[x]=='R':
#         count1=count1+1
#         print('x =',x,'count1=',count1)
#     elif s[x]=='L':
#         count2=count2+1
#         print('x =',x,'count2 =',count2)
#         if x==t-1:
#             if count1==count2:
#                 count=count+1
#         elif s[x+1]=='R':
#             if count1==count2:
#                 count=count+1
#     print('count =',count0)
# print(count)

#print('###657')
# a='UD'
# U=1
# D=-1
# L=-1
# R=1
# count=0
# for x in a:
# 	count=count+value(x)	
# print(count)


# #461
# x=680142203
# y=1111953568
# a=bin(x)
# print(a)
# if 'b' in a:
# 	a=int(a[2:])
# m="%04d" % a
# print(m)

# b=bin(y)
# print(b)
# if 'b' in b:
# 	b=int(b[2:])
# n="%04d" % b
# print(n)
# count=0
# for x in range(len(m)):
# 	if m[x] != n[x]:
# 		count += 1
# print(count)


# print('##811')
# print(bin(7)[2:])



# import collections
# cpdomains=["9001 discuss.leetcode.com"]
# counter = collections.Counter()
# for cpdomain in cpdomains:
# 	print('cpdomain:',cpdomain)
# 	c, *domains = cpdomain.replace(" ",".").split(".")
# 	print('count:',c)
# 	print('domain',domains)
# 	for i in range(len(domains)):
# 		counter[".".join(domains[i:])] += int(c)
# print([" ".join((str(v), k)) for k, v in counter.items()])



# import collections
# cpdomains=["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
# counter = collections.Counter()
# for cpdomain in cpdomains:
# 	print('cpdomain:',cpdomain)
# 	c, *domains = cpdomain.replace(" ",".").split(".")
# 	print('count:',c)
# 	print('domain',domains)
# 	for i in range(len(domains)):
# 		#print(counter[".".join(domains[i:])])
# 		print('c:',int(c))
# 		counter[".".join(domains[i:])] += int(c)
# 		print(counter[".".join(domains[i:])])
# print([" ".join((str(v), k)) for k, v in counter.items()])

#print(collections.Counter[".".join(['discuss','leetcode','com'][0:])])

# s="hehe hehe hehe hehe"
# out=''
# split1=s.split(' ')
# for x in range(len(split1)):
#     y=split1[x][::-1]
#     out += y
#     if x != (len(split1)-1):
#         out += ' '
# print (out)

 
#print('##665')
#nums=[4,2,1]			#False
#nums=[4,2,3]			#true
#nums=[4,2,1]			#f
#nums=[-1,4,2,3]			#t
# pick 1, rest find min, that if biiger right , if smaller left
# fianl : find min and max, start from min then min+1 if present should be right not count 1 then min+2...if you find 2 ans next both shoudl be on right

#nums=[13,14,12,14]			#f
nums=[1,1,1]
nums_len=len(nums)
# count = 0
# if nums_len==1 or nums_len==2:
#     print(True)
# else:
# 	maximum=max(nums)
# 	minimum=min(nums)
# 	nums_sort=sorted(nums)
# 	print(nums_sort)
# 	for x in range(len(nums_sort)-1):
# 		a=[i for i in range(len(nums)) if nums[i] == nums_sort[x]]
# 		b=[i for i in range(len(nums)) if nums[i] == nums_sort[x+1]]
# 		print('x:',x,'a:',a,'b:',b)
# 		a_len=len(a)
# 		b_len=len(b)
# 		for x in range(a_len):
# 			for y in range(b_len):
# 				if a[x] > b[y]:
# 					count+=1
# 		print(count)

# 	if count > 1:
# 		print(False)
# 	else:
# 		print(True)



nums=[1,1,1]
# nums_len=len(nums)
# count = 0
# if nums_len==1 or nums_len==2:
#     print(True)
# else:
# 	maximum=max(nums)
# 	minimum=min(nums)
# 	nums_sort=sorted(nums)
# 	print(nums_sort)
# 	for x in nums_sort:
# 		a=[i for i in range(len(nums)) if nums[i] == x]
# 		b=[i for i in range(len(nums)) if nums[i] == (x+1)]
# 		print('x:',x,'a:',a,'b:',b)
# 		a_len=len(a)
# 		b_len=len(b)
# 		for x in range(a_len):
# 			for y in range(b_len):
# 				if a[x] > b[y]:
# 					count+=1
# 		print(count)

# 	if count > 1:
# 		print(False)
# 	else:
# 		print(True)


# nums=[1,3,5,2,4]
# one, two = nums[:], nums[:]
# print('one:',one)
# print('two:',two)
# for i in range(len(nums) - 1):
# 	print('i:',i)
# 	if nums[i] > nums[i + 1]:
# 		one[i] = nums[i + 1]
# 		print('one[i]:',one[i])
# 		two[i + 1] = nums[i]
# 		print('two[i+1]:',two[i+1])
# 		break
# print('one:',one)
# print(sorted(one))
# print('two:',two)
# print(sorted(two))
# print(one == sorted(one) or two == sorted(two))

# candies = [2,3,5,1,3]
# extraCandies = 3
# ma = max(candies)
# print([x+extraCandies >= ma for x in candies])


# x=max(candies)
# y=len(candies)
# out=[]
# # for a in range(y):
# #     if candies[a]+ extraCandies >= x:
# #         out.append(True)
# #     else:
# #         out.append(False)
# # return out


S = "loveleetcode"
C = 'e'
out,out1=[],[]
#print(S.index('e',5))
no=[x for x in range(len(S)) if S[x]==C]
# for x in range(len(S)):
# 	for y in no:
# 		out.append(abs(y-x))
# 	out1.append(min(out))
# 	out=[]
# print(out1)

#[((out.append(abs(y-x)) for y in no),out1.append(min(out)),out=[])for x in range(len(S))]


# from collections import Counter
# x='akhil'
# #print(Counter(x))

# licensePlate = "1s3 PSt"
# words = ["step", "steps", "stripe", "stepple"]
# #print(Counter(licensePlate))

# ops=["5","2","C","D","+"]
# out=[]
# for x in range(len(ops)):
# 	print(x)
# 	if ops[x]=='C':
# 		out.pop()
# 	elif ops[x]=='+':
# 		out.append(int(out[-1])+int(out[-2]))
# 	elif ops[x]=='D':
# 		out.append(int(out[-1])*2)
# 	else:
# 		out.append(int(ops[x]))
# 	print(out)

# print('496')
# s="I speak Goat Latin"
# for x in s.split(' '):
# 	if x[0].casefold()=='a' or x[0].casefold()=='e' or x[0].casefold()=='i' or x[0].casefold()=='o' or x[0].casefold()=='u':
# 		out.append(x+'ma')
# 	else:
# 		out.append(x[1:]+x[0]+'ma')

# print(out)


# l1=[{'a':'a1'},{'b':'b1'}]

# #for x in l1:
# 	#print(x)

# # for x in range(len(l1)):
# # 	a=l1[x]
# # 	print(a)
# # 	print(a.get(a.keys(),'hi'))

# for x in l1:
# 	print(x)
# 	a=x.keys()
# 	print(x.keys())


 
