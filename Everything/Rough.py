import pandas as pd
import numpy as np
#https://thispointer.com/data-analysis-in-python-using-pandas/


print("***")
df29=pd.read_csv('flights_data.csv')
print(df29.dtypes)

df29['concat1']= df29['updated_at']+'*'+df29['destination_full_name']
print(df29['concat1'].head(10))

# to change datatype
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.astype.html

print("to add new column to existing df")
#Method 1
data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Height': [5.1, 6.2, 5.1, 5.2], 
        'Qualification': ['Msc', 'MA', 'Msc', 'Msc']}  
df = pd.DataFrame(data) 
address = ['Delhi', 'Bangalore', 'Chennai', 'Patna'] 
df['Address'] = address 

#Method 2
data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Height': [5.1, 6.2, 5.1, 5.2], 
        'Qualification': ['Msc', 'MA', 'Msc', 'Msc']} 
df = pd.DataFrame(data) 
df.insert(2, "Age", [21, 23, 24, 21], True) 
print(df)

print("to delete one column")
del df['Age']
print(df)

print("*** drop column and row - write again")
#df13=df12.drop(columns=['Age'],index=['new'])
#print(df13)

print("select all or any columns")
#Method 1
print(df.Name)
#Method 2
print(df['Name'])
#Method 3
print(df.iloc[:4,2])

print("to chnage data type")
df.astype({'Height':'float'})
print(df.dtypes)

List11={'Name':['Tom', 'Jack', 'Steve','John','akhil','khan'],
'Age':[25,40,35,90,14,92]}
df11=pd.DataFrame(List11)
print(df11)

print("*** rename column names and row names - change df **")
df12=df11.rename(columns={'Name':'Fullname'},index={4:'new'})
print(df12)


print("to insert df")
df1 = pd.DataFrame([[1, 2], [3, 4]], columns=list('AB'))
print(df1)
df2 = pd.DataFrame([[5, 6], [7, 8]], columns=list('AB'))
df1.append(df2)

print(df2)

print("to insert rows - see")


List25={'Name':['Tom', 'Jack', 'Steve','John','akhil','khan'],
'Age':[25,40,35,90,14,92]}

print("filter data")

print("**filter with = ")
#method 1
df26=pd.DataFrame(List25)
df26a=df26[df26['Name']=='Tom']
print(df26a)

print("***")
#mwthod 2
df26=df26[df26.Name == 'Tom']
print(df26)


print("** filter with & ")
#method 1
df27=pd.DataFrame(List25)
df27=df27[(df27['Age']<50) & (df27['Age']>20)]
print(df27)

#method 2
df27=df27[(df27.Age<50) & (df27.Age>20)]
print(df27)

print("** IMP: filter with or")
#method 1
df28=pd.DataFrame(List25)
df28=df28[(df28['Name']=='Jack') | (df28['Name']=='akhil')]
print(df28)

#method 2
df28=df28[(df28.Name =='Jack') | (df28.Name=='akhil')]
print(df28)

print("** filter with < ")
df28=df27.query('Age<=40')
print(df28)



print(" ** filter with - see <= , >=, > , Like")




print("sort")
print("*** sort by values ***")
df15=df12.sort_values('Age')
print(df15)

print("*** sort by alphabet -- capital letters pahela and small letters pachi ***")
df16=df11.sort_values('Name')
print(df16)

print("***group by")
df18 = pd.DataFrame({'Animal': ['Falcon', 'Falcon','Parrot', 'Parrot'],'Max Speed': [380., 370., 24., 26.]})
print(df18)

print("*** group by - sum")
group=df18.groupby(['Animal']).sum()
print(group)

print("*** group by - mean")
group1=df18.groupby(['Animal']).mean() 
print(group1) 

list1=[[1,'some_value','some_value'],[2,'some_value','some_value'],[3,'some_value','some_value'],
[4,'some_value','some_value'],[5,'some_value','some_value']]

df= pd.DataFrame(list1,columns=['a','b','c'],index=['row1','row2','row3','row4','row5'])
print (df)

print("***look for and / or ")


print("***delete row based on condition")
indexNames = df[df['a'] ==3].index
df.drop(indexNames , inplace=True)
print(df)

print("***see - delete row based on location") 


print("*** delete all rows")
df.drop(df.index , inplace=True)
print(df)


print("***see-  to delete table")
df1 = {
    'Subject':['semester1','semester2','semester3','semester4','semester1',
               'semester2','semester3'],
   'Score':[62,47,55,74,31,77,85]}
df1 = pd.DataFrame(df1,columns=['Subject','Score'])
print(df1)

df2 = {
    'Subject':['semester1','semester2','semester3','semester4'],
   'Score':[90,47,85,74]}
df2 = pd.DataFrame(df2,columns=['Subject','Score'])
print(df2)

print("***Union all")
df_union_all= pd.concat([df1, df2])
print(df_union_all)

print("***Union")
df_union= pd.concat([df1, df2]).drop_duplicates()
print(df_union)

print("***")
print(df1)
print(df2)

print("*** intersect")
s1 = pd.merge(df1, df2, how='inner', on=['Score'])
print(s1)

print("*** If/case ")
# 1 condition

list1=[[1,'some_value','some_value'],[2,'some_value','some_value'],[3,'some_value','some_value'],
[4,'some_value','some_value'],[5,'some_value','some_value']]

df= pd.DataFrame(list1,columns=['a','b','c'],index=['row1','row2','row3','row4','row5'])

print("*** update with if ")
# meaning: if column a=2 , columb b and c == 'aaaa'
df.loc[df['a'] == 2, ['b','c']] = 'aaaa'
print(df)


print("*** update with if...else")
df['c'] = np.where(df['a'] == 2, 10,20)
print(df)

print("*** update with if...else")
#df['new column name'] = df['column name'].apply(lambda x: 'value if condition is met' if x condition else 'value if condition is not met')

# see - multiple conidition



print("*** IN ")
isin=df[df.a.isin([2,3])]
print(isin)

print("*** see - not in ")


print(" *** between")
between=df[(df.a<4) & (df.a> 2)] 
print(between) 

print(" *** Group by - having")


print("***see -trim")
trim=df.b.str.strip()
print(trim)

#Method 2 see
#df[df.columns] = df.apply(lambda x: x.str.strip())

print("***see - LTRIM")
LTRIM=df.b.str.strip()
print(LTRIM)

print("***see - RTRIM")
RTRIM=df.b.str.strip()
print(RTRIM)


print("*** Left")
Left=df.b.str[:3]
print(Left)

print("*** Right")
Right=df.b.str[-4:-1]
print(Right)

print("*** upper case")


print("*** lower case")

