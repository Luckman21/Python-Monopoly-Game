'''
Created on Mar 29, 2018

@author: Luck
'''
from random import randint,shuffle
import time

cash = [1500,1500,1500,1500]
space = [0,0,0,0]
jail = [0,0,0,0]
names,lost,rent,pays = [],[],[],(25,100)
turn,players,s,g = 0,0,1,0
Monopoly = ("M","O","N","O","P","O","L","Y")
spaces = ("GO","H","CC","H","T","TR","H","C","H","H","JV","H","CO","H","H","TR","H","CC","H","H","FP","H","C","H","H","TR","H","H","CO","H","GTJ","H","H","CC","H","TR","C","H","T","H")
spacename = ("GO","Elemental Sanctuary","Treasure Chest","Minish Village","Door Fee","Spirit Train","House of Gales","Empty Bottle","Sacred Realm","Lorule Castle","Just Visiting","Forsaken Fortress","Bomb Shop","Outset Island","Dragon Roost Island","Loftwing","Four Sword Sanctuary","Treasure Chest","Death Mountain","Vaati's Palace","Free Parking","Gerudo Desert","Empty Bottle","Zora's Domain","Twilight Realm","King of Red Lions","Snowhead","Great Bay","Potion Shop","Clock Town","GO TO JAIL","Eldin Volcano","Faron Woods","Treasure Chest","Skyloft","Epona","Empty Bottle","Hyrule Castle","Mask Merchant","Temple of Time")
price = (0,60,0,60,200,200,100,0,100,120,0,140,150,140,160,200,180,0,180,200,0,220,0,220,240,200,260,260,150,280,0,300,300,0,320,200,0,350,100,400)
buy1,buy2,buy3,buy4 = ["None"],["None"],["None"],["None"]
bought = [buy1,buy2,buy3,buy4]
prop1,prop2,prop3,prop4 = [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]
props = [prop1,prop2,prop3,prop4]
propps = (2,3,3,3,3,3,3,2)
card = [False,False,False,False]
CCcard = ["A","A","B","B","B","C","C","D","E","E","F","F","F","G","G","G"]
#ALL TYPES OF SPACES: GO, H = House, CC = Community Chest, T = Income Tax, C = Chance
#JV = Just visiting, JAIL = Jail, CO = Companies, TR = Train, FP = Free Parking
#GTJ = Go To Jail 

for x in range (0,len(price)):
    if price[x] == 0:
        rent.append(0)
    else:
        rent.append((price[x])/10)

for x in range (0,len(Monopoly),2):
    print Monopoly[x],Monopoly[x+1],
    time.sleep(1)

while True:
    players = input("\n\nHow many players would you like to play with? (Game runs with 2-4 players)\n: ")
    play = players
    if players >=2 and players <=4:
        break
    elif players > 4:
        print "\nSorry, "+str(players)+" cannot play.  Tell at least "+str(players-4)+" to leave so we can start playing already!"
    elif players < 2 and players >= 0:
        print "\nSorry, "+str(players)+" cannot play.  Tell at least "+str(2-players)+" to join so we can start playing already!"
    else:
        print "\nSorry, "+str(players)+" cannot play.  This game is only 2-4 players."

for x in range (0,players):
    name = raw_input("\nPlayer "+str(x+1)+", enter your name: ")
    names.append(name)

choose = raw_input("\nHow fast do you want your game to run?\n\n1 - Fast\n2 - Normal\n3 - Slow\n: ")

if choose == "1":
    s = 0.5
elif choose == "2":
    s = 1
else:
    s = 2

