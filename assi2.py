#Q1 Practice of the session
#Q2
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
if percentage>=60:
       print("Grade A")
elif percentage>=50 and percentage<60:
       print("Grade B")
elif percentage>=40 and percentage<50:
       print("Grade C")
elif percentage>=33 and percentage<40:
       print("Grade D")
else:
       print("Fail")

#Q3 Factorial
f=1
n = int(input("Enter the number"))
for i in range(1,n+1): 
  f=f*i
print(f"factorial of {n} is {f}")

#Q4
items = []
prices = []

while True:
    print("\nEnter choice: ")
    print("1. Create Bill")
    print("2. Display Item Price and Total Bill")
    print("3. Display Total")
    print("4. Exit")
    n = int(input("How many items? "))
    for i in range(n):
            item = input(f"Enter name of item {i+1}: ")
            price = float(input(f"Enter price of {item}: ₹"))
            items.append(item)
            prices.append(price)
    choice = input("Your choice: ")
    if choice == '1':
         print(items)
         print(prices)
         print("Bill is created")
      
    elif choice == '2':
         
            for i in range(len(items)):
                print(f"{items[i]} - ₹{prices[i]}")
            print(f"Total = ₹{sum(prices)}")

    elif choice == '3':
        print(f"Total Amount = ₹{sum(prices)}")

    elif choice == '4':
        print("Exiting... Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")



# #Q5 i) to find smallest number

ls = [23, 4, 67, 9 ,10]
min=ls[0]
for i in range(len(ls)):
    if ls[i]<min:
        min=ls[i]
print(f"Smallest number in the list is {min}")
ls.remove(min)
# second smallest
second_min=ls[0]
for i in range(len(ls)):
    if ls[i]<second_min:
        second_min=ls[i]
print(f"Second smallest number in the list is {second_min}")

# greatest number
max=ls[0]
for i in range(len(ls)):
    if ls[i]>max:
        max=ls[i]
print(f"Largest number in the list is {max}")
ls.remove(max)

#second greatest
secmax=ls[0]
for i in range(len(ls)):
    if ls[i]>secmax:
        secmax=ls[i]
print(f"Second Largest number in the list is {secmax}")