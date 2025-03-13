def operator(a,b):
    print(a is b)
    print(a is not b)

def call():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    operator(num1,num2)

call()