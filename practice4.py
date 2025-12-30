'''class Student:
    subject="Mathematics"
    college="ABC College"
stu1=Student()
stu2=Student()
print(stu1.subject,stu1.college)

#class and instance(Attributes
class Student:
    college ="ABC college"#class
    def __init__(self,name,age):
        self.name=name#instance
        self.age=age    
student1=Student("Alice",20)
student2=Student("Bob",22)
print(student1.name,student1.age,student1.college)
print(student2.name,student2.age,student2.college)        

#instance methods
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name:",self.name)#here we are accessing instance class and instance attributes
        print("Age:",self.age)
student1=Student("Alice",20)
student2=Student("Bob",22)
student1.display()
student2.display()

#product_store
class Product:
    count=0
    def __init__(self,name,price):
        self.name=name
        self.price=price
        Product.count+=1
    def display_info(self):
        print("Product Name:",self.name)
        print("Price:",self.price)
    @classmethod
    def get_count(cls):
        return cls.count
    @staticmethod
    def calculate_discount(price,discount):
        return price-(price*discount/100)
p1=Product("Laptop",800)
p2=Product("Smartphone",500)
p1.display_info()
p2.display_info() 
print("Total products:",Product.get_count())   
p1.calculate_discount    

#encapsulation
class BankAccount:
    def __init__(self,name,balance):
        self.name=name #public attribute
        self.__balance=balance #private attribute
acc1=BankAccount("Alice",1000)
print(acc1.name)'''

#inheritance
class Employee:
    start_time="9 AM"
    end_time="5 PM"
    def change_shift(self,new_start,new_end):
        self.start_time=new_start
        self.end_time=new_end
class Teacher(Employee):
    def __init__(self,subject):
        self.subject=subject
t1=Teacher("Mathematics")
t1.change_shift("8 AM","4 PM")
print("Subject:",t1.subject,t1.start_time,t1.end_time)   

#multilevelinheritance
class Employee:
    start_time="9 AM"
    end_time="5 PM"
class Administrator(Employee):
    def __init__(self,role):
        self.role=role
class Manager(Administrator):
    def __init__(self,department,role):
        super().__init__(role)
        self.department=department
acc1=Manager("Sales","Admin")
print("Department:",acc1.department,acc1.role,acc1.start_time,acc1.end_time)        