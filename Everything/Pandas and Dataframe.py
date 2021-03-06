'''
question: how to get few colums of df 

trick to remember 
------------------
filter column with == , & , | --->  for column --->  df[df.column_name == ]
filter column with multiple values --->  for column --->  df[df.column_name.isin( ) ]
is null for column  ---> for column --->  df[df.column_name.isna( ) ]
not null for column ---> for column --->  df[df.column_name.notna( ) ]
-------------
is null for all columns ---> for dataframe ---> df.isna( )
not null for all colums ---> for dataframe ---> df.notna( )
sorting for all colums ---> for dataframe ---> df.sort_values( )
group by ---> for dataframe ---> df.groupby( column_name ).sum( )/ mean( )
count ---> for dataframe ---> df.count( )
first 2 df rows ---> for dataframe ---> df.head( number of rows )
last 2 df rows ---> for dataframe ---> df.tail ( number of rows)
set index for df ---> for dataframe --->  df.set_index( column name)
----------
left ---> df.column_name.str[ ]
right ---> df.column_name.str[ ]
lower ---> df.column_name.lower( )
upper ---> df.column_name.upper( )
------------------
update with if...than
df.loc[df.column_name > 201,[' column_name]] = value

update with if...than...else
df.column_name=np.where( df.column_name > 201, value1 , value2 )
---------------------
Union all 2 df ---> pd.concat( df , df )
Union 2 df ---> pd.concat( df , df ).drop_duplicates( )
Joins ---> pd.merge( df , df , left_on=column , right_on = column, how = )
----------
delete row ---> df.drop( df [ df.column == ].index , inplace=True )
delete all rows ---> df.drop( df.index , inplace=True )
------------
concat between 2 colums ---> df[ column ] = df[ column ] + 'to' + df[ column ]
calculation between 2 colums ---> df [ column ] = df [ column ] + df [ column ]
'''
import pandas as pd
import numpy as np

print('***to display whole dataframe in console')
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 227)

print('***to create dataframe from CSV file')
df1=pd.read_csv('Testdata1.csv')
print(df1)

print("*** select any particular column or all columns")
#Method 1
print(df1.origin)
#Method 2
print(df1['origin'])
#Method 3
print(df1.iloc[:4,2])

print("***filter data")
print("*filter with = ")
#method 1

#MMIMP =select * from df1[where df1.flt_num==3314]
Equalto=df1[df1.flt_num==3314]            #here first df1 means what you want to display after filter
print(Equalto)

#      =select flight_identifier,Points from df1[where df1[flt_num]==3314]
Equalto=df1.flight_identifier,df1.Points[df1.flt_num==3314]
print(Equalto)

print("***")
#method 2
Equalto=df1[df1['flt_num']==3314]
print(Equalto)

print("***filter with & ")
print("method 1")
filter_and=df1[(df1.origin=='ATL') & (df1.Price==201.2)]
print(filter_and)

print("method 2")
filter_and=df1[(df1['origin']=='ATL') & (df1['Price']==201.2)]
print(filter_and.iloc[:,1])

print("***IMP: filter with or")
#method 1
filter_or=df1[(df1.destination == 'ATL')|(df1.destination == 'FLL')]
print(filter_or)

#method2
filter_or=df1[(df1['destination'] == 'ATL')|(df1['destination'] == 'FLL')]
print(filter_or)

print("*** filter with <,>,<=,>= ")
filter_lessthan=df1[(df1.Price >= 100) & (df1.Price < 400)]
print(filter_lessthan.iloc[:,-4:-1])

print("*** see -filter with  Like")
# https://www.tutorialspoint.com/python/string_startswith.htm
# https://www.tutorialspoint.com/python/string_endswith.htm

print("*** IN ")
isin=df1[df1.Points.isin([0,11,55])]
print(isin.loc[:,['id','scheduled_origin_gate','created_at','updated_at','flight_identifier','flt_num']])

print("***IMP - not in ")
#https://stackoverflow.com/questions/19960077/how-to-filter-pandas-dataframe-using-in-and-not-in-like-in-sql
isnotin=df1[~df1.Points.isin([0,11,55])]
print(isnotin.loc[:,['id','scheduled_origin_gate','created_at','updated_at','flight_identifier','flt_num']])

print("*** is null for whole dataframe")
ISnull=df1.isna()
print(ISnull)

print("*** is null for column")
ISnull=df1[df1.origin.isna()]
print(ISnull)

print("*** is not null for whole DataFrame")
ISnotnull=df1.notna()
print(ISnotnull)

print("*** is not null for column")
ISnotnull=df1[df1.origin.notna()]
print(ISnotnull)

print(" *** between")
#between=df[(df.a<4) & (df.a> 2)] 
#print(between) 

print("*** Left ")
Left=df1.created_at.str[:9]
print(Left)
print(Left.iloc[:10])

print("*** Right")
Right=df1.created_at.str[-4:-1]
print(Right.iloc[:10])

print("***see -trim")
#trim=df1.flight_identifier.str.strip()
#print(trim)

