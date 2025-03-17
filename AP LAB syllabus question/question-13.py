#  Write a program using while loop find sum of the following series. 1+3+5+7+……+N
def calculate(n):
    sum =0
    for i in range(1,n,2):
        sum+=i
        
    return sum
def take_input():
    S_len = int(input("Enter the length: "))
    print("sum of the series:  ", calculate(S_len))
take_input()


