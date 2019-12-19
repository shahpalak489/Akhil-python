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

