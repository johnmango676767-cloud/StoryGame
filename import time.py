import time
import random
import math
mango = 0
noblehorse = 0
coins = 0
bounty = 0
diamondsword = 0
ironsword = 0
blacksuit = 0
train = 0
print("Welcome to the story game!")
time.sleep(3)
story = input("Now choose the story you want to listen to! The Dark Knight(1) Thats all the options! Choose: ")
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
        if choice1 == "2":
            print("Nice man there is a current Great White Knight already maybe one day you can be up to his strength! After all he is the strongest to have held the title so that is probably never going to happen")
            time.sleep(3)
            print("Here is some gold and a sword!")
            print("+300 Coins")
            print("+Iron Sword")
            coins = 300
            ironsword = 1
            choice1 = input("What do you want to do? Do a job for money(1), or do you patrol and try to help people(2)")
            if choice1 == "1":
                print("You go around and do jobs for money!")
                print("+300 Coins")
                coins = coins + 300
            if choice1 == "2":
                print("You help people around and they pay you out of graditude!")  
                print("+500 Coins")
                coins = coins + 500
            print("You are walking down the street and see someone getting robbed, you can pottenitally get robbed also what do you do")   
            choice2 = input("Do you help them(1), or watch(2)") 
            if choice2 == "1":
                chance1 = random.choice([1,2])
                if chance1 == 1:
                    print("You help defeat the bandint and the victim pays you lots of money")
                    print("+600 Coins")
                    coins = coins + 600
                if chance1 == 2:
                    print("You try and help defeat the bandint but he runs away so you don't catch him but the victim still pays you for trying and at least saving their money and life")
                    print("+300 Coins")
                    coins = coins + 300
            if choice2 == "2":
                print("You watch and get nothing out of it...You aren't doing well so far")
            print("You walk the streets thinking about what you have done so far and what you can do")
            time.sleep(3)
            choice3 = input("You walk into a store you can either work for them(1) or just buy some stuff and go home(2)")
            if choice3 == "1":
                print("You get a job for them and get some coins but the day is almost over so you head home")
                print("+300 Coins")
                coins = coins + 300
            if choice3 == "2":
                print("You buy some stuff and go back to your little apartment")
            time.sleep(3)
            print("As you are about to go to sleep you decide not to and you get up and go ouside")
            time.sleep(3)
            choice4 = input("You see a hideout for some bandits do you enter?(y/n)")
            if choice4 == "y":
                print("You enter the hideout and they seem not to notice you")
                time.sleep(3)
                print("Bandint1: Ooof that one guy beat me up badly I didn't get anything today")
                time.sleep(3)
                print("(Thats the bandint that you saw steal from someone)")
                time.sleep(3)
                print("Bandint2: I got a get amount of couns today look") 
                time.sleep(3)
                print("(He puts a massive bag of gold on the table)")
                time.sleep(3)
                print("Bandint1: Wow lets get some food then")
                choice5 = input("Do you attack now or no?(y/n)")
                if choice5 == "y":
                    print("You attack and handle both bandints then you tie them up and yell for cops to come before you leave")
                    time.sleep(3)
                    print("You grab the gold that they stole and leave it there")
                    time.sleep(3)
                    print("Turns out someone watched you do the entire thing and gave you gold for taking care of them!")
                    print("+500 coins")
                    coins = coins + 500
                if choice5 == "n":
                    print("You decide not to and they see you and decide to jump you")
                    time.sleep(3)
                    print("You fight them off and tie them up call officers by yelling and walk away")
                    time.sleep(3)
                    print("You go back to your house and actually sleep ending Day 1")
                    print("*Stats Showing*")
                    print("Coins: " + coins)
                    print("Ironsword: " + ironsword)
                    print("Day 2 Starting")
                    time.sleep(3)
                    print("You wake up with your body slightly injured from yesterdays incounter and decide to get some breakfast")
                    time.sleep(3)
                    print("You walk into the store hoping for a break but the world does not provide and you see bandints robbing the place")
                    time.sleep(3)
                    print("Bandint: Hurry up give me all the coins that you have or get stabbed!")
                    time.sleep(3)
                    print("Shop Owner: Ok ok I'm going as fast as I can please dont do anything")
                    time.sleep(3)
                    choice6 = input("Do you attack the bandints(1) or wait for a pottenitaly better oppetunity(2)?")
                    if choice6 == "1":
                        print("You attack the bandints taking injury but eventually defeating them and coming out on top")
                        time.sleep(3)
                        print("Show Owner: Thank you, I am very grateful here take some coins that you saved!")
                        print("+500 Coins")
                        coins = coins + 500
                    if choice6 == "2":
                        print("You wait for a better opptunity but it doesnt come and you are forced to attack and the shop owner gets injured but you still win")
                        time.sleep(3)
                        print("Shop Owner: Thanks for saving me but what took you o like to strike anyways heres some coins")
                        print("+250 Coins")
                        coins = coins + 250
                        time.sleep(3)
                        print("You also get breakfast for free and enjoy your meal which is one of the best things youv'e ever tasted")
                        time.sleep(3)
                        print("You finish your meal and walk out satifieed but slightly injured")
                        choice7 = input("You can choose do you want to do you want to go to your job(1), or rest to heal your injuries(2)")
                        if choice7 == "1":
                            print("You still go to your job and your injuries dont heal but you get gold")
                            print("+300 Coins")
                            coins = coins + 300
                            injuries = 1
                        if choice7 == "2":
                            print("You stay at home and rest to heal your injuries")
                            injuriesgone = 1
                        print("You are in your apartment then you hear a big BOOM somone is knocking down your door!")
                        time.sleep(3)
                        print("Bandints rush through your door attempting to get revenge after what you did last night")
                        time.sleep(3)
                        input("Do you attack the one to the left(1), middle(2), or right(3) first?")
                        chance2 = random.choice([1,2,3])
                        if chance2 == 1:
                            print("You attack that person and easily defeat them and continue to destroy the rest ")
                        if chance2 == 2:
                            if injuries == 1:
                                print("You attack that person but you had previous injuries so you fight a tough battle but one escapes with some of your money")
                                print("-300 Coins")
                                coins = coins - 300
                            if injuriesgone == 1:
                                print("You attack that person, he was tought but you had rested earlier so you take out the rest and win the battle")
                        if chance2 == 3:
                            print("You fight that person but they are strong so you handle 2 of them while the third runs off with some of your money")
                            print("-300 Coins")
                            coins = coins - 300
                        print("You take the people you captured to the officers and they take them away and you go back into your apartment to finnaly sleep wondering when will ever get a chance to rest")
                        time.sleep(5)
                        print("(Day 2 ended)")
                        time.sleep(3)
                        print("*Stats Showing*")
                        print("Coins: " + coins)
                        print("Bounty: " + bounty)
                        print("Iron Sword: " + ironsword)
                        time.sleep(10)
                        print("Day 3 Starting")
                        time.sleep(3)
                        print("You wake up and hope that you finnaly get a break today")
                        time.sleep(3)
                        choice8 = input("Do you even want a break?")
                        print("Intresting... Anyways")
                        time.sleep(3)
                        print("You go outside to the same store where the bandints were and everything was fine")
                        time.sleep(3)
                        print("You sit down and order some food, still free as the owner is grateful for you")
                        time.sleep(3)
                        print("You decide to go to your job but only a half shift so you still have time in the day")
                        print("+150 Coins")
                        coins = coins + 350
                        choice9 = input("What do you want to do for the rest of the day? Training(1), Rest(2), Stop bandints(3), make the job a full shift(4)")
                        if choice9 == "1":
                            print("You train and get stronger for future fights as maybe potttenialy one might come soon")
                            train = 1
                        if choice9 == "2":
                            print("You rest which prepares you for future fights")
                            rest = 1
                        if choice9 == "3":
                            print("You go out and stop stop bandints")
                            time.sleep(3)
                            print("You get gold for doing so!")
                            time.sleep(3)
                            print("+350 Gold")
                        if choice9 == "4":
                            print("You go to your job again")
                            print("+150 Coins")
                            coins = coins + 150
                        print("The day is ending but as you are wallking home someone is handing out news papers with everyone on the street in panic and shock")
                        time.sleep(3)
                        print("You take it and start reading the newspaper")
                        time.sleep(3)
                        print("\"In the royal arena today the Dark Knight defeated the Great White Knight stripping him of all his power and making him go into hiding out of shame\"")
                        time.sleep(4)
                        print("\"This means that the Great White Knight family hertiage is now gone and we no longer have one till one comes up that can yiled his armor and tools\"")
                        time.sleep(4)
                        print("\"The Dark Knight said and we quote \"I need a worthy opponent NOW or I go on a rampage...\"")
                        time.sleep(3)
                        print("\"Is it wraps for a man when he is gone\"")
                        time.sleep(3)
                        print("I code and code and code and code and i feel exhausted I say to my self \"Does it get better the other way\"")
                        time.sleep(3)
                        print("In ways I say my self In some ways good or bad its lowkey bad tho")
                        time.sleep(3)
                        print("Ifone tyhings provides then I will indeed be a free free man who knows does he tho I dont know ho ho")
                        time.sleep(3)
                        print("I say to my self all that can be done is pray with haste as god will provide everyday and hopefully truely today...")
                        time.sleep(3)
                        print("Can this be done I say with a glee maybe actually the day is almost done and if I just hold on we can be free! IF i can IF i can IF i can")
                        time.sleep(3)
                        print("Can a man beg for extension when he says tmrw man will be a day a day of intriguing days and hard ships as a man learns from heartbreak")
                        time.sleep(3)
                        print("Everyday a mans heart goes to hay his heart his broken his purpose is shattered for what a man says then they say \"Just not to ruin MY day\"")
                        time.sleep(3)
                        print("Fill with heartbreak a man will never wish on his dearest he has 3 minuites to spare and say he is saying random stuff today! if and only if a man had stayed awake to prevent heartbreak tmrw tmrw hey hey hey this is amazing for today is this a good thing or a bad is this a gift that they people gave is this earth helping me out today or is this a punishment for the days that I went into hay...")
                        time.sleep(3)
                        print("My last wish today is taht if its really $5 I will be the happiest man alive to have seen the day")
                        time.sleep(3)
                        print("People see my speech and say this is fake time to deflate! I say this is my heart they say I dont have one for me or you or the world, ten We say out of gratuied thank you for the ooppruinty u have brought on to me today as I work day anda day for hope that goes straight to no where today")
                        time.sleep(3)
                        print("Ez la boi and la fairs today is a day that I truly truly truly hate and I say tmrw and today hey hey het its over for me today maybe i can do the thing that will affect both me and ye and I say with glee yippe maybe today is a good day for me la yippe! my ears cant even breathe woopsie dasie")
                        time.sleep(3)
                        print("I was so thirsty ")
                    

                #this and above marks the Good side of the Knight Story


                    


