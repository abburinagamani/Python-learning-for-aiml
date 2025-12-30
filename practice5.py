'''f=open("sample.txt","w")
print(f.write("hello world"))
f.close()

#for delete files
import os
os.remove("sample2.txt")


data=True
line=1
with open("sample.txt","r") as f:
    while data:
        data=f.readline()
        if ("python" in data.lower()):
            print(f"word found at line {line}")
            break
        print(data)
        line+=1

#exception handling
try:
    a=int(input("Enter a number:"))
    b=int(input("Enter another number:"))
    result=a/b
    print("Result:",result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter numeric values.")    
else:
    print("Division successful.")
finally:    
    print("Execution completed.")'''

#list comprehension
squares=[x**2 for x in range(1,11) if x%2!=0]
print(squares)

nums=[-2,-1,-3,2,1,-1]
new_nums=[0 if val<0 else val for val in nums]
print(new_nums)