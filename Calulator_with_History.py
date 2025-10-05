History_file="History.txt"
def show_history():
    file=open(History_file,"r")
    lines=file.readlines()
    

    if len(lines)==0:
        print("No History Found")
    else:
        for line in reversed(lines):
            print(line.strip())
    file.close()

def Clear_History():
    file=open(History_file,"w")
    file.close()
    print("History Cleared")

def save_to_history(equation,result):
    file=open(History_file,"a")
    file.write(equation+"="+(str(result)+"\n"))
    file.close()



def calculate(user_input):
    parts = user_input.split()
    if len(parts)!=3:
        print("Invalid input. Use format: number operator number (e.g., 8 + 8)")
        return

    try:
        num1 = float(parts[0])
        op = parts[1]
        num2 = float(parts[2])
    except ValueError:
        print("Invalid number input.")
        return
    
    if op=="+":
        result=num1 + num2
    elif op=="-":
        result=num1-num2
    elif op=="*":
        result=num1*num2
    elif op=="%":
        result=num1%num2
    elif op=="**":
        result=num1**num2
    elif op=="/":
        if num2==0:
            print("Can not divided by Zero")
            return
        
        result=num1/num2
        
    else:
        print("Invalid Operator use only (+,-,*,/,%,**)")
    
    if int(result) == result:
        result=int(result)
    print("Result:",result)
    save_to_history(user_input,result)

def main():
    print("---Simple Calculator type--->(history, clear or exit)")

    while True:
        user_input=input("Enter Calculation(+,-,*,/,**,%) or Command (history, clear, exit) =")
        if user_input=="exit":
            print("GoodBye")
            break
        elif user_input=="history":
            show_history()

        elif user_input=="clear":
            Clear_History()

        else:
            calculate(user_input)

    
main()
    


