def operator(a,b):
    a+=b
    print(a)
    b-=a
    print(b)
    a*=b
    print(a)
    b/=a
    print(b)
    a%=b
    print(a)
    a**=b
    print(a)
    b//=a
    print(b)


def call():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    operator(num1,num2)

call()