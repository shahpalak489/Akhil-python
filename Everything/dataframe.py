import pandas as pd
import numpy as np
#https://thispointer.com/data-analysis-in-python-using-pandas/
#pandas.DataFrame(data, index, columns, dtype, copy)
# first use [] and if you hve other kind of values than use {}

print("*** to create DataFrame")

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

print("*****")
List10 = {'a':[15,50], 'b':[22,40] }
df10 = pd.DataFrame(List10, index=['first', 'second'])
print(df10)

# to change datatype
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.astype.html

print("**** to add new column to existing df")
data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Height': [5.1, 6.2, 5.1, 5.2], 
        'Qualification': ['Msc', 'MA', 'Msc', 'Msc']} 
df = pd.DataFrame(data) 

#Method 1
df.insert(2, "Age", [21, 23, 24, 21], True) 
print(df)

print("*****")
#Method 2
address = ['Delhi', 'Bangalore', 'Chennai', 'Patna'] 
df['Address'] = address 
print(df)

print("**** to delete one column")
del df['Age']
print(df)

print("*** see - drop column and row")
#df13=df12.drop(columns=['Age'],index=['new'])
#print(df13)

print("select any particular column or all columns")
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

print("***to insert df")
df1 = pd.DataFrame([[1, 2], [3, 4]], columns=list('AB'))
print(df1)
df2 = pd.DataFrame([[5, 6], [7, 8]], columns=list('AB'))
df1.append(df2)

print(df2)

print("***")
students = [ ('jack', 34, 'Sydeny' , 'Australia') ,
             ('Riti', 30, 'Delhi' , 'India' ) ,
             ('Vikas', 31, 'Mumbai' , 'India' ) ,
             ('Neelu', 32, 'Bangalore' , 'India' ) ,
             ('John', 16, 'New York' , 'US') ,
             ('Mike', 17, 'las vegas' , 'US')  ]
dfObj = pd.DataFrame(students, columns = ['Name' , 'Age', 'City' , 'Country'], index=['a', 'b', 'c' , 'd' , 'e' , 'f'])

print("*** to insert rows with all columns values at the end")
listOfSeries = [pd.Series(['Raju', 21, 'Bangalore', 'India'], index=dfObj.columns ) ,
                pd.Series(['Sam', 22, 'Tokyo', 'Japan'], index=dfObj.columns ) ,
                pd.Series(['Rocky', 23, 'Las Vegas', 'US'], index=dfObj.columns ) ]
modDfObj = dfObj.append(listOfSeries , ignore_index=True)
print(modDfObj)

print("*** to insert rows with few columns values at the end")
modDfObj = dfObj.append({'Name' : 'Sahil' , 'Age' : 22} , ignore_index=True)
print(modDfObj)

print("*** to insert row at particular location")
new_row = pd.DataFrame({'Name':'akhil','Age':32},index =[0]) 
modDfObj = pd.concat([new_row, modDfObj]).reset_index(drop = True) 
print(modDfObj)

