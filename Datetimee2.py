from datetime import *

while True:
      dob = int(input("Enter the date of birth:"))

      today=datetime.today()
      year=today.year

      age=int(year)-int(dob)
      print("Your age is:",age)
