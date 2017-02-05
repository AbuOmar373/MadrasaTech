def login():
    user=input("Enter a name: ")
    if user=='admin':
        print("winner")
    elif user=='zouhair':
        print("you are almos")
    else:
        print("Try again")
        login()

login()
