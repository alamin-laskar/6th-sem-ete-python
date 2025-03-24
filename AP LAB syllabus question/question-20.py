# import random module and execute the following functions: 
# a. choice(arg) #arg can be list or tuple or string 
# b. randrange(start, stop, step) 
# c. random() 
# d. shuffle(list) 
# e. uniform(x, y) # output is a random number R, such that R is less than or equal to R and R is less than y. 
# f. randint(x, y) # generate a random number within the given range 

import random
def random_stuff():
    listt = [2,4,6,83,6,-1]
    random.shuffle(listt)
    print("rnadom choice : ",random.choice(listt))
    print("random range ",random.randrange(5,100))
    print("random value:",random.random())
    print("Shuffle: ",listt)


random_stuff()