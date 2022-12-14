name=input("type your name : ")
print("Welcome ",name," to this adventure!")
answer=input("You are a dirt road, it has come to an end and you can go 'left' or 'right'. Which way would you like to go? : ").lower()
if answer=="left":
    answer=input("You come to a river, you can walk around it or swim across? type 'walk' to walk around and 'swim' if you want to swimcross : ")
    if answer=="swim":
        print("You swam across the river and were eaten by an alligater, YOU LOSE!")
    elif answer=="walk":
        print("You walked miles,ran out of water and YOU LOSE!.")
    else:
        print("Not a valid option. You LOSE!")
elif answer=="right":
    answer=input("You came across a bridge, it looks wobbly, do you want to 'cross' it or head 'back' (cross/back)? : ")
    if answer=="back":
        print("You go back and  YOU LOSE!")
    elif answer=="cross":
        answer=input("You cross the bridge and met a stranger. Do you want to talk to him(yes / no) : ")
        if answer=="yes":
            print("You talk to the stranger and they gift you the treasure. YOU WON!!!!")
        elif answer=="no":
            print("You ignore the stranger and they get offended and YOU LOSE!")
        else:
            print("invalid option YOU LOSE!")
    else:
        print("invalid option YOU LOSE!")
else:
    print("invalid option YOU LOSE!")
print("THANK YOU FOR TRYING !!! ",name)
