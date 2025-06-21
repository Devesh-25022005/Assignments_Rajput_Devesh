#Q1 Practise dictionary,tuple,set
d = {1:"Python", "name":"Programming Language", 3:{1:"one",2:"two"}}
print(d)
print(d[3])
print(type(d))
print(d["name"])


#tuple
t= (1,2,3,4,5,6,7,8,9)
print(t)
print(type(t))
l=len(t)
for x in t:
    print(x)
for i in range(l):
    print(i, t[i])

#set
s={"apple", "banana", "cherry","d","e"}  
print(s)
s.add("orange")
s1 = {"apple", "mango", "papaya"}
s2 = s.union(s1) 


#Q2 Basic Arithmetic Operations using function

def operations(a,b):
   print("Sum is",a+b)
   print("Difference:",a-b)
   print("Multiplication:",a*b)
   print("Division is:",a/b)  
n1 = int(input("Enter number 1")) 
n2 = int (input("enter number 2"))


operations(n1,n2)



#Q3 Pallindrome 
n = int(input("Enter number"))
number=n
z  = 0
while n!=0:
    r = n%10
    z = z*10+r
    n = n//10

if z==number:
    print(number,"is pallindrome")
else:
    print(number,"is not pallindrome")