name=input("enter your name:")
print("Hello",name,"welcome to the path waygame .")
answer=input("This has to be end enter whether you want to go left/right or back:").lower()
if answer=="left":
    answer=input("you came to a river you have to decide now whether you have to cross or go back")
    if answer=="cross":
            print("the river is so deep you fell into the river and lost")
            quit()
    elif answer=="back":
            print("you went back and lost the game")
            quit()
    else:
            print("invalid option you lost")
            quit()
elif answer=="right":
         answer=input("you came near a bridge now do yo want to walk on the bridge or cross the bridge ")
         if answer=="walk":
             print("you have walked many miles and you lost the game")
             quit()
         elif answer=="cross":
             answer=input("you are going to meet a stranger now do you want to meet him yes/no")
             if answer=="yes":
                 print("you met a stranger and he gave you gold you won the game")
                 quit()
             elif answer=="no":
                 print("you didn't meet the stranger you lost ")
                 quit()
             else:
                 print("invalid answert you loss the game")
                 quit()
else:
        print("you go back and lost the game")
print("thank you for playing",name)
