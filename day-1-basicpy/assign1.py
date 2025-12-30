#question1
name=input("enter your name:")
age=input("enter your age:")
print("Hello " + name + ", you are " + age + " years old.")

#question2
a=int(input("enter first number:"))
b=int(input("enter second number:"))
sum=a+b
diff=a-b
prod=a*b
quotient=a/b
print("Sum:", sum)
print("Difference:", diff)      
print("Product:", prod)
print("Quotient:", quotient)

#question3
a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=float(input("enter third number:"))
a=float(a)
b=float(b)
average = (a + b + c) / 3
print("Average:", average)

#question4
num_str=input("enter a number:")
num_int=int(num_str)
num_float=float(num_str)
num_string=str(num_str)
print(num_int,type(num_int))
print(num_float,type(num_float))
print(num_string,type(num_string))

#question5
x=10 + 3 *2 ** 2
print(x)

#question6
a=int(input("enter first number:"))
b=int(input("enter second number:"))
a,b=b,a
print("After swapping: a =",a,"b =",b)

#question7
celsius_str=input("enter temperature in celsius:")
celsius=float(celsius_str)
fahrenheit=(celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)

#question8
r=float(input("enter radius of circle:"))
pi=3.1416
area=pi*r**2
print(area)

#question9
P=float(input("enter principal amount:"))
R=float(input("enter rate of interest:"))
T=float(input("enter time in years:"))
SI=(P*R*T)/100
print("Simple Interest:", SI)

#question10
num = float(input("Enter a decimal number: "))

integer_part = int(num)
fractional_part = num - integer_part

print("Integer part:", integer_part)
print("Fractional part:", fractional_part)
