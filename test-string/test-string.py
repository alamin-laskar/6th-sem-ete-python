def call():
    text = "Hello, BVEC"
    print("Uppercase:", text.upper())      # Convert to uppercase
    print("Lowercase:", text.lower())      # Convert to lowercase
    print("Length:", len(text))            # Get length of string
    print("Substring:", text[0:5])         # Extract substring
    print("Reversed:", text[::-1])         # Reverse the string

    for i in text:
        print(i)


    text1 = "welcome to rasplandor"
    print(text+" "+text1)

    print(text1.capitalize())
    print(text1*3)
    print(text1.startswith("to"))
    print(text1.endswith("rasplandor"))
    print(text1.replace("rasplandor","BVEC"))
    print(text1.split(" "))
    print(text1.find("from"))
    print(text1.strip())


    words = ["hello", "world"]
    print("".join(words))  
    print(text.title())
    

    digit = "12345"
    print(digit.isdigit())  
    print("123abc".isdigit()) 
    print(text1.isalpha()) 
    alpha_num = "hello1234"
    print(alpha_num.isalpha())


    SPACE = "  "
    print(SPACE.isspace())
    test_txt = "ankara messi suiooooo"
    print(test_txt.isspace())

    print(test_txt.count())

call()






# capitalize
# replication
# startswith()
# endswith()
# replace()
# split()
# find()
# strip()
# join()
# title()
# isdigit()
# isalpha()
# isspace()
 