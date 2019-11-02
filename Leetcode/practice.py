#List to tuple
# List to set

'''def convert(list): 
	#return tuple(list) 
	return set(list)
# Driver function 
list = [1, 2, 3, 4] 
print(convert(list)) 

#list to dict
def Convert(lst): 
	res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)} 
	return res_dct 
# Driver code 
lst = ['a', 1, 'b', 2, 'c', 3] 
for i in range(0, len(lst), 2):
	print (i)
print(Convert(lst)) 


# set to list 
my_set = {'Geeks', 'for', 'geeks'} 

s = list(my_set) 
print(s) '''

dict = {}
dict['Capital']="London"
dict['Food']="Fish&Chips"
dict['2012']="Olympics"

#lists
temp = []
dictList = []

for key, value in dict.items():
    temp = [key,value]
    dictList.append(temp)


print (dictList)
#for i in dictList:
 #  print (i)