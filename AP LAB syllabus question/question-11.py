#  Write a program to find the largest of three numbers. 

def largest_of_three(a, b, c):
    # return a if (a >= b and a >= c) else (b if b >= c else c)
    # return max(a, b, c) 
    if(a>b):
        if(a>c):
            return a 
        elif(c>b):
            return c
    elif(b>c):
        return b
    else:
        return c

def call():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    num3 = int(input("Enter another number: "))

    result = largest_of_three(num1, num2, num3)
    print("The largest number is:", result)

call()
