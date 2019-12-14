import pandas as pd
#pandas.DataFrame(data, index, columns, dtype, copy)
# first use [] and if you hve other kind of values than use {}
print("***empty DataFrame***")
df = pd.DataFrame()
print(df)

print("***DataFrame from list- 1column without column name**")
List1=[34,63,85,14,96]
df1=pd.DataFrame(List1)
print(df1)

print("***DataFrame from list- 2columns without column name*")
List2=[['alex',10],['bob',20],['mike',30]]
df2=pd.DataFrame(List2)
print(df2)

print("***give data type,row names,columns names***")
List3=[['shah',25],['patel',28],['kumar',11]]
df3=pd.DataFrame(List3,dtype=float,
	index=['city1','city2','city3'],
	columns=['last_name','birth_day'])
print(df3)

print("*** DataFrame from dictionry ***")
List4 = {'Name':['Tom'],'Age':[28]}
df4=pd.DataFrame(List4)
print(df4) 

print("**To create 1 column with column name**")
lst= {"city":["baroda","bangalore"],
		"state":["GJ","KA"]}
df=pd.DataFrame(lst)
print(df)

print("***")
List5={'Name':['Tom', 'Jack', 'Steve'],'Age':[28,34,29]}
df5=pd.DataFrame(List5)
print(df5)

print("***Not IMP**List of Dics***")
List7=[{'a':1,'b':2},{'a':5,'b':10,'c':2}]
df7=pd.DataFrame(List7)
print(df7)

print("***give row names***")
List6={'City':['baroda','delhi','surat'],'state':['GJ','DEL','GJ']}
df6=pd.DataFrame(List6,index=['city1','city2','city3'])
print(df6)

print("***Series of Dics***")
List8={'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df8=pd.DataFrame(List8)
print(df8)

print("***2 coulms dataframe from 4 columns data***")
List9 = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20, 'd': 0}]
df9 = pd.DataFrame(List9, index=['first', 'second'], columns=['a', 'b'])
print(df9)

print("iloc,loc and ix")
lst={"city":["baroda","surat"],
		"zip":["06","05"]}
df=pd.DataFrame(lst)
print(df)
print("Rule 1 : iloc = i am loc = based on location = perfection")
print("Rule 2: when we use loc its mandotory to mention column name")
#Rule 3 : 

print("1-----")
lst2= {"city":["baroda","bangalore","surat","mangalore"],
		"state":["GJ","KA","GJ","KA"]}
df2=pd.DataFrame(lst2)
print(df2)

print("2 not possible ")
#print(df2.loc[2,1]) # row-2 :col-1   

print("3-----")
print(df2.iloc[2,1]) # row-2 :col-1 

print("4------")
print(df2.ix[2,1]) # row-2 :col-1 

print("5------")
print(df2.loc[2,"city"]) # row - 2 :col- city

print("6-----")
print(df2.ix[2,"city"]) # row - 2 :col- city

print("7--IMP")
print(df2.loc[:2,"city"]) # row - 0,1,2 :col- city

print("8--IMP")
print(df2.ix[:2,"city"]) # row - 0,1,2 :col- city

print("9--IMP")
print(df2.iloc[:2,:1]) # row - 0,1 :col- 0 

print("10--IMP  (see)")
print(df2.ix[:2,:1]) # row - 0,1,2 :col- 0  

print("*****")
List10 = {'a':[15,50], 'b':[22,40] }
df10 = pd.DataFrame(List10, index=['first', 'second'])
print(df10)

print("*** calculation between 2 columns")
# df2["k"] = np.where(df2['a']==1, 'palak', 'red')
df10["ab"] = 25
df10["abc"] = df10["a"] + df10["ab"] 
df10["abcd"] = df10["a"] - df10["ab"] 
df10["Multi"] = df10["a"] * df10["abcd"]
df10["sub"]=df10["abc"]/df10["abcd"]
print(df10)

List11={'Name':['Tom', 'Jack', 'Steve','John','akhil','khan'],
'Age':[25,40,35,90,14,92]}
df11=pd.DataFrame(List11)
print(df11)

print("*** operations**")
print("*** get first 2 rows **")
head=df11.head(2)
print(head)

print("*** get last 2 rows**")
tail=df11.tail(2)
print(tail) 


print("***")
print(df12)

print("*** keep column as index column ***")
df14=df12.set_index('Age')
print(df14)

print("***")
print(df12)


List17={'First_Name':['Tom', 'Jack', 'Steve','akhil'],
'Last_Name':['Walter','Shavella','Jha','Shah']}
df17=pd.DataFrame(List17)

print("*** concatenation 2 columns")
df17['Full_Name']=df17['First_Name']+' ' + df17['Last_Name']
print(df17)



print("*** merge **")
'''DataFrame.merge(self, right, how='inner', on=None, left_on=None, 
right_on=None, left_index=False, right_index=False, sort=False, 
suffixes=('_x', '_y'), copy=True, indicator=False, validate=None)'''
df19 = pd.DataFrame({'lkey': ['foo', 'bar', 'baz', 'koo'],
	'value': [1, 2, 3,4]})
print(df19)
df20 = pd.DataFrame({'rkey': ['foo', 'bar', 'baz', 'foo'],
	 'value': [3,4,5, 6]})
print(df20)

print("*** Inner Join ***")
df21=pd.merge(df19,df20,on='value',how='inner')
print(df21)

print("*** Outer Join ***")
df22=pd.merge(df19,df20,on='value',how='outer')
print(df22)

print("*** Left Join")
df23=pd.merge(df19,df20,on='value',how='left')
print(df23)

print("*** Right Join")
df24=pd.merge(df19,df20,on='value',how='right')
print(df24)

print("*** to get particular columns")
List25={'Name':['Tom', 'Jack', 'Steve','John','akhil','khan'],
'Age':[25,40,35,90,14,92]}
df25=pd.DataFrame(List25)
df25=df25[['Name']]
print(df25)
 




