def mix():
    print ("Search for cup")
    print ("Put Hot Water")
    print ("Put Suqar")
    print ("Use Spoon")

def make_coffee():
    mix()
    print ("Drink coffee")

def make_chocolate():
    mix()
    print ("Drink chocolate")

wake_up = input("Enter you name: ")

if (wake_up == "zoo"):
    make_chocolate()

elif wake_up == "ahh":
    make_coffee()

else:
    print ("Please drink waater")
