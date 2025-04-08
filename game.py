import random


def stringOut():
 guess=int(input("enter a number:").strip())
 rand=random.randrange(0,11)
 count=0

 while guess!=rand:
   if guess < 0 or guess > 10:
    return 0
   if guess+3<=rand:
     print("you are way to down")
     count+=1
     guess=int(input("try again:").strip())
   elif guess-3>=rand:
       print("you are way to up")
       count+=1
       guess = int(input("try again:").strip())
   else:
    count+=1
    print("you are close")
    guess = int(input("try again:").strip())




 count+=1
 print(f"yeeey you got it in {count} try ")







stringOut()