#Method 2 see
#df[df.columns] = df.apply(lambda x: x.str.strip())

print("***see - LTRIM")
#LTRIM=df.b.str.strip()
#print(LTRIM)

print("***see - RTRIM")
#RTRIM=df.b.str.strip()
#print(RTRIM)

print("*** upper case")
Upper_case=df1.scheduled_destination_gate.str.upper()
print(Upper_case)
print(Upper_case.iloc[:10])

print("*** lower case")
Lower_case=df1.origin.str.lower()
print(Lower_case)
print(Lower_case.iloc[:10])

print("*** see - replace")

print("*** see - reverse(not imp)")

print("*** If/case ")
print("* update with if...than ")
# if df1.price > 201 than 'price_level'= 'costly'
df1.loc[df1.Price > 201,['Price_level']] = 'costly'
print(df1.iloc[:5,-4:])

print("* update with if...than...else")
# if df1.price > 201 then price_level= costly else price_level= cheaper
df1.Price_level = np.where(df1.Price > 201,'costly','cheaper')
print(df1.iloc[:5,-4:])

# method 2
# df['new column name'] = df['column name'].apply(lambda x: 'value if condition is met' if x condition else 'value if condition is not met')

print("see - if ...multiple conidition")
#https://stackoverflow.com/questions/48569166/multiple-if-else-conditions-in-pandas-dataframe-and-derive-multiple-columns/48569899

print("***sort")
print("* sort for values")
sort_values=df1.sort_values('Price')
print(sort_values.loc[:,['destination_full_name','origin_full_name','Price']])

print("* sort for alphabet -- capital letters pahela and small letters pachi ***")
sort_alphabet=df1.sort_values('destination_full_name')
print(sort_alphabet.loc[:,['destination_full_name','origin_full_name','Price']])

print("***see - group by")
print("* group by - sum")
groupby_sum=df1.groupby(['Price']).sum()
print(groupby_sum)

print("* group by - mean")
groupby_mean=df1.groupby(['Price']).mean()
print(groupby_mean)

print("***see  Group by - having")

print("*** sub string")
substring=df1.destination_full_name.str[-5:]
print(substring)

print("*** count")
count=df1.count()
print(count)

print("*** get first 2 rows **")
head=df1.head(2)
print(head)

print("*** get last 2 rows**")
tail=df1.tail(2)
print(tail)

print("*** keep column as index column ***")
index_column=df1.set_index('Coreid')
print(index_column)

print("*** df2")
df2=pd.read_csv('Testdata2.csv')
print(df2)

print("***Union all between 2 dataframes")
Union_all=pd.concat([df1,df2]) 
print(Union_all)

print("*** Union between 2 dataframes")
Union=pd.concat([df1,df2]).drop_duplicates()
print(Union)

print("*** intersect")
#intersect= pd.merge(df1, df2, how='inner', on=['Score'])
#print(intersect)

print("*** merge")
print("* Inner Join")
inner_join=pd.merge(df1,df2,left_on='Coreid',right_on='Coreid_2',how='inner')
print(inner_join.loc[:,['Coreid','Coreid_2']])

print("* Outer Join ")
Outer_join=pd.merge(df1,df2,left_on='Coreid',right_on='Coreid_2',how='outer')
print(Outer_join.loc[:,['Coreid','Coreid_2']])

print("* Left Join")
Left_join=pd.merge(df1,df2,left_on='Coreid',right_on='Coreid_2',how='left')
print(Left_join.loc[:,['Coreid','Coreid_2']])

print("* Right Join")
Right_join=pd.merge(df1,df2,left_on='Coreid',right_on='Coreid_2',how='right')
print(Right_join.loc[:,['Coreid','Coreid_2']])

print("*** concatenation between 2 columns")
# below will add new column to df as well
df1['flight_fulldetail']=df1['origin_full_name'] + ' TO ' + df1['destination_full_name']
print(df1.loc[:,['origin_full_name','destination_full_name','flight_fulldetail']])

print("*** IMP: to get second column")
print(df1.iloc[:,1])

print("*** to get second row")
print(df1.iloc[1])

print("*** IMP: to get by column names")
#use loc ... 

print("*** calculation between 2 columns")
#belwo will add new column each time
df1['Plus']=df1['Price']+df1['Points']
df1['Minus']=df1['Price']-df1['Points']
df1['Muliply']=df1['Price']*df1['Points']
df1['Divide']=df1['Price']/df1['Points']
print(df1.loc[:,['Price','Points','Plus','Minus','Muliply','Divide']])

print("***see - look for and / or ")

print("*** delete all rows")
df1.drop(df1.index , inplace=True)
print(df1)

print("***delete row based on condition")
# remember syntax
df1.drop(df1[df1.Coreid==15].index, inplace=True)
print(df1.iloc[:,-7:-1])

print("***see - delete row based on location") 

print("***see- to delete table")
#del df2
#print(df2)

print("*** to know dataframe datatype")
print(df2.dtypes)

print("*** to create DataFrame")

print("* to create empty DataFrame ")
df = pd.DataFrame()
print(df)

