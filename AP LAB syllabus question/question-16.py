# Create a list „L‟ of 10 numbers. Observe the following. 
# a. print  L[0] 
# b. print  L[1:5] 
# c. print  L[:] 
# d. print  L[1:5:2] 
# e. print  L[-1]
# f. print  L[-5:] 
# g. print the length of the list 
# h. Update the list „L‟.
# i. Delete any two values from the list. 
# j. Perform L+[234, 456,765] 
# k. Perform L*4 
# l. Check whether a number is present in the list „L‟ or not. (hint: use in) 
# m. Print all the elements of „L‟ using a for loop. 
# n. Print the maximum and minimum value of „L‟. 
# o. Apply append() function to insert a number to the list „L‟. 
# p. Apply count() function to count objects of the list „L‟. 
# q. Apply extend() function to merge two lists. 
# r. Apply index() function to find index of elements. 
# s. Apply remove() function to remove an element from a list. 
# t. Apply reverse() to reverse a list. 
# u. Apply sort() to sort a list  

def extend_list(L):
    L.extend(["hi","hello"])
    return L

def reverse_list(L):
    L.reverse()
    return L
def update_list(L):
    value = int(input("Enter a value to update the list: "))
    L.append(value)
    return L
def Print_list(L):
    print("printing 0th element",L[0])
    print("printing upto 5th element",L[1:5])
    print("printing the whole list ",L[:])
    print("printing the list alternatively ",L[::2])
    print("printing from th end",L[-1])
    print("printing  with -ve argument ",L[-5:])

    print("length pf the list: ",len(L))

    updated_lst = update_list(L)
    print("updating the list: ",updated_lst)

    print("extended list: ",extend_list(L))

    L.remove(L[2])
    print("using remove fun: ",L)

    L.insert(2,"hellll")
    print("inserted list: ",L)

    L.pop()
    print("popped from list:",L)

    print("revered list: ", reverse_list(L))


    index_list = L.index(3)
    print("index of 3: ",index_list)
    print(L)
  
    print("4 repeated ",  L.count(8)," times")

    L.clear()
    print("cleared list: ",L)

    L+[234,125,522]
    print(L)
    
# update
Lst = [1,3,4,56,4.6,8,9,6]
Print_list(Lst)






