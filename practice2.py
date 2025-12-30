'''age=15
if age>=18:
    print("You are eligible to vote.")
print("Thank you.")    

color=input("enter traffic light color:")
if color=="red":
    print("Stop")
elif color=="yellow":
    print("Ready to go")
elif color=="green":
    print("Go")
else:
    print("Invalid color")
age=int(input("enter your age:"))
if age<13:
    print("You are a child.")
elif age>=13 and age<20:
    print("You are a teenager.")
elif age>=20 and age<60:
    print("You are an adult.")  
else:
    print("You are a senior citizen.")  
  

#for nested loops
username=input("enter username:")
password=input("enter password:")   
if username=="admin" and password=="pass":
    print("Access granted.")
else:
    if username!="admin":
        print("Invalid username.")  
    else:
        print("Invalid password.") 

n=int(input("enter a number:"))
i=1
while i<=10:
    product=n*i
    print(n,"x",i,"=",product)
    i=i+1   

#print odd nums using continue
i=1
while i<=20:
    if i%2==0:
        i=i+1
        continue
    print(i)
    i=i+1

name="mani"
for i in name:
    print(i)

#vowel count
text=input("enter a string:")
vowels="aeiouAEIOU"
count=0
for char in text:
    if char in vowels:
        count+=1 
print("Number of vowels:", count)     

#sum  of n natural numbers
n=int(input("enter a number:"))
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)    

#lambda function
square=lambda x: x**2
print("Square of 5 is", square(5))'''

#factorial
n=int(input("enter a number:"))
fact=1
for i in range(1,n+1):
    fact*=i
print("Factorial of", n, "is", fact )