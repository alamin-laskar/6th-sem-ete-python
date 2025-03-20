# Create a tuple „T‟ of 10 numbers. Observe the following. 
# a. Use len() to find the length of the tuple. 
# b. Apply T+(100, 200, 300) on T. 
# c. Apply T*4 
# d. Check whether a number is present in the tuple „T‟ or not. (hint: use in) 
# e. Print all of „T‟ using a for loop. 
# f. Print the maximum and minimum value of „T‟.


T = (2,4,5,1,6)
print("length of the tuple: ",len(T))

T+(100, 200, 300)
print(T)

print(T*4)

if 4 in T:
    print("4 is present..")
else:
    print(" 4 is not present")
for i in range(0,len(T)):
    print(T[i])

print("Minimum : ",min(T))
print("Maximum : ",max(T))


