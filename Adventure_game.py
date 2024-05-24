name = input("Type your name: ").title()
print(f"Welcome {name} to this adverture!")

answer = input("You are on a dirt road, it has come to an end and you can do left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = left == input("you have come to a river, you can walk around it or swim across? Type walk to walk around it or swim to swim across: ").lower()
    if left == "swim":
        print("You swam across and were eaten by an alligator. You lose!")
    elif left == "walk":
        print("You walked for many miles and run out of water. You lose!")
    else:
        print("Not a valid option. You lose!")
elif answer == "right":
    right = input("You come to a bridge, it looks creepy. Do you want to cross it or head back?(cross/back) ").lower()
    if right == "back":
        print("You back and lose")
    elif right == "walk":
        bridge = input("You cross the bridge and meet a stranger. Do you want to talk to them?(yes/no) ").lower()
        if bridge == "yes":
            print("You talk to the stranger and he gave you Gold. You Win!")
        elif bridge == "no":
            print("You ignore the stranger and he is offended. You lose!")
        else:
            print("Not a valid option. You lose!")

    else:
        print("Not a valid option. You lose!")
else:
    print("Not a valid option. You lose!")
print(f"Thanks for playing {name}.")