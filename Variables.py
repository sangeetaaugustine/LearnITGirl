print("Welcome to the dungeon!")
print("Do you go through the door 1 or door 2?")
door = input(">")
if door == "1":
    print("There is a nice vampire asking you if you enjoy life.")
    print("What do you do?")
    print("1.Smile and nod")
    print("2.Scream and run")
    vampire = input(">")

    if vampire == "1":
        print("Congratulations, you found a new friend!")
    elif vampire == "2":
        print("Sorry the vampire is faster.You become a dinner")
    else:
        print("The is the end of the line, Vampires are not so bad?")

elif door == "2":
    print("There is a nice vampire asking you if you enjoy life.")
    print("What do you do?")
    print("1.Smile and nod")
    print("2.Scream and run")
    coffin = input(">")

    if coffin == "1":
        print("Congratulations, you found a new friend!")
    elif coffin == "2":
        print("There is a brown teakwood coffin for you")
    else:
        print("The options are are just 1 or 2 my friend")

else:
        print("You want many options, do you?")