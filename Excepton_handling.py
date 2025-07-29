try:
    numenator =int(input("enter the number of numenator: "))
    demonator =int(input("enter the number of denonator: "))
    result = numenator/demonator
    #print(result)
   
except ZeroDivisionError as e:
    print(e)
    print("you cant divide by zero!!!!!! idiot  ")    
except ValueError as e:
    print(e)
    print("write only number plz !!!!----")    
except Exception as e:
    print("Something went wrong :( ") 

except TypeError as e:
    print(e)
    print("this is a type_error idiot  $$$")
 
    print("idiot slove this issue :(")          
else:
   print(result)
finally:
    print("this wil always eceute")
