#  Write a program to find the bigger between two numbers. 
def bigger(a,b):
    if(a>b):
        print(a," is bigger.")
    else:
        print(b, " is bigger.")
    # print(max(a,b)," is bigger.")
def get_Value():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    bigger(num1,num2)

get_Value()