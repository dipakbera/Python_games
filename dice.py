print("welcome!")
import random
mood='y'
while mood=='y':
    num=random.randint(1,6)
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
    mood=input("Press y to roll again,press any key to stop\n")
print("\nThanks!Hope you enjoyed!........\n")