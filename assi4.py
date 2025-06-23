#Q1 CSV file
import csv
address_book = [["Name","Address","Mobile","Email"],
                 ["Jethalal","Mumbai","1238902340","jetha@mail.com"],
                 ["Doraemon","Japan","3456234570","dora@mail.com"],
                 ["Daya","CID Bureau","daya@mail.com"]]

with open("address_book.csv","w", newline="") as file:
    writer = csv.writer(file)
    for x in address_book:
     writer.writerow(x)
with open("address_book.csv","r") as file:
   reader = csv.reader(file)
   for row in reader:
      print(row)

#Q2
import requests

def weather(city):
  url= f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=8330c3c2ff4eb46a37ef64414b457d49&units=metric"
  try:
    response= requests.get(url)
    response.raise_for_status()
    data = response.json()
    # print(data)
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    feels_like = data['main']['feels_like']
    visibility = data['visibility']
    country = data['sys']['country']

    # print(data)

    print(f"Weather in {city}:")
    print(f"Temperature: {temperature}°C, Humidity: {humidity}%, Feels Like: {feels_like}°C")
    print(f"visibility:{visibility}meters, Country: {country}")
    print(f"Weather Description: {data['weather'][0]['description'].capitalize()}")
  
  except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
    
city = input("Enter the city name: ")
weather(city)

#Q3
import sqlite3

conn = sqlite3.connect("db2.db")

# conn.execute('''
#        Create Table Employee (
#                emp_Id INTEGER PRIMARY KEY AUTOINCREMENT,
#                emp_Name VARCHAR(100),
#                salary INTEGER,
#                department VARCHAR(100))

#  ''')

# conn.execute('''
#        Create Table Student (
#                roll_no INTEGER PRIMARY KEY AUTOINCREMENT,
#                Name VARCHAR(100),
#                Marks INTEGER
#                )

#  ''')

# conn.execute('''
#        Create Table Faculty (
#                Faculty_id INTEGER PRIMARY KEY AUTOINCREMENT,
#                Name VARCHAR(100),
#                Department VARCHAR(100)
#                )
#''')

conn.execute('''
Insert into Employee(emp_name,salary,department)
             Values ("rajat",10000,"Sales"),
             ("Pranay",40000,"Finance")
             '''
    
)
conn.execute('''
Insert into Student(Name,Marks)
             Values ("Preet",100),
             ("Raghu",40)
             '''
    
)
conn.execute('''
Insert into Faculty(Name,Department)
             Values ("Mohandas","Electrical"),
             ("Pranil","Mechanical")
             '''
    
)

data1 =conn.execute('''
Select * from Employee
''')
for x in data1:
  print("Employee Table",x)
data2=conn.execute ('''
Select * from Student'''
              )
for x in data2:
  print("Student Table",x)
data3=conn.execute ('''
Select * from Faculty''')
for x in data3:
  print("Faculty Table",x)

conn.execute('''
update Employee set emp_name = "Rohit" where emp_id = 2
''')
conn.execute('''
update Student set Name = "Roy" where roll_no = 1
''')
conn.execute('''
update Faculty set Name = "Risky" where Faculty_id  = 2
''')
id = input("Enter the roll_no of Student to delete: ") 
conn.execute("DELETE FROM Student WHERE roll_no  ="+ id)
conn.commit()
conn.close()