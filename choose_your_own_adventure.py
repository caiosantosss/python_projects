name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    q2 = input("You come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim accross: ").lower()

    if q2 == "swim":
        print("You swam accross and were eaten by an alligator.")
    elif q2 == "walk":
        q5 = input("You walked for many miles, and you see a dragon flying. Do you want to run for the trees or enter an abandoned car? (run/car)")

        if q5 == "run":
            q6 = input("You run into the trees and you find Rambo. But he ask you if you want the knife or the gun.(knife/gun)").lower()

            if q6 == "knife":
                print("Rambo teach you how to use a knife. You run to the dragon and you throw the knife into his heart. You WIN!")
            elif q6 =="gun":
                print("You take the gun, the gun is without ammo and you die.")
            else:
                print("Not a valid option. You lose")

        elif q5 =="car":
            print("You enter in the car and the dragon put fire on it. You lose.")
        else:
            print("Not a valid option. You lose")
    else:
        print("Not a valid option. You lose")

elif answer == "right":
    q3 = input("You come to a bridge, it looks wobbly, do you want to cross it or head back?(cross/back) ").lower()

    if q3 == "back":
        print("You go back to the main road. And a car killed you. You lose!")
    elif q3 == "cross":
        q4 = input("You cross the bridge and meet a stranger. Do you want to talk to them?(yes/no) ")

        if q4 == "yes":
            print("You talk to the stranger and they give you gold. You WIN!!!")
        elif q4 == "no":
            q7 = input("You ignore the stranger and you find a mage! The mage talk with you asking if you want fire or ice? ").lower()

            if q7 == "fire":
                print("The mage make a fire magic and turn you rich, You win!")
            elif q7 =="ice":
                print("The mage frozen you. You lost.")
            else:
                print("Not a valid option. You lose")
        else:
            print("Not a valid option. You lose")

    else:
        print("Not a valid option. You lose")

else:
    print("Not a valid option. You lose")

print("Thanks for trying", name, "! Good luck next time =)")
