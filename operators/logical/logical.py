def operator(a,b):
    a, b = True, False
    print(a and b)  
    print(a or b)  
    print(not a)    



def call():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    operator(num1,num2)

call()