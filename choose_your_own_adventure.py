name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    q2 = input("You come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim accross: ").lower()

    if q2 == "swim":
        print("You swam accross and were eaten by an alligator.")
    elif q2 == "walk":
        print("You walked fot many miles, ran out of water and you lost the game")
    else:
        print("Not a valid option. You lose")

elif answer == "right":
    q1 == input("You come to a bridge, it looks wobbly, do you want to cross it or head back?(cross/back) ").lower()

    if q2 == "back":
        print("You go back to the main road. And a car killed you.")
    elif q2 == "cross":
        print("You cross the bridge and meet a stranger. Do you want to talk to them?(yes/no) ")

        if q2 == "yes":
            print("You swam accross and were eaten by an alligator.")
        elif q2 == "no":
            print("You walked fot many miles, ran out of water and you lost the game")
        else:
            print("Not a valid option. You lose")

    else:
        print("Not a valid option. You lose")

else:
    print("Not a valid option. You lose")