List25={'Name':['Tom','Jack','Steve','John','akhil','khan'],
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

print("***filter with & ")
#method 1
df27=pd.DataFrame(List25)
df27=df27[(df27['Age']<50) & (df27['Age']>20)]
print(df27)

#method 2
df27=df27[(df27.Age<50) & (df27.Age>20)]
print(df27)

print("***IMP: filter with or")
#method 1
df28=pd.DataFrame(List25)
df28=df28[(df28['Name']=='Jack') | (df28['Name']=='akhil')]
print(df28)

#method 2
df28=df28[(df28.Name =='Jack') | (df28.Name=='akhil')]
print(df28)

print("***filter with < ")
df28=df27.query('Age<=40')
print(df28)

print("***see -filter with -<= , >=, > , Like")

list1=[[1,'some_value','some_value'],[2,'some_value','some_value'],[3,'some_value','some_value'],
[4,'some_value','some_value'],[5,'some_value','some_value']]

df= pd.DataFrame(list1,columns=['a','b','c'],index=['row1','row2','row3','row4','row5'])

print("*** IN ")
isin=df[df.a.isin([2,3])]
print(isin)

print("*** IMP - not in ") # use ~
#https://stackoverflow.com/questions/19960077/how-to-filter-pandas-dataframe-using-in-and-not-in-like-in-sql

print("*** is null")
ISnull=df1.isna()
print(ISnull)

print("*** is not null")
ISnotnull=df1.notna()
print(ISnotnull)

print(" *** between")
between=df[(df.a<4) & (df.a> 2)] 
print(between) 

print("*** Left")
Left=df.b.str[:3]
print(Left)

print("*** Right")
Right=df.b.str[-4:-1]
print(Right)

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

print("*** upper case")
Upper_case=df.b.str.upper()
print(Upper_case)

print("*** lower case")
Lower_case=df.b.str.lower()
print(Lower_case)

print("*** If/case ")
# 1 condition

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
def flag_df(df):

    if (df['trigger1'] <= df['score'] < df['trigger2']) and (df['height'] < 8):
        return 'Red'
    elif (df['trigger2'] <= df['score'] < df['trigger3']) and (df['height'] < 8):
        return 'Yellow'
    elif (df['trigger3'] <= df['score']) and (df['height'] < 8):
        return 'Orange'
    elif (df['height'] > 8):
        return np.nan

df2['Flag'] = df2.apply(flag_df, axis = 1)


print("*** see - replace")


print("*** see - reverse(not imp)")


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

print(" *** Group by - having")


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

print("*** sub string")
substring=df1.Subject.str[:3]
print(substring)

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
df21=pd.merge(df19,df20,left_on='value',right_on='value',how='inner')
print(df21)

print("*** Outer Join ***")
df22=pd.merge(df19,df20,left_on='value',right_on='value',how='outer')
print(df22)

print("*** Left Join")
df23=pd.merge(df19,df20,left_on='value',right_on='value',how='left')
print(df23)

print("*** Right Join")
df24=pd.merge(df19,df20,left_on='value',right_on='value',how='right')
print(df24)

print("*** count")
count=df1.count()
print(count)

print("*** get first 2 rows **")
head=df11.head(2)
print(head)

print("*** get last 2 rows**")
tail=df11.tail(2)
print(tail) 


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

List17={'First_Name':['Tom', 'Jack', 'Steve','akhil'],
'Last_Name':['Walter','Shavella','Jha','Shah']}
df17=pd.DataFrame(List17)

print("*** concatenation 2 columns")
df17['Full_Name']=df17['First_Name']+' ' + df17['Last_Name']
print(df17)

print("*** IMP: to get second column")
#https://www.shanelynn.ie/select-pandas-dataframe-rows-and-columns-using-iloc-loc-and-ix/
List25={'Name':['Tom', 'Jack', 'Steve','John','akhil','khan'],
'Age':[25,40,35,90,14,92]}
df25=pd.DataFrame(List25)
print(df25.iloc[:,1])
print("*** to get second row")
print(df25.iloc[1])

print("*** IMP: to get by column names")
#use loc ... 


print("*** calculation between 2 columns")
# df2["k"] = np.where(df2['a']==1, 'palak', 'red')
df10["ab"] = 25
df10["abc"] = df10["a"] + df10["ab"] 
df10["abcd"] = df10["a"] - df10["ab"] 
df10["Multi"] = df10["a"] * df10["abcd"]
df10["sub"]=df10["abc"]/df10["abcd"]
print(df10)


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
    'Subject':['Math','Physics','Biology','Chemistry','Language',
               'Social science','computer'],
   'Score':[62,47,55,74,31,77,85]}
df1 = pd.DataFrame(df1,columns=['Subject','Score'])

df11=pd.DataFrame(List11)
print(df11)

print("***")
print(df12)

print("*** keep column as index column ***")
df14=df12.set_index('Age')
print(df14)

print("***")
df29=pd.read_csv('flights_data.csv')
print(df29.dtypes)

df29['concat1']= df29['updated_at']+'*'+df29['destination_full_name']
print(df29['concat1'].head(10))