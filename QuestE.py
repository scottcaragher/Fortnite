#stage 1
def QuestEA():
    text = "You land in a big mansion that looks real snobby."
    text = "You noticed someone landing on the neighboring house so you gather supplies."
    text = "You find a sniper,submachine gun, and a boogie bomb as you hear someone frolicking around the backyard pool."
    #user input choice
    myDialogueQuestEA = screenText.textinput("Fortnite", "1. Throw the bomb at him and attack? 2. Or throw it and have a dance party? Please Choose 1 or 2.")
 
    if myDialogueQuestEA == "1": 
        #70% chance of surviving
        computerQuestEA = randint(1,10)
        if computerQuestEA > 3:
            text = "You get him by surprise and its really funny as he starts disco dancing but he's vulnerable so you pummel him." 
            text = "Great kill."
            QuestEB()
        else:
            text = "Your slow to shoot him and he manages to jump around dodging your bullets then kills you."  
            text = "Get your game up."    
            text = "Please play again"  
            done()

    if myDialogueQuestEA == "2": 
        #20% chance of survival
        computerQuestEAA = randint(1,10)
        if computerQuestEAA > 8:
            text = "You both start dancing, wave at each other with the emote and go in seperate ways." 
            text = "We are all the same people playing this game. What a great guy."
            QuestEB()

        else:
            text = "You start dancing with him but he's not a nice guy so he kills you after the bomb."  
            text = "It was fun while it lasted but you can't trust anyone in this game."
            text = "Please play again."
            done()

#stage 2
def QuestEB():  
    text = "The storm is forming around Pleasant Park."  
    text = "You looted everything so you dip away from Snobby Shores."  
    text = "There's a fort on your route so you loot it out and gather some more ammo."
    text = "There's gun fire from a distance so you go and investigate. A player just killed someone and begins to run over for the loot."
    #user input choice
    myDialogueQuestEB = screenText.textinput("Fortnite", "1. Snipe him? Or 2. Let him pass? Please Choose 1 or 2.")

    if myDialogueQuestEB == "1": 
        #60% chance of survival
        computerQuestEB = randint(1,10)
        if computerQuestEB > 4:
            text = "You dome him in the head and he dies #getrect."
            QuestEC()
        else:
            text = "You miss the easy shot and he builds an instant fort. Uh oh get ready for battle."  
            text = "He doesn't quite know where you are so you shoot him again but he stays alive."    
            text = "He re-heals and pokes his head out but he gets you in the head a millisecond before you shoot."
            text = "Sorry please play again."  
            done()

    if myDialogueQuestEB == "2": 
        #60% chance of survival
        computerQuestEBA = randint(1,10)
        if computerQuestEBA > 4:
            text = "You stay hidden like a scaredy cat and let him pass. Hopefully he doesn't find you later."
            QuestEC()
        else:
            text = "Your crouched down behind a tree watching him staying completely still and out of nowhere someone snipes you to your death."  
            text = "Oops, always keep moving."
            text = "Please play again."
            done()

#stage 3
def QuestEC():
    text = "Your outside the safe zone from the storm so you move in and begin building a tall fort."
    text = "5 players left."
    text = "You destroy someones fort and kill him easily from previous low health. Another guy starts shooting at you with no fort so you snipe him."
    text = "You start getting shot at 100 yards away and your pinned with fire. You must try and engage."
    #50% chance of winning
    computerQuestEC = randint(1,10)
    if computerQuestEC > 5:
        text = "You can see where he is with his head poking out so you aim down your sights with the sniper, stand up and finish off the last guy."  
        text = "#1 VICTORY ROYALE"
        text = "Nice shot!!!"  
        done()
    else:
        text = "You jump out to shoot him but he was ready and kills you."  
        text = "You tried your best, there was nothing else to do."  
        text = "Sorry."  
        text = "Please play again"  
        done()