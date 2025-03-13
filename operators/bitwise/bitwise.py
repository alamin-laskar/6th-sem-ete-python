def operator(x,y):
    x, y = 5, 3
    print(x & y) 
    print(x | y) 
    print(x ^ y) 
    print(~x)     
    print(x << 1) 
    print(x >> 1)

    
def call():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    operator(num1,num2)

call()