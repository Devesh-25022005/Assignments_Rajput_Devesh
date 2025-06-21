#Q1
name = input("Enter your name: ")
className = input("Enter your class: ")
print("Enter marks of 5 subjects")
m1 = int(input("Subject 1: "))
m2 = int(input("Subject 2: "))
m3 = int(input("Subject 3: "))
m4 = int(input("Subject 4: "))
m5 = int(input("Subject 5: "))
total = m1 + m2 + m3 + m4 + m5
percentage = (total / 500) * 100

print(f'''
Name       = {name}
Class      = {className}
Total Marks= {total}
Percentage = {percentage:.2f}%
''')


#Q2
str1 = str(input("Enter string1"))
str2 = str(input("Enter string2"))
str = str1+str2
print(str)
print(str.capitalize())
print(str.upper())
print(str.title())
print(str.isalnum())
print(str.split())


