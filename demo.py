# Day-1 for python practice
"""print('hello world ................')
x = 23
y = 2
print(x*y)
g = " hello world"
s = 2.33334
e = 0 + 4j
print(type(g))
print(type(s))
print(type(e))
name = " shadda kapra"
print(name)
price = 25.99
print(price)
a,b = 7, 6
sum = a*b
print(complex(sum))

c = (1,2,44,6,8,99)
print(type(c))
a = 19+4j
b= 3
print(a + b)
a = True
b = True
print(not(b),a)
y = input("enter your age...  ")
print("the age is",y)
# question 1) intput two number and sum 
x = int(input("enter the number1... "))
y = int(input("enter the number 2... "))
sum = x+y
print(sum)
# question 2) take input the two value of length and print square of the length 
a = int(input("enter the value of side of length.....  "))
#b = int(input("enter the value of side of breath.....  "))
area_of_squre = a**2
print(area_of_squre)
# question 3) take two input float number and make a average
print("input the value to caLCULATE THE Average of given input")
a = float(input("enter the integer value 1 !!!!!.....  "))
b = float(input("enter the integer value 2 !!!!!.....  "))
c = float(input("enter the integer value 3 !!!!!.....  "))
d = float(input("enter the integer value 4 !!!!!.....  "))
Average = a+b+c+d /4
print(Average)
# question 4) take two a and b if a is greater than equal to b print true or if not print false
a = int(input("enter the number1... "))
b = int(input("enter the number2... "))
if a >= b :
    print("True")
else :
    print("false")
    
  # day-2 practice for python  
str1 =input("enter the string value1.... ")
str2 = input("enter the string value 2....")
cont = str1+ " "+str2
print(cont)
print(len(cont)) # calculate the length(its counting starts with 1)
print(cont[0])  #indexing start with  thats why its called it is 0 indexing
print(cont[0:len(cont)])
print(cont[-3:-1])

# string funtion
str ="i am coder "
print(str.endswith("er "))
print(str.capitalize())
print(str.replace("coder","Monster"))
print(str.find("i"))
print(str.count("c"))
# question 1) WAP to input user’s first name & print its length
x = input("Enter the First name please!!!!!! ")
print(x)
print(len(x))
# question 2) WAP to find the occurrence of ‘$’ in a String.
j = "Suffyan khan my friend do you know  $$$$$......!!!!!*****"
print(j,j.count("$"))

# Conditional Statement 
 #  if-elif-else (SYNTAX)
marks = int(input("Enter the value of marks of a student"))
if marks >= 90 :
    print("congrastulation you get a  A-Grade ")
elif marks >= 80 and marks <= 90 :
    print("congrastulation you get a  B-Grade ")    
elif marks >= 70 and marks <= 80 :
    print("Congrastulation you get a  C-Grade" )
elif marks >= 70 :
    print("congrastulation you get a  D-Grade ")
else :
    print("never give up your learning marks does not define your future but remember one thing you should keep learning and hardwork  you get a  E-Grade" )       

# question 1) WAP to check if a number entered by the user is odd or even
a = int(input("Enter the number to check even or odd "))
if a % 2==0 :
    print("Even number")
else :
    print("Odd Number")    
# quesion 2) WAP to find the greatest of 3 numbers entered by the user.
a = int(input("enter the num1....  "))
b = int(input("enter the num2.....  "))
c = int(input("enter the num3.....  "))
if a > b :
    print("the greatest of 3 number is  ",a)
elif b > c :
    print("the greatest of 3 number is  ",b)
elif c > a :
    print("the greatest of 3 number is ",c)
else :
    print("invalid numbers") 
 
# Question 3) WAP to check if a number is a multiple of 7 or not.   
a = int(input("enter the table ....  "))
if a % 7 ==0 :
    print("it is multiple of ",{a})
else :
    print("invalid means its not multiple of 7")              
     
# day-3 PRACTICE FOR PYTHON!!!!!!
 # In-bulid function
y = abs(-12.99)
print(y)
x = bin(56)
print(x)
s = bytes(4)
print(s)
d = chr(98)
print(d)
z = chr(90)
print(z)
c = complex(3,5)
print(c)
z = complex(0,5)
print(z)
t = float(46)
print(t)
h= int(12+3.55)
print(h)
a = str("2568")
print(a)
print(type(a))
b = str(25.68)
print(b)
print(type(b))
# help(print)
# help(float)
h= input("enter your name $$$.....!!!..... ")
print("HELLO",h)
y = int(input("Enter your age please......"))
print("your age is",y)

# program to display number 1 to 5
i = 1
n = 5 
while i <= n :
    print(i)
    i=i+1
# enter the value of a user and make a multiplication table till 
x = int(input("enter the value of a table...."))
i=1
while i<=10 :
    print(i*x)
    i=i+1
print("the table of ", x ,"is here wow")
# make a voting age
 #y =int(input("enter your age....."))
# while y>=18 :
   # print("you can vote") infinite loop
y =int(input("enter your age.....")) 
if y >= 18 :
    print("you can vote.....xd")
else :
    print("Sorry bro you can not cast vote ")    
count = 0 
while count<=10 :
    print("hello student")
    count=count+1 
else :
    print("this is the else block " ) 
     
 # for loop 

for i in range(100):
    print(i)  # Output: 0, 1, 2, 3, 4
    
furits =["banana","strawberry","cherry","mango","blackberry"]
for x in "banana":
    print(x)    
for x in furits:
    print(x)    
for c in range(3,11):
     print(c)   
 #  nested loop "if-else"
age = 27
own_car ="True"
if age >=18 :
    
    if (own_car =="True") :
         print("Drive a car")
    else :
        print("work hark and purchare a new car bro...... ") 
else :
    print("beta bare hu ja phir car chalana ehhe ehhe......")            

# Day-4 practice for python come on bro lets do it!!!
# user- define function
def my_funtion():
    print("hello World ")         
my_funtion()   
   # creating use define function
def brocode():
       print("hello everybody") 
       print("hello world")
       print("hello coders")
brocode()   
my_funtion() #calling a function
def x():
    c = input("enter the address of your school  ")
    print("your school address is ", c)   
x()    
def contract():
    print("contract detailed of the school") 
    print("Rose house Grammar School")
    print("Orangi Town Karachi")
    print("+92334566788") 
    print("RHGS@gmail.com")
contract()    
for i in range(14):
    a = input("enter the name of a student ")
    b = int(input("enter the marks of math out of 100 "))
    c = int(input("enter the marks of islamiat out of 100 "))
    d = int(input("enter the marks of science out of 100 "))
    e = int(input("enter the marks of social study out of 100 "))
    f = int(input("enter the marks of art out of 100 "))
    g = int(input("enter the marks of English out of 100 "))
    sum = b+c+d+e+f+g
    percentage= sum/600*100
    print("congrasulation your hardwork ,dedication & support of your parents a you get a percentage of ",percentage)
    contract()     
  # two argument
def my_function(fname,lname):
        print(fname,"",lname)
my_function("Amania","Shahid")        
    # calculate a program to calculate the electricity bill
def electricity_bill(n):
 if n<= 100 :
    print("your bill rate is",n*7.74)
 elif n<= 500 and n>= 100 :
    print("your bill rate is",n*20)
 elif n<= 700 and n>= 500 :
    print("your bill rate is",n*25)
 elif n<= 1000 and n>= 500 :
    print("your bill rate is",n*30)
 else :
    print("your bill rate is",n*50)                
def intraction():
    print("last date bill payingis 20-june-2025")
    print("after 20-june-25 you pay RS 1000 as a fine")
for i in range(3):
    g=input("Enter the name of coustemer")
    f=int(input("inter your coustemer id"))
    n=int(input("Enter the electricity  unit you have used" )) 
    print(g)
    print(f)
    print(n)
    print("  ")
    print("details of your electricity bill")
    electricity_bill(n)
    intraction()
 
# revised topic which is "STRING"lets do it
a ="hello Amania how are you doing today????"
print(a.upper())            
b ="HELLO IQRA HOW ARE YOU DOING TODAY????????"
print(a.lower())            
print(b.replace("IQRA","SARA"))                
print(b.find("I"))        
g= "hello my dear friend how are you brother" 
print(g[::-1])      
 # Day-5 practice of python 
 # today topic is list and tuples lets do it buddy!!!!!
 # List       
a = ["Apple",804,True,"Strawberry"]  
print(a)
print(type(a))
print(a[::-1]) #reverse of list
q=list[1,2,3,4,5] #list contucture
print(q)
print(types(q))
marks= [99,98,97,96,95,94,93,92,88,77,678,90]   
print(marks)
print(marks[1])      
print(marks[1:4])   
print(len(marks))
print(marks[1:])    
print(marks[-12:-1])     
a = ["Apple","Cherry","PineApple","Strawberry"]     
a[0:3]=["cake","banana"]
print(a[0:4:2])   
list=[2,1,6,3,4,99,98,97,96,"Apple","Cherry",True,"PineApple","Strawberry",95,94,93,92,88,77,678,90]   
list.append("ali khanzada")  
list.reverse()
list.remove("Apple")

print(list)   
abc =[2,1,6,3,4,99,98,97,96,95,94,93,92,88,77,678,90]   
abc.sort(reverse=True )
print(abc)
abc.sort()
print(abc) 
abc.insert(1, 5)
print(abc)
abc.remove(99) 
abc.pop(3)  
print(abc)
abc =[2,1,6,3,4,99,98,97,96,95,94,93,92,88,77,678,90] 
q = 0 
for i in range(17):
    q = q+ abc[i]
    print("the sum of a list is",q)
# question Multiply all the number of a list.
abc =[2,1,6,3,4,99,98,97,96,95,94,93,92,88,77,678,90] 
b=1
for i in range(17):
    b = b *abc[i]
    print("the list of all multiply is a",b)
s = ["ali","ahmed","faian","mustafa","ali"] 
print(s[0])   
# list me duplicate allow huta hai bro
 # tuple
a =("ali","ahmed","faian","mustafa")  
print(a)
print(type(a))
print(a[0])  
tup = (2,1,3,1)
tup.index(2)
print(tup)
tup.count(3)   
print(tup)  
# Let‘s Practice
 # WAP to ask the user to enter names of their 3 favorite movies & store them in a list.   
f = input("Enter the three favourite movies name bro $$$ ")          
s = input("Enter the three favourite movies name bro $$$ ")                  
q = input("Enter the three favourite movies name bro $$$ ")  
list = [f,s,q]
print(list)   
  
 # WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method)  
list1 = [1,2,3,2,1]
list2 = [1,2,1]
list3= [1,"abc","abc",1]
copy_list = list1.copy()
copy_list.reverse()
if(copy_list== list1) :
    print("palindrome")  
else :
    print("not palindrome")
    # ---------
list1 = [1,2,3,2,1]
list2 = [1,2,1]
list3= [1,"abc","abc",1]
copy_list = list3.copy()
copy_list.reverse()
if(copy_list== list3) :
    print("palindrome")  
else :
    print("not palindrome")
                

# WAP to count the number of students with the “A” grade in the following tuple.   
a = ("C","D","A","A","B","B","A")  
print(a.count("A"))
print(a.index("A"))  
# Store the above values in a list & sort them from “A” to “D”
E =["B","D","C","A"]
E.sort( )
print(E) 
a = ("hello",["world"],(123,345,678))
print(a)
print(type(a))
# tuple contrcture
p =tuple((1,2,3,4,5,6,7,8))
print(p)
print(type(p))
# sciling
p =tuple((1,2,3,4,5,6,7,8))
print(p)
print(p[0:7])
print(p[-1:])
print(p[0:8:2])
print(p[::-1]) # reverse of tuples
t= (1,2,3,2,1)# duplicate is allow
print(t)
print(type(t))
w=(1,2,3,4,5,6,7,8,9,10)
y =list(w)
y.append(30)
w = tuple(y)
print(w)
print(type(w))# tuple is unchangeable that's why we use type casting method to add in tuples
w=(1,2,3,4,5,6,7,8,9,10)
y =list(w)
y.remove(5)
w = tuple(y)
print(w)
print(type(w))
#delete
w=(1,2,3,4,5,6,7,8,9,10)
# del(w)
print(w)
# loop in tuple
e = ("A","B","C","D","E")
for i in e:
    print(i)
tup1= (1,2,3,4,5)
tup2=("a","b","c","d")
print(tup1+tup2)
u= ("\nI LOVE YOU TUBA SHAHID ")
q= u*100
print(q)
print(len(q))
print(q+q+q)

# write a program to take input from user and store it in a tuple
T =()
i=0
while i<=5:
    num = int(input("Enter the value to store the tuple"))
    T = T+(num,)
    print(T)
    i=i+1
    
# Day - 6 for practice of python lets do it bro $$$$
# topics: SETS & DICTIONARY
  # topic:- Dictionary
dict ={ "name":"Musharraf",
         "CGPA": 3.2,
         "marks": [23,29,25,20] 
        }

print(dict)
print(type(dict))
Student= {
      "name":"Musharraf Muzammil",
      "score": { "math": 88,
               "English": 87,
               "Urdu": 68
            }
}
print(Student)
print(type(Student))  
mydict ={ "name":"Musharraf",
         "CGPA": 3.2,
         "marks": [23,29,25,20] 
        }
print(mydict.keys())
print(mydict.values()) 
print(mydict.items()) 
print(mydict.get("name"))
Student= {
      "name":"Musharraf Muzammil",
      "score": { "math": 88,
               "English": 87,
               "Urdu": 68
            }
}
print(Student)
new_dict ={"SST":98,"Science":93,"isl":91}
Student.update(new_dict)
print(Student) 
print(len(Student))  
print(Student.pop("SST"))
print(Student)
del Student["name"]
print(Student)
Student.clear()
print(Student)
dict1 ={1:10,2:20}
dict2 ={3:30,4:40}
dict3 ={5:50,6:60}
dict4 ={}
for d in (dict1,dict2,dict3):
    
    dict4.update(d)
print(dict4)
d = dict= {}
x =1
for x in range(1,16):
    d[x]=x**2
    print(d)    
#question Check the wheather a given key already exist or not in dictionary
srch ={1: 3,
       5:7,
       9:11,
       13:15,
       17:19}
print(srch)
print(type(srch))
x =int(input("Enter the number of the seraching number OF ABOVE GIVEN NUMBER "))
if x in srch:
    
    print("NUMBER IS eXIST BRO!!!!!")
else:
    print("NOT EXIST")  
# Topics:- Sets  
nums ={1,2,1,2,4,6,8,10,12,14,16,18,20,"abc","issb","damm"}
print(nums)
print(type(nums))
# print(nums[0] index in not exist in sets  
null_sets ={}
print(null_sets) 
sets = {1,2,1,2,4,6,8,10,12,14,16,18,20} 
sets.add(100)
sets.remove(20) 
print(sets)  
#sets.clear() 
print(sets)  
sets.pop()   
print(sets)  
sets2={"ac","fan","remote","mobile",1,2,3,4,5,6,7}
print(sets.union(sets2)) 
print(sets.intersection(sets2))   
#Let's Practice
# Store following word meanings in a python dictionary:  
# table : “a piece of furniture”,“list of facts & figures” ,cat : “a small animal”  
dict ={}
new_dict= {"Table":"a piece of furnitue","dog":"a pet animal","lion":"kings of all animal","cat":"a small animal"}
dict.update(new_dict)
print(dict)
   
# You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students.  
a = {"python","java","C++","python","javascript","java","python","java","C++","C"}
print(a)  
print(len(a))
# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
#           an empty dictionary & add one by one. Use subject name as key & marks as value.  
marks ={}
x =int(input("enter physics:"))
marks.update({"phy": x})    

x =int(input("enter math:"))
marks.update({"math": x})    

x =int(input("enter chem:"))
marks.update({"chem": x})    
print(marks)      
  
 # question Figure out a way to store 9 & 9.0 as separate values in the set. (You can take help of built-in data types)
values = {9,9.0}
print(values)
values = {9,"9.0"}
print(values)  
values = {"9",9.0}
print(values)   
values = {("float", 9.0),
          ("int", 9)
         }
print(values)   
# sets ka topic hai***
setn ={5,10,3,15,2,20}
print("the maximum value is",max(setn)) 
print("the minimum value is ",min(setn))
# write a set of min & max and print print lentn fuction & sets and tuple
s ={2,4,6,8,10,14,18,16}
print(len(s))
print(type(s))
print("the maximum value is",max(s)) 
print("the minimum value is ",min(s))  
y =tuple(s) # tuples
x =list(s)
print(y)
print(type(y))
print(x)
print(type(x))
# Day-7 for practice python bro******
# topic function and recursion
def calc_sum(a,b):
    sum = a+b
    print(sum)
    return(sum)
calc_sum(9,100)  
calc_sum(9909,100) 
calc_sum(9,450) 
calc_sum(9678,100)   
def print_hello():
    print("hello world")
print_hello()    
print_hello()     
print_hello() 
output = print_hello()
print(output)  # none
def calc_sum(a,b):
    return a+b
sum =calc_sum(3,2)
print(sum)   
# average of three number
def calc_average(a,b,c):
    if(a==0):
        print("you are idot!!!")
    sum = a+b+c
    avg = sum/3
    print(float(avg))
    return avg
calc_average(5,10,15)
calc_average(5567,1090,1509)
calc_average(0,3,9) 

  
# Q: Assigning a default value to parameter, which is used when no argument is passed.
def print_deflt(b,a=1):
    print(a*b)
    return a*b
print_deflt(6)

# Q: WAF to print the length of a list. ( list is the parameter)
cities = ["karachi","dubai","berlin","sydney"]
heros = ["salman khan","sk","amir khan"]
def list_print(list):
    print(len(list))      
    
list_print(cities)
list_print(heros)  
# Q:WAF to print the elements of a list in a single line. ( list is the parameter)
def print_list(list):
    for item in list:
        print(item,end=" ")
print_list(cities)        
print_list(heros) 
# q:WAF to find the factorial of n. (n is the parameter)
def calc_fact(n):
    
    fact =1
    for i in range(1,n+1):
          fact*= i
    print(fact)
calc_fact(7)             
calc_fact(5)    
# Q: WAF to convert USD to INR.
def converter(calc_usd):
    ind = calc_usd*85
    print(calc_usd,"usd=",ind,"ind")   
converter(100)  
#n = int(input("enter the number"))
def even_odd(n):
    if n % 2 == 0:
        print("even number")
    else :
        print("odd number")    
even_odd(5)
even_odd(2)  

# Recursive function
def show(n):
    if(n == -1):
        return
    
    print(n)
    show(n - 1)
show(7)   
# ------  
def show(n):
    if (n == 0):
        return
    print(n)
    show(n - 1)

show(6)
def fact(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return fact(n - 1) * n
print(fact(7))   

 
# Write a recursive function to calculate the sum of first n natural numbers.
def sum(n):
    if(n == 0):
        return 0
    return sum(n-1) + n
cal = sum(50)
print(cal)     
fruits = ["Apple","mango","PineApple","Strawberry","Cherry"]
def print_list(list,idx = 0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)   
print_list(fruits)
# file handling ----
f = open("sample.txt","w")   
f.write("I am learning html.\n but i want to learn css")

f = open("sample.txt","a")   
f.write("\nthen i become a suceesful data scientist")
f.close()
f = open("practice.txt","a")

#data = f.read()
#print(data) # read entire data
#print(type(data)) 


# line1 = f.readline()
# print(line1)

# line2 = f.readline()
# print(line2)

# line3 = f.readline()
# print(line3)

# line4 = f.readline()
# print(line4)

# line5 = f.readline()
# print(line5)
f.close()
   
f = open("sample.txt","a+")
#f.write("abc")
print(f.read())
f.write("abc")
f.close()
with open("sample.txt","r") as f:
    data =f.read() 
    print(data)
with open("sample.txt","w") as f:
    f.write("so iam become coder" )
import os
os.remove("practice.txt")   

#Create a new file “practice.txt” using python. Add the following data in it:
# Hi everyone
# we are learning File I/O

# using Java.

# I like programming in Java.

# Q2 WAF that replace all occurrences of “java” with “python” in above file.
with open("practice.txt","r") as f:
    data = f.read()
new_data= data.replace("Java","Python")  
print(new_data)  

with open("practice.txt","w") as f:
    data = f.write(new_data)

# Q3 Search if the word “learning” exists in the file or not.
word = "learning"
with open("practice.txt","r") as f:
    data = f.read()
    if(data.find(word) != -1):
        print("found")
    else:
        print("not found")    
def checkfor_word():
    word = "learning"
    with open("practice.txt","r") as f:
        data = f.read()
    if(data.find(word) != -1):
        print("found")
    else:
        print("not found") 
checkfor_word() 
"""
# Q4 WAF to find in which line of the file does the word “learning”occur first. Print -1 if word not found.
def checkfor_line():
    word = "learning"
    data = True
    line_no = 1
    with open("practice.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no =line_no + 1    
    return -1                       
print(checkfor_line())       

#Q5 From a file containing numbers separated by comma, print the count of even numbers.
count = 0
with open("practice.txt","r") as f:
    data = f.read()
    num = data.split(",")
    for val in num:
        if(int(val) % 2 == 0):
            count+=1
print(count)            

# Exception handling!!!!!!!!!          
        
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
    