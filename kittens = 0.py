#Each time you input 'y', it gives you the number of kitten who have attempted world domination.
#A 'n' response will print out 'The world is safe ... for now'
kittens = 0
question = input("Has a kitten attempted to take over the world?(y/n) ")

if question == "y":
        kittens += 1
        print(f"{kittens} have attempted world domination")
    
elif question != "n":
        print("Invalid Input")
        print("Please enter either y or n")
question = input("Has another kitten attempted to take over the world?(y/n) ")
if question == "n":
    print("The world is safe ... for now")
