import time as ti
print("Welcome!\n")
import datetime
print("Enter your birthday in the format like YYYY/MM/DD (as an example 1998/03/06)")
print("[Give input 0 before date and month if it is single digit e.g. month march as 03 or date 8 as 08]\n") 
def check():
    x=input()
    x=str(x)
    try:
       y=int(x[:4])
       if int(x[5])==0:
          m=int(x[6])
       else:
         m=int(x[5:7])
       if int(x[8])==0:
         d=int(x[9])
       else:
         d=int(x[8:])
       p=datetime.datetime(y,m,d)
       print("Congrats!you born on {}.\n".format(p.strftime("%A")))
    except ValueError:
        print("please try in specified format YYYY/MM/DD")
        check()

check()
while True:
   p=input('Do you want to check another? Press y/n\n')
   if p == 'y':
       print("Enter the new one!\n")
       check()
   else:
         break
ti.sleep(10)
