import sys

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
def mod(a,b):
    return a%b

def UI():
    
    print("\n-------- choose an operation --------\n1.Addition\n2.Subtraction\n3.Multiply\n4.Divide\n5.Modulus\ne.Exit")
    choice = input("Enter your choice: ")
    if(choice == 'e'):
        sys.exit()
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    if(choice=='1'):
        print("The sum is: ",add(num1,num2))
    elif(choice=='2'):
        print("The difference is: ",sub(num1,num2))
    elif(choice=='3'):
        print("The product is: ",multiply(num1,num2))
    elif(choice == '4'):
        print("The dividision is: ",divide(num1,num2))
    elif(choice == '5'):
        print("the modulus is: ",mod(num1,num2))
    else:
        print("Wrong input!!!!!!!")

while(1):
    UI()
