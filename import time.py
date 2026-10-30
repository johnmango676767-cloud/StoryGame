import time
print("Welcome to the story game!")
time.sleep(3)
print("Now choose the story you want to listen to! The Dark Knight(1)\n Thats all the options!")
time.sleep(3)
story = input(" ")
print("TRANSITIONING NOW TO STORY CHOSEN")
time.sleep(5)
if story == "1":
    print("STARTING STORY \"THE DARK KNIGHT\"")
    time.sleep(3)
    print("The things that you do in this game give coins you can play against friends to see who gets a higher score which is your networth!")
    time.sleep(3)
    name1 = input("What is your name?: ")
    if name1 == "Mohammed":
        print("Wow best name of all time litteraly the perfect name, the best in fact")
    else:
        print("Well welcome warrior what path do you want to go?")
        time.sleep(3)
        choice1 = input("The Dark Side(1) or the Good Side(2)?")
        if choice1 == "1":
            print("Well, Well, Well your intresting BUT I CANT LET YOU BE THE DARK SIDE")
            time.sleep(3)
            choice2 = input("FIGHT attack first(1) or defend(2)")
            if choice2 == "1":
                print("You attack first which knocks the guy out and you steal his diamond sword and 300 coins but you must escape soon before you get caught!")
                time.sleep(3)
                print("+300 coints\n+diamond sword")
                coins = 300
                diamondsword = 1
            if choice2 == "2":
                print("You block, counter attack and and you steal his 300 coins but you must escape soon before you get caught!")
                time.sleep(3)
                print("+300 coins")
                coins = 300
            print("(You are forced to flee and stumble upon a great german black horse)")
            choice3 = input("Do you steal it(1), or do you run off without it to go get some gold(2)?")
            if choice3 == "1":
                print("You now have a noble horse! But it belonged to a milltary officer and now a fleet is running after you but you manage to escape them, your bounty is increased be careful if its too high it could cause trouble!")
                bounty = 1000
                noblehorse = 1
                print("+1000 Bounty (Bad thing)")
                time.sleep(5)
            if choice3 == "2":
                print("You steal the gold but get caught doing so but you escape so your bounty increased which can cause you trouble later")
                print("+500 Bounty (Bad thing)")
                print("+500 Coins")
                coins = coins + 500
                bounty = 500
            print("Now that you are free what do you do now? Raid a home(1), lay low for a little bit to calm down the hipe.")
        elif choice1 == "2":
            print("Nice to see you are going the right way here is a sword to help you and some coins \n+100 coins\n+iron sword")
            ironsword = 1
            coins = 100

        else:
            print("Uhh u didnn't write the right thing so, uhh restart next time do well")
        