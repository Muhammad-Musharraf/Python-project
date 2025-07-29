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
