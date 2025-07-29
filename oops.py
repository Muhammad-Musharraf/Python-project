# class Student:
#     name = "Urooj Wadood"
#     Location = "General store"
# s1 = Student()
# print(s1.name)
# print(s1.Location)   
 
# s2 =Student()


class Car:
    Name = "KIA Motors"
    Model = "Sportage"
    year ="2024"

c1 = Car()
print(c1.Name)   
print(c1.Model) 
print(c1.year)

class Student:
    # #default Constructor
    # def __init__(self):
    #pass
  
      #parameterized Constructor  
    def __init__(self,name, Marks):
        self.name = name
        self.Marks = Marks
        print("adding new Student of Database...")
   
s1 = Student("Saleem",57)
print(s1.name, s1.Marks)

s2 =Student("waleed",99)
print(s2.name, s2.Marks)

s3 =Student("Urooj",85)
print(s3.name,s3.Marks)
 

