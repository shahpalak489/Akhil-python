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
#df15=df12.sort_values('Age')
#print(df15)

print("*** sort by alphabet -- capital letters pahela and small letters pachi ***")
#df16=df11.sort_values('Name')
#print(df16)

print("***group by")
#df18 = pd.DataFrame({'Animal': ['Falcon', 'Falcon','Parrot', 'Parrot'],'Max Speed': [380., 370., 24., 26.]})
#print(df18)

print("*** group by - sum")
#group=df18.groupby(['Animal']).sum()
#print(group)

print("*** group by - mean")
#group1=df18.groupby(['Animal']).mean() 
#print(group1) 

print(" *** Group by - having")
'''
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
'''

print("*** sub string")
#substring=df1.Subject.str[:3]
#print(substring)

print("***Union all")
#df_union_all= pd.concat([df1, df2])
#print(df_union_all)

print("***Union")
#df_union= pd.concat([df1, df2]).drop_duplicates()
#print(df_union)

print("***")
print(df1)
print(df2)

print("*** intersect")
#s1 = pd.merge(df1, df2, how='inner', on=['Score'])
#print(s1)
