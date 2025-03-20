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

    print("capitalize:",text1.capitalize())
    print("replicate: ",text1*3)
    print("startswith: ",text1.startswith("to"))
    print("endswith:",text1.endswith("rasplandor"))
    print("replace: ",text1.replace("rasplandor","BVEC"))
    print("split: ",text1.split())
    print("find:",text1.find("from"))
    print("strip:",text1.strip())


    words = ["hello", "world"]
    print("join:","".join(words))  
    print("title: ",text.title())
    

    digit = "12345"
    print("isdigit: ", digit.isdigit())  
    print("isdigit: ","123abc".isdigit()) 
    print("isalpha: ",text1.isalpha()) 
    alpha_num = "hello1234"
    print("isalpha: ",alpha_num.isalpha())


    SPACE = "  "
    print("ispace: ",SPACE.isspace())
    test_txt = "ankara messi ankara messi ankara messi suiooooo"
    print("ispace: ",test_txt.isspace())

    print("count messi:  ",test_txt.count("messi"))

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
 