#Q1 
# create panda series from a dictionary

import pandas as pd
dict = {"Ram":40,"Raju":78,"Mohit":89}
sd = pd.Series(dict)
print(sd)

# create panda series from list
list =["Python","Java","C++","C"]
sl = pd.Series(list)
print(sl)

#Accessing element of series in panda
print(sd["Ram"])
print(sl.iloc[2])
print(sd.loc["Mohit"])
print(sl[0])
print(sd.iloc[0])


#Q2 Dataframes
#Make a pandas dataframe from two dimensional Python list

list_2d = [[1,2,3],[4,5,6],[7,8,9]]
df1 = pd.DataFrame(list_2d, index = ["x","y","z"])
print(df1)

# Dataframe from dict
d = {"a":["Apple"],"b":["ball"],"c":["Cat"]}
df2 = pd.DataFrame(d)
print(df2)

# Dataframe from list of list
ll = [[100,200,300],[400,500,600],[700,800,900]]
df1 = pd.DataFrame(ll, index = ["a","b","c"])
print(df1)

#Dataframe from list of tuples
lt = [("tiger","lion","Monkey"),
      ("Rose","Lotus","Sunflower")]
df_lt = pd.DataFrame(lt)
print(df_lt)

#DataFrame from list of dict
l_dict = [{1:"A",2:"B"},
           {3:"C",4:"D"} ]
df_ldict = pd.DataFrame(l_dict)
print(df_ldict)

#Q3 
#iterate over rows in python dataframe
df = pd.DataFrame([['a','b'],['c','d'],['e','f'],['g','h']],columns=['col1','col2'])
df.index=['r1','r2','r3','r4']
print(df)
result = df.loc['r1':'r3','col1']
print(result)

#selecting rows based on a condition
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Marks': [85, 92, 78, 90]
}

df = pd.DataFrame(data)
print(df)
high_scores = df[df['Marks'] > 85]
print(high_scores)

#dataframe from using iloc
print(df.iloc[0])

#limited row selection with a given col
print(df.loc[0:2,"Name"])

# drop row based on a condition
result = df[df["Marks"]!=92]
print(result)

#Insert row at a given position in pandas dataframe
df.loc[3] = ['Aly', 88] 
print(df)



#Create a list from pandas Df
l_name = df["Name"].tolist()
l_marks = df["Marks"].tolist()
print(l_name)
print(l_marks)
