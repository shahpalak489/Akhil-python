import pandas as pd

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


print("*** rename column names and row names - change df **")
#df12=df11.rename(columns={'Name':'Fullname'},index={4:'new'})
#print(df12)


print("to insert df")
df1 = pd.DataFrame([[1, 2], [3, 4]], columns=list('AB'))
print(df1)
df2 = pd.DataFrame([[5, 6], [7, 8]], columns=list('AB'))
df1.append(df2)

print(df2)

print("to insert rows - see")



print("filter data")

print("**filter with = ")
df26=pd.DataFrame(List25)
df26a=df26[df26['Name']=='Tom']
print(df26a)

# try to use other df thans df27
print("** filter with & ")
df27=pd.DataFrame(List25)
df27=df27[(df27['Age']<50) & (df27['Age']>20)]
print(df27)

print("** IMP: filter with or")
df28=pd.DataFrame(List25)
df28=df28[(df28['Name']=='Jack') | (df28['Name']=='akhil')]
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
df18 = pd.DataFrame({'Animal': ['Falcon', 'Falcon','Parrot', 'Parrot'],
	'Max Speed': [380., 370., 24., 26.]})
print(df18)

print("*** group by - sum")
group=df18.groupby(['Animal']).sum()
print(group)

print("*** group by - mean")
group1=df18.groupby(['Animal']).mean() 
print(group1)



 