#ghost name

from random import randint

print(3*"\t","========>> لعبة الشبح <<==========")
brave=True
score=0

while brave:
      ghost_door=randint(1,3)
      print(3*"\t","ثلاثة ابواب أمامك...==> الشبح يختفي خلف أحدها")
      print(3*"\t","[+]أختر أحد الأبواب لفتحه[+]")
      door=input("أختر باب واحد من 1 إلى 3: ")
      door_num=int(door)
      if door_num==ghost_door:
            print(3*"\t","شبــــــــــح")
            brave=False
      else:
            print("لا يوجد شبح, رائع")
            print("أدخل غرفة أخرى")
            score=score+1

print("أهرب الشبح خلفك")
print("انتهت اللعبة! محولاتك الناجحة ",score)
