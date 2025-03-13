#  Write a program to print the days of the week using nested if. (eg. If 1, print Monday, 2, Tuesday……etc.)


def printday(day):
    if day == 1:
        print("Monday")
    else:
        if day == 2:
            print("Tuesday")
        else:
            if day == 3:
                print("Wednesday")
            else:
                if day == 4:
                    print("Thursday")
                else:
                    if day == 5:
                        print("Friday")
                    else:
                        if day == 6:
                            print("Saturday")
                        else:
                            if day == 7:
                                print("Sunday")
                            else:
                                print("Invalid input! Please enter a number between 1 and 7.")


def get_value():
    day = int(input("Enter the number of the day "))
    printday(day)
get_value()