while players >= 2:
    turn+=1
    time.sleep(s)
    g = 0
    
    while g == 0:
        g = 0
        for x in range(0,players):
            if cash[x] < 0:
                print "\n"+names[x]+" is now out of the game because "+names[x]+" has lost all their Rupees!"
                time.sleep(s*2)
                print "All properties of "+names[x]+" are now up for sale!"
                time.sleep(s*2)
                del cash[x],space[x],jail[x],bought[x],props[x],card[x]
                lost.append(names.pop(x))
                players-=1
                break
            else:
                g = 1
    
    if players < 2:
        continue
            
    print "\n|==========(STATS)==========|"
    print "\n",
    
    for x in range (0,players):
        print names[x]+"\n\tSpace = "+str(space[x])+"\n\tRupees = $"+str(cash[x])+"\n\n\tProperty = "+str(bought[x])+"\n"
    time.sleep(s*2)
    
    for x in range (0,players):
        change,doubles = 0,0
        time.sleep(s)
        
        print "\n|-----(TURN #"+str(turn)+")-----|"
        
        while doubles < 3 and change == 0:
            
            while True:
                print "\n["+names[x],
                enter = raw_input("press enter to roll the dice! (0 and \"ENTER\" to enter the menu)]")
                
                if enter == "0":
                    print "\n|~~~~~(MENU)~~~~~|"
                    choose = raw_input("\nWhat would you like to do?\n\n1 - Check Stats\n2 - Sell Property\n(0 and \"ENTER\" to exit!)\n: ")
                    
                    if choose == "0":
                        pass
                    elif choose == "1":
                        print "\nStatistics:"
                        for y in range (0,players):
                            print names[y]+"\n\tSpace = "+str(space[y])+"\n\tRupees = $"+str(cash[y])+"\n\n\tProperty = "+str(bought[y])+"\n"
                        continue
                    elif choose == "2":
                        if bought[x][0] == "None":
                            print "\nYou don't have any properties at the moment, so this feature is unavailable!"
                            pass
                        else:
                            print "\nWhich property would you like to sell?\n"
                            time.sleep(s)
                            for y in range(0,len(bought[x])):
                                print str(y+1)+": "+str(bought[x][y])+" = $"+str((price[spacename.index(bought[x][y])])/2)
                            sell = input("\n(0 and \"ENTER\" to quit!)\n: ")
                            sell-=1
                            if sell == -1:
                                pass
                            else:
                                print "\nYou sold "+str(bought[x][sell])+" for $"+str((price[spacename.index(bought[x][sell])])/2)+" Rupees!"
                                if len(bought[x]) == 1:
                                    (bought[x]).append("None")
                                cash[x]+=((price[spacename.index(bought[x][sell])])/2)
                                if bought[x][sell] == "Elemental Sanctuary" or bought[x][y] == "Minish Village":
                                    props[x][0] = 0
                                elif bought[x][sell] == "House of Gales" or bought[x][y] == "Sacred Realm" or bought[x][y] == "Lorule Castle":
                                    props[x][1] = 0
                                elif bought[x][sell] == "Forsaken Fortress" or bought[x][y] == "Outset Island" or bought[x][y] == "Dragon Roost Island":
                                    props[x][2] = 0
                                elif bought[x][sell] == "Four Sword Sanctuary" or bought[x][y] == "Death Mountain" or bought[x][y] == "Vaati's Palace":
                                    props[x][3] = 0
                                elif bought[x][sell] == "Gerudo Desert" or bought[x][y] == "Twilight Realm" or bought[x][y] == "Zora's Domain":
                                    props[x][4] = 0
                                elif bought[x][sell] == "Snowhead" or bought[x][y] == "Clock Town" or bought[x][y] == "Great Bay":
                                    props[x][5] = 0
                                elif bought[x][sell] == "Faron Woods" or bought[x][y] == "Eldin Volcano" or bought[x][y] == "Skyloft":
                                    props[x][6] = 0
                                elif bought[x][sell] == "Hyrule Castle" or bought[x][y] == "Temple of Time":
                                    props[x][7] = 0
                                del bought[x][sell]
                        continue
                else:
                    break
                
            dice1,dice2 = randint(1,6),randint(1,6)
            die = dice1+dice2
            
            if dice1 == dice2:
                change = 0
                doubles+=1
            else:
                change = 1
            
            print names[x],  
            
            if die == 8 or die == 11:
                print "rolled an "+str(die)+"!"
            else:
                print "rolled a "+str(die)+"!"
            
            if space[x] == "JAIL":
                pass
            else:
                space[x]+=die 
                time.sleep(s)
            
            if change == 0:
                print "Wow!  You rolled two "+str((die)/2)+"'s!"
                time.sleep(s)
            if doubles == 3:
                print "\nUh oh, you rolled 3 doubles in a row!  Jail time for you >_<"
                time.sleep(s)
                space[x] = "JAIL"
                break
            
            time.sleep(s)
            if space[x] != "JAIL":
                            
                if space[x] == 30:
                    print "Oh no!  You landed on the \"GO TO JAIL\" space!  Jail time for you,",names[x]+"!"
                    space[x],doulbes,change = "JAIL",0,1
                    continue
                
                if space[x] > 39:
                    space[x]-=39
                    if space[x] == 0:
                        print "You are on the \"GO!\" space.  You earned $200 Rupees!"
                    elif space[x] > 0:
                        print "You passed the \"GO!\" space.  You earned $200 Rupees!"
                    cash[x]+=200
                
                if spaces[space[x]] == "CC" or spaces[space[x]] == "C":
                    if spaces[space[x]] == "CC":
                        select = input("\nYou landed on a "+spacename[space[x]]+" space!  Choose a card from 1 - 16: ")  
                    if spaces[space[x]] == "C":
                        select = raw_input("\nYou landed on an "+spacename[space[x]]+" space!  Choose a card from 1 - 16: ")
                    if select == "":
                        select = randint(1,16)
                    select=int(select)-1
                    if select < 0 or select > 15:
                        select = randint(0,15)
                    else:
                        shuffle(CCcard)
                        print "The card reads:",
                        if CCcard[select] == "A":
                            print "\"Advance to \"GO\" and collect $200 Rupees!\"\nYou've collected $200 Rupees and are now on \"GO\"!"
                            cash[x]+=200
                            space[x] = 0
                        elif CCcard[select] == "B":
                            if space[x]+10 > 39:
                                print "\"Advance to "+spacename[space[x]-29]+".  If you pass \"GO\", collect $200 Rupees.\""
                                space[x]-=29
                                cash[x]+=200
                                print "\nYou passed \"GO\" and collected $200 Rupees!"
                            else:
                                print "\"Advance to "+spacename[space[x]+10]+".  If you pass \"GO\", collect $200 Rupees.\""
                                space[x]+=10
                                print "\nYou did not pass go, but moved to "+spacename[space[x]]+"."
                        elif CCcard[select] == "C":
                            print "\"GO TO JAIL.\""
                            space[x] = "JAIL"
                            continue
                        elif CCcard[select] == "D":
                            print "\"GET OUT OF JAIL FREE CARD. Only redeemable once.\""
                            card[x] = True
                        elif CCcard[select] == "E":
                            num = randint(1,2)
                            if num == 1:
                                print "\"Defeat Ganondorf.  You've earned $200 Rupees!\""
                                cash[x]+=200
                            else:
                                print "\"Touch the Triforce.  You've gained $300 Rupees!\""
                                cash[x]+=300
                        elif CCcard[select] == "F":
                            num = randint(1,3)
                            if num == 1:
                                print "\"Breaking Pots.  You've collected $50 Rupees!\""
                                cash[x]+=50
                            elif num == 2:
                                print "\"Complete a sidequest.  Collect $30 Rupees!\""
                                cash[x]+=30
                            else:
                                print "\"Cutting Grass.  You've collected $25 Rupees!\""
                                cash[x]+=25
                        else:
                            num = randint(1,3)
                            if num == 1:
                                print "\"Lose to Ganondorf.  Drop $150 Rupees.\""
                                cash[x]-=150
                            elif num == 2:
                                print "\"The Bokoblin's steal your gear.  Lose $50 Rupees.\""
                                cash[x]-=50
                            else:
                                print "\"Princess Zelda is defeated.  Forfeit $200 Rupees.\""
                                cash[x]-=200
                    
                if spaces[space[x]] == "H":
                    print "\nYou landed on a property!"
                    time.sleep(s)
                    rents,buy = 0,1
                    for y in range (0,len(bought)):
                        for z in range(0,len(bought[y])):
                            if bought[y][z] == spacename[space[x]]:
                                rents,buy,pay = rent[space[x]],0,y
                            for i in range(0,len(bought[x])):
                                if bought[x][i] == spacename[space[x]]:
                                    rents,buy = 0,2
                                
                    print "\nProperty:",
                    print spacename[space[x]]
                    
                    if buy == 1:
                        print "\n\tPrice: $"+str(price[space[x]])+" Rupees\n\tRupees in wallet = $"+str(cash[x])
                        buy = raw_input ("\nWould you like to purchase this property?\n\n1 - Yes\n2 - No\n: ")
                        if buy == "1":
                            if bought[x][0] == "None":
                                del bought[x][0]
                            (bought[x]).append(spacename[space[x]])
                            cash[x]-=int(price[space[x]])
                        if buy != "1":
                            print "\nYou didn't buy "+spacename[space[x]]+"."
                    if buy == 0:
                        print "\nSorry, this property is already bought!  You must pay a rent of $"+str(rents)+" Rupees to "+names[pay]+"!"
                        cash[x]-=rents
                        cash[pay]+=rents
                    if buy == 2:
                        print "\nYou landed on your own property, so you didn't lose any Rupees!"
                    
                if spaces[space[x]] == "JV" or spaces[space[x]] == "FP":
                    if spaces[space[x]] == "JV":
                        place = "Just Visiting"
                    else:
                        place = "Free Parking"
                    print "\nYou've landed on "+place+"."
                    time.sleep(s)
                
                if spaces[space[x]] == "T":
                    print "\n"+spacename[space[x]]+".  You payed $"+str(price[space[x]])+" Rupees to pass."
                    cash[x]-=price[space[x]]
                
                if spaces[space[x]] == "TR":
                    buy = 1
                    print "\nYou landed on a transportation space!"
                    time.sleep(s)
                    pay = 0
                    for y in range (0,len(bought)):
                        for z in range(0,len(bought[y])):
                            if bought[y][z] == spacename[space[x]]:
                                buy,payed = 0,y
                                for n in range(0,len(bought[y])):
                                    if bought[y][n] == "Spirit Train" or bought[y][n] == "Loftwing" or bought[y][n] == "King of Red Lions" or bought[y][n] == "Epona":
                                        pay+=1                           
                            for i in range(0,len(bought[x])):
                                if bought[x][i] == spacename[space[x]]:
                                    buy = 2
                                
                    print "\nTransportation:",spacename[space[x]]
                    if buy == 1:
                        print "\n\tPrice: $"+str(price[space[x]])+" Rupees\n\tRupees in wallet = $"+str(cash[x])
                        buy = raw_input ("\nWould you like to purchase this transportation?\n\n1 - Yes\n2 - No\n: ")
                        if buy == "1":
                            if bought[x][0] == "None":
                                del bought[x][0]
                            (bought[x]).append(spacename[space[x]])
                            cash[x]-=int(price[space[x]])
                        if buy != "1":
                            print "\nYou didn't buy "+spacename[space[x]]+"."
                    if buy == 0:
                        print "\nSorry, this transportation is already bought!  You must pay a rent of $"+str(pay*25)+" Rupees to "+names[payed]+"!"
                        cash[x]-=(pay*25)
                        cash[y]+=(pay*25)
                    if buy == 2:
                        print "\nYou landed on your own transportation, so you didn't lose any Rupees!"
                        
                if spaces[space[x]] == "CO":
                    buy = 1
                    print "\nYou landed on a company!"
                    time.sleep(s)
                    pay = 0
                    for y in range (0,len(bought)):
                        for z in range(0,len(bought[y])):
                            if bought[y][z] == spacename[space[x]]:
                                buy,payed = 0,y
                                for n in range(0,len(bought[y])):
                                    if bought[y][n] == "Potion Shop" or bought[y][n] == "Bomb Shop":
                                        pay+=1                           
                            for i in range(0,len(bought[x])):
                                if bought[x][i] == spacename[space[x]]:
                                    buy = 2
                    if pay == 2:
                        pay = 10
                    else:
                        pay = 4    
                    print "\nCompany:",spacename[space[x]]
                    if buy == 1:
                        print "\n\tPrice: $"+str(price[space[x]])+" Rupees\n\tRupees in wallet = $"+str(cash[x])
                        buy = raw_input ("\nWould you like to purchase this company?\n\n1 - Yes\n2 - No\n: ")
                        if buy == "1":
                            if bought[x][0] == "None":
                                del bought[x][0]
                            (bought[x]).append(spacename[space[x]])
                            cash[x]-=int(price[space[x]])
                        if buy != "1":
                            print "\nYou didn't buy "+spacename[space[x]]+"."
                    if buy == 0:
                        print "\nSorry, this company is already bought!  You must pay a fine of $"+str(pay*die)+" Rupees to "+names[payed]+"!"
                        cash[x]-=(pay*die)
                        cash[y]+=(pay*die)
                    if buy == 2:
                        print "\nYou landed on your own company, so you didn't lose any Rupees!"
            
            if space[x] == "JAIL":
                jail[x]+=1
                if doubles == 1:
                    print "\nWow, you rolled a double.  You got out of jail and you moved "+str(die)+" spaces!"
                    space[x] = 12+(die)
                    jail[x] = 0
                elif card[x] == True:
                    print "\nWow, you have a get out of jail free card and you used it!  You moved "+str(die)+" spaces!"
                    space[x] = 12+(die)
                    jail[x],card[x] = 0,False
                else:
                    pay = raw_input("\nWould you like to pay the $50 Rupee fine to get out of jail?\n\n1 - Yes\n2 - No\n: ")
                    
                    if pay == "1":
                        outjail = ["\nYou payed $50 Rupees.","You are out of jail.","You moved "+str(die)+" spaces."]
                        space[x] = 12+(die)
                        jail[x] = 0
                        cash[x]-=50
                    if jail[x] == 3:
                        outjail = ["\nYou were forced to pay $50 Rupees because you were in jail for 3 turns.","You are out of jail.","You moved "+str(die)+" spaces."]
                        for y in outjail:
                            print y,
                            time.sleep(s*1.5)
                        space[x] = 12+(die)
                        jail[x] = 0
                        cash[x]-=50
                change = 1
                
time.sleep(s*2)
print "\n"*50         
print "\n          GAME OVER!\n|=============================|\n"
time.sleep(s*2)
lost.reverse()
for x in range(0,play):
    if x == 0:
        print str(x+1)+": "+str(names[0])
    else:
        print str(x+1)+": "+str(lost[x-1])
    time.sleep(s)
print "\nWinner: "+names[0]+"!"
time.sleep(s)
print "Congratulations, "+names[x]+", you are the winner of this game's Monopoly!"
