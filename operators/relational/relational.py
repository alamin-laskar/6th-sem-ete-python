
def operator(x,y):
    print(x == y) 
    print(x != y)  
    print(x > y)   
    print(x < y)   
    print(x >= y)  
    print(x <= y)  




def call():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    operator(num1,num2)

call()