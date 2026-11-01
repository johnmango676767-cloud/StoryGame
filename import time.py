import time
import random
import math
mango = 0

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
    if mango == 0:
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
                print("You steal the gold but get caught doing so but you escape so your bounty increased which can cause you trouble later so be careful")
                print("+500 Bounty (Bad thing)")
                print("+500 Coins")
                coins = coins + 500
                bounty = 500
            choice4 = input("Now that you are free what do you do now? Raid a home(1), lay low for a little bit to calm down the hipe.")
            if choice4 == "1":
                print("You raid a home but its full of bandits so they steal half of your gold and you escape with your life!")
                coins = coins/2
            if choice4 == "2":
                print("You lay low and your bounty gets decreased by 300!")
                time.sleep(1.5)
                print("-300 Bounty(Good thing)")
                bounty = bounty-300
                time.sleep(3)
            print("A peasent walks up to you but you can clearly see through his disguies and find out he is a rich person")
            time.sleep(3)
            print("He asks do you want to gamble your coins off a coin flip? If you guess right you double your money if not I take half...")
            time.sleep(3)
            coinflip = random.choice(["Heads","Tails"])
            choice5 = input("Do you gamble it?(y/n)")
            if choice5 == "y":
                choice6 = input("Ok heads(1) or tails(2)?")
                if name1 == "Mohammed":
                    print("Oh your name is Mohammed, double gold and you skip the risk")
                    choice6 == 123456789
                    print("+Double Gold")
                    coins = coins*2
                elif choice6 == "1":
                    if coinflip == "Heads":
                        print("Oh you won... like I promised...")
                        time.sleep(2)
                        print("+Double Gold!")
                        coins = coins*2
                    elif coinflip == "Tails":
                        print("HA YOU LOST GIVEME HALF")
                        time.sleep(2)
                        print("-Half Gold")
                        coins = coins/2
                elif choice6 == "2":
                    if coinflip == "Tails":
                        print("Oh you won... like I promised...")
                        time.sleep(2)
                        print("+Double Gold!")
                        coins = coins*2
                    elif coinflip == "Heads":
                        print("HA YOU LOST GIVEME HALF")
                        time.sleep(2)
                        print("-Half Gold")
                        coins = coins/2
                elif choice6 == 123456789:
                    print("Ok goodbye sir enjoy your money")
                elif choice5 == "n":
                    print("Umm I guess goodbye!")


        elif choice1 == "2":
            print("Nice to see you are going the right way here is a sword to help you and some coins \n+100 coins\n+iron sword")
            ironsword = 1
            coins = 100

        else:
            print("Uhh u didnn't write the right thing so, uhh restart next time do well")
        choice7 = input("He walks away and you can steal from him(1), or you can just walk away(2)")
        if choice7 == "1":
            print("You try to steal from him but he hits your head with a stick and now you have a concussion!")
            print("Even worse the officers found you and you are forced out of three options!(For you fighting doesn't work because you are concussed)")
        elif choice7 == "2":
            print("You dont steal and officers found you and surrond you and you have three options!")
        if choice7 == "1":
            choice8 = input("Do you use a whistle thats in your bag(1) or do you just run(2)")
        elif choice7 == "2":
            choice8 = input("Do you fight(1), use a whistle in your bad(2), or just run(3)")
            if choice8 == "1":
                print("You fight them, you are one great dark knight and take them down but your bounty is emmense now but so is your gold!")
                print("+2500 Bounty")
                print("+1250 Gold")
                bounty = bounty + 2500
                coins = coins + 1250
            if choice8 == "2":
                if noblehorse == "1":
                    print("You call your horse using your whistle and leave unschated!")
                if noblehorse != "1":
                    print("You use the whistle but you dont have a horse so you get beat up and have to pay bail")
                    print("-500 coins")
            if choice8 == "3":
                print("You run but drop some gold to run faster so you lose some")
                print("-200 coins")
                coins = coins - 200
            print("A blacksmith walks up to you and offers you a deal, make a great distraction while he smuggles stuff for a reward")
            time.sleep(3)
            choice9 = input("Do you accept it? (y/n)")
            if choice9 == "y":
                print("You call your horse over and start breaking things in the street causing your bounty to go up")
                print("+300 bounty")
                bounty = bounty + 300
                time.sleep(3)
                choice10 = ("For this he offers you a great black knight suit of armor for half off(500 coins now)Do you take it? (y/n)")
                if choice10 == "y":
                    print("Ok here you go, thanks for your services")
                    print("-500 coins")
                    print("+Black Knight Suit")
                    coins = coins - 500
                    blacksuit = 1
                if choice10 == "n":
                    print("Ahhhh I guess man, heres 300 coins as payment though")
                    print("+300 coins")
                    coins = coins + 300
                print("The night comes over and you rent a apartment for 400 coins, a small room")
                print("-400 Coins")
                coins = coins - 400
                print("*Showing Stats*")
                time.sleep(3)
                print("Coins: " + str(coins))
                print("Bounty: " + str(bounty))
                if noblehorse == "1":
                    print("Noble Horse: " + str(noblehorse))
                if blacksuit == "1":
                    print("Knight Black Suit: " + str(blacksuit))
                
                time.sleep(3)
                if blacksuit == "1":
                    if diamondsword == "1":
                        print("You leave your blacksuit behind along with your diamond sword in your apartment for later")
                    elif ironsword == "1":
                        print("You leave your blacksuit behind along with your iron sword in your apartment for later")
                    else:
                        print("You leave your blacksuit behind in your apartment for later")
                else:
                    print("You leave your apartment to the outside")
                print("What do you want to do now?")
                time.sleep(3)
                choice11 = input("Get a meal(1), Go feed your horse(2), Go back into your apartment to lay low more POTENITALLY(3)")
                if choice11 == "1":
                    print("You go to get a meal pay 5 coins but your full so you filled prepared for battle")
                    print("-5 coins")
                    coins = coins - 5
                if choice11 == "2":
                    print("You feed your horse, its happy and you get blessed with 300 coins from the sky don't ask how be happy")
                    time.sleep(3)
                    print("+300 Coins")
                    coins = coins + 300
                if choice11 == "3":
                    laylow1 = random.choice([1,2])
                    if laylow1 == "1":
                        print("You lay low and lose 200 bounty(Chance btw)")
                        time.sleep(3)
                        print("-200 bounty")
                    if laylow1 == "2":
                        print("You laylow and just laylown bounty change(Chance btw)")
                


                