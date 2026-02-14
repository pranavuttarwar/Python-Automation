inp = int(input("Enter your value: "))

match inp:
    case 1:
        print("Today is Mon")
    case 2:
        print("Today is Tue")
    case 3:
        print("Today is Wed")
    case 4:
        print("Today is Thu")
    case 5:
        print("Today is Fri")
    case 6:
        print("Today is Sat")
    case 7:
        print("Today is Sun")
    case _:
        print("Invalid Input give input from 1 to 7")