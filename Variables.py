print("What is your name?")
myName = input(">")
print(f"Welcome to the dungeon,{myName}!")
print("Do you go through the door 1 or door 2?")
door = input(">")
if door == "1":
    print("There is a nice vampire asking you if you enjoy life.")
    print(f"What do you do {myName} ?")
    print("1.Smile and nod")
    print("2.Scream and run")
    print(f"Are you sure that was right {myName} ?")
    answer = input(">")
    print("Go on be happy")
    vampire = input(">")

    if vampire == "1":
        print(f"Congratulations {myName}, you found a new friend!")
    elif vampire == "2":
        print(f"Sorry {myName} the vampire is faster. You become a dinner")
    else:
        print("The is the end of the line, Vampires are not so bad.")

elif door == "2":
    print("There is a nice vampire asking you if you enjoy life.")
    print(f"What do you do {myName} ?")
    print("1.Smile and nod")
    print("2.Scream and run")
    coffin = input(">")
    print ( f"Are you sure that was right {myName} ?")
    answer = input (">")
    print("Go on be happy.")

    if coffin == "1":
        print(f"Congratulations {myName}, you found a new friend!")
    elif coffin == "2":
        print("There is a brown teakwood coffin for you")
    else:
        print(f"The options are are just 1 or 2 {myName}")

else:
        print(f"{myName} you want many options, don't you?")