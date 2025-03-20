fruits = ["Alamin", "noor", "protin"] #homogineous list

fruits.append("Orange")  # Add item
print("Fruits:", fruits)
fruits.remove("noor")  # Remove item
print("Fruits:", fruits)
fruits[0] = "Mango"      # Modify item
print("Fruits:", fruits)
print("First Fruit:", fruits[0])
print("Last Fruit:", fruits[-1])  # -ve sign denotes that it starting from end


#heterogenious list

L=[1,2,3.5,"hi","BVEC"]

print(L)

L.append("ALAMIN")
print(L)


print("list Lenght: ",len(L))
L.extend(["nigga","why nigga"])
print("\nextended list: ",L)

L.insert(2,"hellll")

print("inserted list: ",L)

L.remove(L[4])
print("4th pos removed: ",L)


# tuple -->faster than list

T = (1,2,3,"hello","brothaa")
print(T[3])

# unpacking of tuple
# slice[start:stop:step]
T2 = T[0:3]
print(T2)
T3 = T[-3:-1]
print(T3)

# def extend_list(T):
#     T.extend(["hi","hello"])
#     return T

def reverse_list(T):
    T.reverse()
    return T
def update_list(T):
    # value = int(input("Enter a value to update the list: "))
    # T.append(value)
    return T
def Print_list(T):
    print("printing 0th element",T[0])
    print("printing upto 5th element",T[1:5])
    print("printing the whole list ",T[:])
    print("printing the list alternatively ",T[::2])
    print("printing from th end",T[-1])
    print("printing  with -ve argument ",T[-5:])

    print("length pf the list: ",len(T))

    updated_tpl = update_list(T)
    print("updating the list: ",updated_tpl)

    # print("extended list: ",extend_list(T))

    # T.remove(T[2])
    print("using remove fun: ",T)

    # T.insert(2,"hellll")
    print("inserted list: ",T)

    # T.pop()
    print("popped from list:",T)

    # print("revered list: ", reverse_list(T))


    index_list = T.index(3)
    print("index of 3: ",index_list)
    print(T)
  
    print("4 repeated ",  T.count(8)," times")

    # T.clear()
    print("cleared list: ",T)

    # T+[234,125,522]
    print(T)
    
# update
tpl = (1,3,4,56,4.6,8,9,6)
Print_list(tpl)







# how to find a dictionary in 
