import pandas as pd
import numpy as np

# to display whole dataframe in console 
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 227)

# to create dataframe from CSV file
df1=pd.read_csv('flights_data_dataframe.csv')
print(df1)

print("filter data")
print("**filter with = ")
#method 1
Equalto=df1[df1.flt_num==3314]
print(Equalto)

print("***")
#mwthod 2
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
isin=df1[df1.scheduled_origin_gate.isin(['B22','B25',2,'Any'])]
print(isin.loc[:,['id','scheduled_origin_gate','created_at','updated_at','flight_identifier','flt_num']])

print("***IMP - not in ")
#https://stackoverflow.com/questions/19960077/how-to-filter-pandas-dataframe-using-in-and-not-in-like-in-sql
isnotin=df1[~df1.scheduled_origin_gate.isin(['B22','B25',2,'Any'])]
print(isnotin.loc[:,['id','scheduled_origin_gate','created_at','updated_at','flight_identifier','flt_num']])


print("*** is null")
ISnull=df1.isna()
print(ISnull)

print("*** is not null")
ISnotnull=df1.notna()
print(ISnotnull)

print(" *** between")
#between=df[(df.a<4) & (df.a> 2)] 
#print(between) 

print("*** Left")
Left=df1.created_at.str[:4]
print(Left.iloc[:10])

print("*** Right")
Right=df1.origin_full_name.str[-4:-1]
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
print(Upper_case.iloc[:10])

print("*** lower case")
Lower_case=df1.origin.str.lower()
print(Lower_case.iloc[:10])


print("*** see - replace")


print("*** If/case ")
print("*** update with if...than ")
df1.loc[df1.Price > 201,['Price_level']] = 'costly'
print(df1.iloc[:5,-4:])

print("*** update with if...than...else")
df1.Price_level = np.where(df1.Price > 201,'costly','cheaper')
print(df1.iloc[:5,-4:])

#method 2
#df['new column name'] = df['column name'].apply(lambda x: 'value if condition is met' if x condition else 'value if condition is not met')

print("see - if ...multiple conidition")
#https://stackoverflow.com/questions/48569166/multiple-if-else-conditions-in-pandas-dataframe-and-derive-multiple-columns/48569899

print("sort")
print("*** sort by values ***")
sort_values=df1.sort_values('Price')
print(sort_values.loc[:,['destination_full_name','origin_full_name','Price']])

print("*** sort by alphabet -- capital letters pahela and small letters pachi ***")
sort_alphabet=df1.sort_values('destination_full_name')
print(sort_alphabet.loc[:,['destination_full_name','origin_full_name','Price']])

print("***group by")
print("*** group by - sum")
groupby_sum=df1.groupby(['Price']).sum()
print(groupby_sum)

print("*** group by - mean")
groupby_mean=df1.groupby(['Price']).mean()
print(groupby_mean)

print("***see- Group by - having")

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

print("*** df2")
df2=pd.read_csv('flights_data_dataframe2.csv')
print(df2)

print("***Union all")
Union_all=pd.concat([df1,df2]) 
print(Union_all)

print("*** Union")
Union=pd.concat([df1,df2]).drop_duplicates()
print(Union)

print("*** intersect")
#intersect= pd.merge(df1, df2, how='inner', on=['Score'])
#print(intersect)

print("*** see - merge **")
print("*** Inner Join ***")
inner_join=pd.merge(df1,df2,left_on='Coreid',right_on='Coreid_2',how='inner')
print(inner_join.loc[:,['Coreid','Coreid_2']])

print("*** Outer Join ***")
Outer_join=pd.merge(df1,df2,left_on='Coreid',right_on='Coreid_2',how='outer')
print(Outer_join.loc[:,['Coreid','Coreid_2']])

print("*** Left Join")
Left_join=pd.merge(df1,df2,left_on='Coreid',right_on='Coreid_2',how='left')
print(Left_join.loc[:,['Coreid','Coreid_2']])

print("*** Right Join")
Right_join=pd.merge(df1,df2,left_on='Coreid',right_on='Coreid_2',how='right')
print(Right_join.loc[:,['Coreid','Coreid_2']])


print("*** concatenation between 2 columns")
df1['flight_fulldetail']=df1['origin_full_name'] + ' TO ' + df1['destination_full_name']
print(df1.loc[:,['origin_full_name','destination_full_name','flight_fulldetail']])

print("*** IMP: to get second column")
#https://www.shanelynn.ie/select-pandas-dataframe-rows-and-columns-using-iloc-loc-and-ix/
#List25={'Name':['Tom', 'Jack', 'Steve','John','akhil','khan'],
#'Age':[25,40,35,90,14,92]}
#df25=pd.DataFrame(List25)
#print(df25.iloc[:,1])
print("*** to get second row")
#print(df25.iloc[1])

print("*** IMP: to get by column names")
#use loc ... 

print("*** calculation between 2 columns")
#df10["ab"] = 25
df1['Plus']=df1['Price']+df1['Points']
df1['Minus']=df1['Price']-df1['Points']
df1['Muliply']=df1['Price']*df1['Points']
df1['Divide']=df1['Price']/df1['Points']
print(df1.loc[:,['Price','Points','Plus','Minus','Muliply','Divide']])

print("***see - look for and / or ")

print("***delete row based on condition")
deleterow=df1[df1.Coreid==25].index
df1.drop(deleterow, inplace=True)
print(df1.iloc[:,-7:-1])

print("***see - delete row based on location") 

print("*** delete all rows")
#df.drop(df.index , inplace=True)
#print(df)


print("***see-  to delete table")
#df1 = {'Subject':['Math','Physics','Biology','Chemistry','Language','Social science','computer'],'Score':[62,47,55,74,31,77,85]}
#df1 = pd.DataFrame(df1,columns=['Subject','Score'])

#df11=pd.DataFrame(List11)
#print(df11)

print("***")
#print(df12)

print("*** keep column as index column ***")
#df14=df12.set_index('Age')
#print(df14)

print("***")
#df29=pd.read_csv('flights_data.csv')
#print(df29.dtypes)

#df29['concat1']= df29['updated_at']+'*'+df29['destination_full_name']
#print(df29['concat1'].head(10))