#This and below marks the bad side of the knight story
        if choice1 == "1":
            print("Well, Well, Well your intresting BUT I CANT LET YOU BE THE DARK SIDE")
            time.sleep(3)
            choice2 = input("FIGHT attack first(1) or defend(2)")
            if choice2 == "2":
                print("You block, counter attack and and you steal his 300 coins but you must escape soon before you get caught!")
                time.sleep(3)
                print("+300 coins")
                coins = 300
            if choice2 == "1":
                print("You attack first which knocks the guy out and you steal his diamond sword and 300 coins but you must escape soon before you get caught!")
                time.sleep(3)
                print("+300 coints\n+diamond sword")
                coins = 300
                diamondsword = 1
            print("(You are forced to flee and stumble upon a great german black horse)")
            choice3 = input("Do you steal it(1), or do you run off without it to go get some gold(2)?")
            if choice3 == "1":
                print("You now have a noble horse! But it belonged to a milltary officer and now a fleet is running after you but you manage to escape them, your bounty is increased be careful if its too high it could cause trouble!")
                bounty = 1000
                noblehorse = noblehorse + 1
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
                    choice6 = 123456789
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
        if choice7 == "2":
            print("You dont steal and officers found you and surrond you and you have three options!")
        if choice7 == "1":
            choice8 = input("Do you use a whistle thats in your bag(1) or do you just run(2)")
        if choice7 == "2":
            choice8 = input("Do you fight(1), use a whistle in your bad(2), or just run(3)")
            if choice8 == "1":
                print("You fight them, you are one great dark knight and take them down but your bounty is emmense now but so is your gold!")
                print("+2500 Bounty")
                print("+1250 Gold")
                bounty = bounty + 2500
                coins = coins + 1250
            if choice8 == "2":
                if noblehorse == 1:
                    print("You call your horse using your whistle and leave unschated!")
                if noblehorse != 1:
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
                choice10 = input("For this he offers you a great black knight suit of armor for half off(500 coins now)Do you take it? (y/n)")
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
                if blacksuit == 1:
                    print("Knight Black Suit: " + str(blacksuit))
                
                time.sleep(3)
                if blacksuit == "1":
                    if diamondsword == 1:
                        print("You leave your blacksuit behind along with your diamond sword in your apartment for later")
                    elif ironsword == 1:
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
                print("You are outside and hear people talk about the great white knight, you are curious so you ask them for more info")
                time.sleep(5)
                print("Random Dude: Oh yeah the Great White Knight is coming")
                time.sleep(3)
                print("Randome Dude: Maybe he could stop the crazy guy who is fighting officers and stealing from people")
                time.sleep(3)
                print("You: Yeah I guess... but he isn't easy to take down he is very strong")
                time.sleep(3)
                print("Random Dude: Nah the Great White Knight is way too powerful for some random bandit")
                time.sleep(3)
                print("Random Dude: Wait who are you again? OH CRAP ITS YO-")
                time.sleep(3)
                print("You right hook him fast enough before he can finish his setence.")
                time.sleep(3)
                print("You walk back into your apartment and chill you decide to borrow books from the libary to read about the great white kinght")
                time.sleep(3)
                print("You walk into the libary and instantly start searching for books and start reading")
                time.sleep(3)
                print("\"The Great White Knight is a title passed through a family\"")
                time.sleep(3)
                print("\"The maiden of the previous knight's offspring brind down the title to their strongest one once he or she is ready for it, which  becomes the new Great White Knight\"")
                time.sleep(3)
                print("\"The current Great White Knight is the strongest out of all the people to have held the title")
                time.sleep(3)
                print("\"Any bandit or criminal who thinks that they can take the current Great White Knight is mistaken")
                time.sleep(3)
                print("\"He currently holds the Great White Knight armor and sword with the only armor and tools that can pottenitally overpower it is the Great Black Knight's armor and sword but one hasn't been seen in a while.\"")
                time.sleep(3)
                print("You think to your self \"I am the dark knight\"")
                time.sleep(3)
                if blacksuit != 1:
                    print("You go out to a armor store and find a black knight suit that speaks to you and you buy it on the spot.")
                    print("-900 Coins")
                    coins = coins - 900
                choice12 = input("What do you want to do now? Rob some more people(1), train (2), laylow(3)")
                if choice12 == "1":
                    print("You rob some people of the street and get gold and increased bounty")
                    print("+500 Coins")
                    print("+500 Bounty")
                    coins = coins + 500
                    bounty = bounty + 500
                if choice12 == "2":
                    print("You train and get stronger, much stronger could help soon")
                    train = 1
                if choice12 == "3":
                    print("You laylow and lose some bounty")
                    print("-300 Bounty")
                    bounty = bounty - 300
                print("Then in shock like it happened in a split second the Great White Knight comes from no where")
                time.sleep(3)
                print("In one strike you are knocked out and defeated as you are closing your eyes while the crowd celebrates him but something astounding happens.")
                time.sleep(3)
                print("You stand right back up adreline shaking you rush into your apartment grab your armor and sword and you run back out ready to fight!")
                time.sleep(4)
                print("Great White Knight: Most men wouldn't even live after a hit like that, but your still standing. Also your armor it's different...")
                time.sleep(3)
                print("You: Im not a ordinary man you know")
                if noblehorse == 1:
                    print("You call your horse and get ready to fight with both of yall on your horses")
                else:
                    print("You see a black german horse and buy it off a  officer for 750 coins")
                    print("-750 coins")
                    coins = coins - 750
                    noblehorse = 1
                choice13 = input("Do you attack first by charging(1), or do you defend(2)")
                if choice13 == "1":
                    print("You attack first but your sword is too weak but you take mutlple hits before falling to his strength because your armor is strong")
                if choice13 == "2":
                    print("You defend first and yor armor is strong but your sword is weak so you take hits before falling to his strength")
                time.sleep(3)
                print("Great White Knight: Hmph so much talk to fall down to my might")
                time.sleep(3)
                print("He is about to land the final hit on you while you are on the floor...")
                time.sleep(5)
                print("Then your noble horse clamps onto you by biting your armor with its mouth and drags you at high speeds away to saftey barely alive!")
                time.sleep(4)
                print("You end up in a near by village and start to rest along a tree with injuries")
                time.sleep(3)
                print("You go to a doctor known for not reporting criminals who come to him, unless your bounty is above 2000")
                time.sleep(3)
                print("Your Bounty: " + str(bounty))
                time.sleep(3)
                if bounty <= 2000:
                    print("Your bounty is less than or equal to 2000 your fine for now")
                if bounty > 2000:
                    print("It higher lets see if you trained to make the self healing faster!")
                    if train == 1:
                        print("Ok your fine you trained but spend 200 coins taking care of your self")
                    if train != 1:
                        print("You try and self healbut messs up causing you to buy random healthy junk that you don't need")
                        print("-1500 Coins")
                        coins = coins - 1500
                choice14 = input("Do you do a robbery for gold for extra money? (y/n)")
                if choice14 == "y":
                    print("You do it and get gold but also increased bounty")
                    print("+750 Coins")
                    print("+500 Bounty")
                    coins = coins + 750
                    bounty = bounty + 500
                print("You hear of a rumor, a whisper infact that in a village nearby there is a sword in a rock that started to have a emmenese aura of black")
                time.sleep(3)
                print("Even werider it started to glow right after the fight of you and the great white knight like it is calling you...")
                time.sleep(3)
                print("You leave the next day DAY 2 CLOsED")
                print("*Showing Stats*")
                print("Coins: " + str(coins))
                print("Bounty: " + str(bounty))
                if noblehorse == 1:
                        print("Noble Horse: " + str(noblehorse))
                if blacksuit == 1:
                        print("Knight Black Suit: " + str(blacksuit))
                print("You wake up take your horse and belongings and go to the nearby village in seek of that sword")
                time.sleep(3)
                print("You arrive in the village and decide to wear your armor to find and approach the sword and hopefully take it")
                time.sleep(3)
                print("You walk into a store to ask where this alleged sword is")
                time.sleep(3)
                print("Store Manager: Oh you one of em tourists arent ye well go down the street take a right and then another right and you should see it")
                time.sleep(3)
                print("You: Thank you, and I ain't no common tourist. Goodbye sir")
                time.sleep(3)
                print("You follow his instructions and stumble accross some officers guarding it, you easily overpower them")
                time.sleep(3)
                print("You gain coins and bounty")
                print("+500 Coins")
                print("+500 Bounty")
                coins = coins + 500
                bounty = bounty + 500
                print("Then you see it the shining black sword that has a aura like it speaks to you just like your armor, then...")
                time.sleep(3)
                print("The Great White Knight comes up, it was all a trap!")
                time.sleep(3)
                print("Great White Knight: hmph you fell for it now prepare")
                time.sleep(3)
                print("He charges at you, you do the same but last second you dodge then you reach down your arm off your horse and grab the dark sword...")
                time.sleep(3)
                print("The second you touch it its like a piece of you that finally connected, you run off with your horse with the Great White Knight in absoulute shock")
                time.sleep(3)
                print("You ride all the way back to the village and rest on the same tree that you rested on after your first encounter")
                time.sleep(3)
                choice15 = input("You cab go to a crimal hub and steal all of their loot (y/n)")
                if choice15 == "y":
                    print("+750 Coins")
                    print("+750 Bounty")
                if choice15 == "n":
                    print("You decide just to rest next to the tree today was a long day for you")
                time.sleep(3)
                print("You walk into a shop buy some food then rest in a hotel for the night...")
                time.sleep(3)
                print("Day 3 has ended, it was a long day for you")
                time.sleep(3)
                print("*Stats Showing*")
                print("Coins: " + str(coins))
                print("Bounty: " + str(bounty))
                if noblehorse == 1:
                    print("Noble Horse: " + str(noblehorse))
                if blacksuit == 1:
                    print("Knight Black Suit: " + str(blacksuit))
                print("You leave your hotel in search of something to do to prepare you for your inevetable encounter with the Great White Knight soon")
                time.sleep(3)
                input("Do you train(1), buy supplies(2), or eat(3)")
                print("You decide your activity then")
                time.sleep(2)
                print("A sudden BOOM and your door is knocked down officers are swaming in you over power them put on all your stuff and go oustide")
                time.sleep(4)
                print("Almost 100 officers came to stop you you try and fight back but your fate is ineventable and you are soon knocked unconsious")
                time.sleep(3)
                print("They are taking you away to a far far place in a carridge tied up with over 150 soilders surronding it prepared to attack")
                time.sleep(3)
                print("The soilders in your carrige see you woke up and knock you out again but it takes MUTLIPLE hits its like you get stronger after each fight...")
                time.sleep(3)
                print("Soon you wake up a a dark dunegon room with your sword next to you but you can't reach because you are chained up")
                time.sleep(3)
                print("Then they take your chains and drag you all the way into a MASSIVE areana, a collsumen")
                time.sleep(3)
                print("Its the royal areana in the capital and you've only dreamed of ever being here but today you are here to fight")
                time.sleep(3)
                print("Then you see him on the other side of the areana, the Great White Knight")
                time.sleep(3)
                print("They unlock your chains you pick up your weapon from the floor and you hear a loud voice")
                time.sleep(3)
                print("Royal Commentary: TODAY WE HAVE THE ONE AND ONLY GREAT WHITE KNIGHT AND THE ALLEGED BLACK KNIGHT ON THE OTHER SIDE")
                time.sleep(3)
                print("The people celebrate when they hear the Great White Knights name but boo when hear yours.")
                time.sleep(3)
                print("Royal Commentary: THE KING IS PLEASED TO SEE BOTH FIGHTES IN THE ARENA TODAY")
                time.sleep(3)
                print("Royal Commentary: IF THE DARK KNIGHT WINS THEN HE GETS A CLEAN TITLE IF HE LOSES THEN...")
                time.sleep(3)
                print("Great White Knight to You: Hmm I've encountred you many times before, be prepared to meet the same fate")
                time.sleep(3)
                print("Royal Commentary: LET THE BATTLE COMMENCE")
                time.sleep(3)
                print("Your horse and the Great White Knight's come out and you both get on them")
                time.sleep(3)
                choice16 = input("Do you charge first(1) or do you defend(2)")
                if choice16 == "1":
                    print("You attack first and your sword does a lot of damage due to your incredible strenth along with it")
                if choice16 == "2":
                    print("You defend block his attack and deliever a strong counter attack")
                time.sleep(3)
                print("Royal Commentary: I CANT BELIEVE IT THE DARK KNIGHT IS TAKING THE LEAD")
                time.sleep(3)
                print("You continue to exachange hits but its like for both of yall each hit makes yall stronger...")
                time.sleep(3)
                print("The Great White Knight starts to look desperate no one has matched him before")
                time.sleep(3)
                print("He rides away for a second you assume to rest so so do you")
                time.sleep(3)
                print("You soon charge again he strikes a spot at a hinge to hit skin, almost no force due to the direction")
                time.sleep(3)
                print("Then you feel queasy and fall off your horse, he wasn't resting he was coating his blade with poison...")
                time.sleep(3)
                print("You hear in the background as you are closing your eyes.")
                time.sleep(3)
                print("Royal Commentary: LOOKS LIKE THE DARK KNIGHT IS DOWN NO ONE CAN DEFEAT THE GREAT WHITE KNIGHT")
                time.sleep(3)
                choice17 = input("Do you resist(1), or let go...(2)")
                if choice17 == "1":
                    print("You resist and get back up on your horse with your body trembling with energy and rage, The Great White Knight isn't so fair")
                if choice17 == "2":
                    print("You try and let go but your body says no and you get back up on your horse trembling, The Great White Knight isn't so fair")
                print("Royal Commentary: THE BLACK KNIGHT IS BACK UP HE LOOKS EVEN SCARIER THEN BEFORE, HIS ARMOR IT'S? EMMITING GAS?")
                time.sleep(3)
                print("You finnally figure out the secret of this armor, the more angrey and detmermined you are the stronger your armor and sword get...")
                time.sleep(3)
                print("Great White Knight: How are you still standing, stronger than before. Well I cant let you tell anyone about my secret")
                time.sleep(3)
                print("You: You dirty cheater you don't desereve your title")
                time.sleep(3)
                choice18 = input("(WARNING A WRONG CHOICE CAN LEAD TO THE END)Do you raise your hand to call for a check of cheating(1), charge foward(2), or do you try to block his next attack(3)")
                while True:
                    if choice18 == "1":
                        print("You try and call a check but they deney it and the Great White Knight strikes you ending your story...")
                        break
                while True:
                    if choice18 == "2":
                       print("You attack first your rage carrying your movement and your sword easily pierces the Great White Knight's ending the fight but keeping him alive")
                       print("You have won your bounty is split in half and they let you run free for one day to get away")
                       print("-" + bounty)
                       bounty = bounty/2
                while True:
                    if choice18 == "3":
                        print("You block counter attack and win and you are let go and given a one day headstart to run away ")
                


                
               


        
                