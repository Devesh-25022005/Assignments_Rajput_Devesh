#1) Explore more regex patterns
#Eg. The regex pattern used to validate email addresses, mobile no, string, and more
import pandas as pd

df = pd.DataFrame({'Email':['abc@gmail.com','wrong_email.com','xyz@domain.co.in','hello@','user@123']})
print(df)
mail_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
df['Valid_Email'] = df['Email'].str.match(mail_pattern)
print(df)

df = pd.DataFrame({
    'Mobile': ['9876543210', '1234567890', '9999999999', '5000000000', '812345678']
})

mobile_pattern = r'^[6-9]\d{9}$'

df['Valid_Mobile'] = df['Mobile'].str.match(mobile_pattern)
print(df)

df = pd.DataFrame({
    'Price': ['₹40,000', '$5000', 'Rs.600', 'Free', '1200INR']
})

# Extract all numbers
df['Extracted'] = df['Price'].str.extract(r'(\d+)')  # first number
print(df)

#2) Explore more datetime function and uses in pandas
data = {"date":['23-06-25','4-08-25','7-09-25','12-08-25']}
df = pd.DataFrame(data)
df['date'] = pd.to_datetime(df['date'])
df['year'] = df['date'].dt.year
df['day_name']=df['date'].dt.day_name()
df['is_month_end']=df['date'].dt.is_month_end
print(df)

#Q3) Import an meaningful csv file for data analysis and perform data cleaning, and analysis for meaningful output
df = pd.read_csv('customers.csv')
new_df = df.dropna()
print(new_df)
print(df)
print(df.to_string())
print(df.head(5))
print(df.info())
print(df.describe())
print(df.shape)
print(df.columns)
print(df['First Name'])
gd = df.groupby('City')['Customer Id'].count()
print(gd)
print(df['First Name'].value_counts())

x = df["Index"].mean()
df.fillna({"Index":x}, inplace =True)
print(df)