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
            print("You run into the trees and you find Rambo. You WIN!!!")
        elif q5 =="car":
            print("You enter in the car and the dragon put fire on it. You lose.")
        else:
            print("Not a valid option. You lose")
    else:
        print("Not a valid option. You lose")

elif answer == "right":
    q3 = input("You come to a bridge, it looks wobbly, do you want to cross it or head back?(cross/back) ").lower()

    if q3 == "back":
        print("You go back to the main road. And a car killed you.")
    elif q3 == "cross":
        q4 = input("You cross the bridge and meet a stranger. Do you want to talk to them?(yes/no) ")

        if q4 == "yes":
            print("You talk to the stranger and they give you gold. You WIN!!!")
        elif q4 == "no":
            print("You ignore the stranger and they are offended and you Lose!")
        else:
            print("Not a valid option. You lose")

    else:
        print("Not a valid option. You lose")

else:
    print("Not a valid option. You lose")

print("Thanks for trying", name, "! Good luck next time =)")
