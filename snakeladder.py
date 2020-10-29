import random
import time as ti

def luck(x):
    inputt=[3,9,11,17,24,39,50,59,62,63,70,91,99]
    outputt=[22,34,49,90,94,96,12,19,38,81,47,64,5]
    if x in inputt:
        for i in range(len(inputt)):
            if(inputt[i]==x):
                x=outputt[i]
                break
    return x

def ludo(num):
    if num==1:
        print("----------")
        print("|        |")
        print("|    o   |")
        print("|        |")
        print("----------")
    if num==2:
        print("----------")
        print("|      o |")
        print("|        |")
        print("| o      |")
        print("----------")
    if num==3:
        print("----------")
        print("|      o |")
        print("|    o   |")
        print("| o      |")
        print("----------")
    if num==4:
        print("----------")
        print("| o    o |")
        print("|        |")
        print("| o    o |")
        print("----------")
    if num==5:
        print("----------")
        print("| o    o |")
        print("|    o   |")
        print("| o    o |")
        print("----------")
    if num==6:
        print("----------")
        print("| o    o |")
        print("| o    o |")
        print("| o    o |")
        print("----------")

def opening(x):
    val=0
    if x==1 or x==6:
        print("condition fulfilled here!")
        val=1
    return val

print("welcome!Try your(s) luck!")
n=input("Are you single?Play with your system. y/n\n")
if n.lower() not in ['y','n']:
    n=input("Enter y if you want to play with system otherwise n/n")
x,me,comp,flag=0,0,0,0
if n=='y':
    while flag==0:
     p=input("want to roll? Press y\n")
     if p.lower()!='y':
         p=input("Enter y to roll the dice")
     if p.lower()=='y':
        x=random.randint(1,6)
        if me==0:
         mee=opening(x)
        ludo(x)
        
        if mee!=0:
           if me+x<=100:
               me+=x
               me=luck(me)
           if me==100:
               flag=1
               print("You win!!\n**************************************\n")
               break
           print("you reach at position: ",me)
     print("Now system turn!")
     y=random.randint(1,6)
     if comp==0:
         compp=opening(y)
     ludo(y)
     if compp!=0:
           if comp+y<=100:
               comp+=y
               comp=luck(comp)
           if comp==100:
               flag=1
               print("oops!You loose!!\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
               break
           print("system has reached at position: ",comp)

ti.sleep(20)

               


