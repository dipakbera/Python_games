import random
from itertools import combinations
def toc():
 turns,flagg=1,0
 w=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
 me=[]
 comp=[]
 total=list(range(1,10))

 l1=[" "," "," ","|"," "," "," ","|"," "," "," "]
 l2=["-"," ","-"," ","-"," ","-"," ","-"," ","-"]
 l3=[" "," "," ","|"," "," "," ","|"," "," "," "]
 l4=["-"," ","-"," ","-"," ","-"," ","-"," ","-"]
 l5=[" "," "," ","|"," "," "," ","|"," "," "," "]

 def board():
    print("")
    print("".join(l1))
    print("".join(l2))
    print("".join(l3))
    print("".join(l4))
    print("".join(l5))

 board()
 def placing(x,sign):
  if(x==1):
     l1[1]=sign
  if(x==4):
     l3[1]=sign
  if(x==7):
     l5[1]=sign
  if(x==2): 
     l1[5]=sign
  if(x==5):
     l3[5]=sign
  if(x==8):
     l5[5]=sign
  if(x==3):
     l1[9]=sign
  if x==6:
     l3[9]=sign
  if x==9:
     l5[9]=sign
 def resultf():
     placing(x,'X')
     placing(y,'O')
     board()

 while turns<5:
  flag=0
  x=int(input("\nplace your 'X' in position within {}\n".format(total)))
  if x not in total:
     print("please place correctly!")
     x=int(input("place your 'X' in position within {}\n".format(total)))
  total.remove(x)
  me.append(x)
  if turns>=3:
     comb1=list(set(combinations(me,3)))
     for i in range(len(comb1)):
            comb1[i]=sorted(comb1[i])
            if comb1[i] in w:
                print("\n**********You win!**********")
                flagg=1
                break
     if(flagg!=0):
             print("your last turn in board was:")
             resultf()
             break
  if turns==2:
    for k in total:
        me.append(k)
        if sorted(me) in w:
            y=k
            flag=1
            me.remove(k)
            break
        me.remove(k)
   
  if turns>2:
       for k in total:
         comp.append(k)       
         comb3=list(set(combinations(comp,3)))        
         for i in range(len(comb3)):
                comb3[i]=sorted(comb3[i])
                if comb3[i] in w:
                    y=k
                    flag=2
                    comp.remove(k)
                    break
         if(flag==2): 
             break
         comp.remove(k)
       if(flag==0):
            for k in total:
               me.append(k)
               comb4=list(set(combinations(me,3)))
               for i in range(len(comb4)):
                 comb4[i]=sorted(comb4[i])
                 if comb4[i] in w:
                     y=k
                     flag=1
                     me.remove(k)
                     break 
               if(flag!=0):
                    break
               me.remove(k)
       
  if(flag==0):
     y=random.choice(total)
  print("System has placed 'O' in position {}".format(y))
  total.remove(y)
  comp.append(y)
     
  if(turns>=3 and flagg==0):
         comb2=list(set(combinations(comp,3)))
         for i in range(len(comb2)):
            comb2[i]=sorted(comb2[i])
            if comb2[i] in w:
                print("@@@@@@@@!!You loose!!@@@@@@@")
                flagg=2
                break
         if(flagg!=0):
            print("This happens as:")
            resultf()
            break
  resultf() 
  turns+=1

 if turns==5 and flagg==0:
    print("This is the last chance!what will be your luck....")
    print("Ok!calm.I will place your 'X' last position in > {}".format(total[0]))
    x=total[0]
    me.append(x)
    comb6=list(combinations(me,3))
    for i in range(len(comb6)):
            comb6[i]=sorted(comb6[i])
            if comb6[i] in w:
                print("\n**********wow!Lastly you win!**********\n")
                print("The board becomes:")
                resultf()
                flagg=3
                break

 if(flagg==0):
    print("\n!!!!!!!!Oops!There is a Tie.None win.!!!!!!!")
    print("This happens as the board becomes:")
    resultf()
 return

print("Hi!Guest,welcome to the Tic-Tac-Toe Game")
mood='y'
while(mood.lower()=='y'):
    toc()
    mood=input("\nEnjoying!Are you want to play again? y/n\n")
    if mood.lower() not in ['y','n']:
        mood=input("Enter y to play or n not to play\n") 
    if mood.lower()=='n':
        print("sorry!I am unable to catch up your mood now.\n")
        break
