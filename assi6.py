#Q1 Convert series of datestrings to time series
import pandas as pd

date = pd.Series(["2025-06-24","2024-09-25","2005-02-25"])
dates = pd.to_datetime(date)
values = pd.Series([100,110,120],index=dates)
print(values)

#Q2 
df1 = pd.DataFrame({"Name":["Raju","Ramu","Geeta"],
                    "id":[101,102,103],
                      "salary":[10000,11000,12000]},
                      index=[1,2,3])
df2 = pd.DataFrame({"Name":["Mohan","Sohan","Geetanj"],
                    "id":[101,102,104],
                      "salary":[10000,11000,12000]},
                      index=[1,2,3])
#inner merge
print(df1.merge(df2, on ="id",how="inner"))
#left join
print(df1.merge(df2, on="id", how="left"))
# the values which are missed in either of the dataframes are displyed Nan. In these way missing values are handled

#right join based on a commun col salary
print(pd.merge(df1,df2, on="salary", how="right"))
#merge with mutiple keys
print(df1.merge(df2, on = ["id","salary"], how="right"))
#index based join
print(df1.join(df2, lsuffix="_l", rsuffix='_r'))

# comparing the results we can see that pd.merge() merges df1 and df2 based on a commun column salary and whereas in pd.join() joins df1 and df2(just placed df2 horizontal yo df1 based on index) 


one = pd.DataFrame({'Name':["A1",'A2','A3','A9'],
                    'Subject':["sub1",'sub2','sub3','sub4'],
                    'Marks':[80,56,78,90]},
                    index=[1,2,3,4])
two = pd.DataFrame({'Name':["A4",'A5','A6','A7'],
                    'Subject':["sub5",'sub8','sub1','sub9'],
                    'Marks':[88,57,79,93]},
                    index=[1,2,3,4])
three =  pd.DataFrame({'Name':["A10",'A11','A12','A13'],
                    'Subject':["sub5",'sub10','sub11','sub12'],
                    'Marks':[81,58,80,98]},
                    index=[1,2,3,4])
result = pd.concat([one,two,three])
print(result)

print(result.merge(three, on="Subject",how="outer"))


#Primary differences pd.merge and df.join
#pd.merge
#Works like SQL JOIN,Can specify on common column left_on, right_on for different column names

#Methods "inner", "left", "right", "outer"
#syntax :pd.merge(left_df, right_df, on='column_name', how='jointype')

#df.join
#Joins on the index by default,To join on columns,Slightly limited compared to merge()
#syntax:  df1.join(df2, how='jointype')

