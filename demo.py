import random
num1=random.randint(1,9) 
count=0
while (count<5):
  num=int(input("enter the number between1-9"))
  if(num1==num):
      print ("YOU WON")
      break
  else:
      print ("try again")
  count=count+1 