file2=open("password.txt", 'r') #read
data=file2.read()
for i in data:
      print(i,end='')  # end='' لكتابة حروف الكلمة في سطر واحد
file2.close()