print("* to cretae DataFrame from list : 1column without column name")
List1=[34,63,85,14,96]
df1=pd.DataFrame(List1)
print(df1)

print("* to create DataFrame from list : 2columns without column name ")
List2=[['alex',10],['bob',20],['mike',30]]
df2=pd.DataFrame(List2)
print(df2)

print("* create dataframe with data type,row names,columns names")
List3=[['shah',25],['patel',28],['kumar',11]]
df3=pd.DataFrame(List3,dtype=float,
  index=['city1','city2','city3'],
  columns=['last_name','birth_day'])
print(df3)

print("* to create DataFrame from dictionry ")
dict4 = {'Name':['Tom'],'Age':[28]}
df4=pd.DataFrame(dict4)
print(df4) 

dict5= {"city":["baroda","bangalore"],
    "state":["GJ","KA"]}
df=pd.DataFrame(dict5)
print(df)

print("* create dataframe for List of Dics ")
List7=[{'a':1,'b':2},{'a':5,'b':10,'c':2}]
df7=pd.DataFrame(List7)
print(df7)

print("* Not IMP: create dataframe for Series of Dics")
List8={'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df8=pd.DataFrame(List8)
print(df8)

print("* NOT IMP : create 2 colums dataframe from 4 columns data ")
List9 = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20, 'd': 0}]
df9 = pd.DataFrame(List9, index=['first', 'second'], columns=['a', 'b'])
print(df9)

# to change datatype
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.astype.html

print("*** to add new column to existing df ")
data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Height': [5.1, 6.2, 5.1, 5.2], 
        'Qualification': ['Msc', 'MA', 'Msc', 'Msc']} 
df = pd.DataFrame(data) 

#Method 1
df.insert(2, "Age", [21, 23, 24, 21], True) 
print(df)

print("*****")
#Method 2
df['Address'] = ['Delhi', 'Bangalore', 'Chennai', 'Patna']
print(df)

print("*** to delete one column from df")
del df['Age']
print(df)

print("*** see - drop column and row")
#df13=df12.drop(columns=['Age'],index=['new'])
#print(df13)

print("*** to change data type")
df.astype({'Height':'float'})
print(df.dtypes)  

List11={'Name':['Tom', 'Jack', 'Steve','John','akhil','khan'],
'Age':[25,40,35,90,14,92]}
df11=pd.DataFrame(List11)
print(df11)

print("*** rename column names and row names ")
df12=df11.rename(columns={'Name':'Fullname'},index={4:'new'})
print(df12)

print("*** to insert df")
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

print("*** iloc,loc and ix")

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

print("2---- ")
print(df2.iloc[2,1]) # row-2 :col-1 

print("3---- ")
print(df2.iloc[:2,:1]) # row - 0,1 :col- 0

print("4---- ")
print(df2.loc[2,"city"]) # row - 2 :col- city

print("5---- IMP")
print(df2.loc[:2,"city"]) # row - 0,1,2 :col- city

print("6---- not possible ")
#print(df2.loc[2,1]) # row-2 :col-1 

print("7---- ")
print(df2.ix[2,"city"]) # row - 2 :col- city

print("8---- IMP")
print(df2.ix[:2,"city"]) # row - 0,1,2 :col- city

print("9----")
print(df2.ix[2,1]) # row-2 :col-1

print("10---")
print(df2.ix[:2,:1]) # row - 0,1,2 :col- 0  

'''
pivot_table
df.pivot
melt
stack
unstack

columns
rename
drop

what is inplace true/false

fillna/dropna( thresh=4)
head and tail in dataframe


set_index
group by
multiltvel dataframe --> drop level

ternary oprator using if else in one line

take datatype date , decimal for the input
1)
dataframe ma 1 column ni value parthi biji column ni column ni val nakki karo

name    surname gender  applicable
palak   shah    female   no
akhil   shah     male    no
shivani shah    female   no

gender = female --> status-applicaple = yes

2) 
input
name    surname gender  applicable
palak   shah    female    no
akhil   shah1     male    no
shivani shah2    female   no

output
name    surname gender  applicable
palak           female   no
akhil   shah     male    no
shivani shah1    female   no

shift column value to 1 step down

3)
input
name    surname gender  applicable  date
palak   shah    female    no        19-12-26
akhil   shah1     male    no        19-12-27
shivani shah2    female   no        19-12-28
shivani1 shah3    female   no       19-12-29
shivani2 shah4    female   no       19-12-30


output
name    surname gender  applicable  date
shivani2 shah4    female   no      19-12-30

get the last row from the dataframe


4)
name    surname gender  applicable full_name
palak   shah    female    no       palak shah
akhil   shah1     male    no       akhil shah1
shivani shah2    female   no       shivani shah2

get the last column as a combination of first 2 columns

5)

name  a   b    c  d  sum
palak 1   2   3   4  10

get sum column from sum of all the rows

6)
name    a   b   c   d
palak   5  7   nan
palak1  5  8   0
palak2  5  9
palak3  5   5
sum     20 50  0   0

get the sum row from sum of all the columns

'''