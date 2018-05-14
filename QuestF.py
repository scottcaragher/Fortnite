#stage 1
def QuestFA():
    text = "You land in a broken house and find an RPG and a rare Assault Rifle, wow who would've thought in such a house."
    text = "You noticed someone landing on the neighboring house so you get ready."
    #user input choice
    myDialogueQuestFA = screenText.textinput("Fortnite", "1. Go investigate? 2. Or keep distance? Please Choose 1 or 2.")
 
    if myDialogueQuestFA == "1": 
        #70% chance of survival
        computerQuestFA = randint(1,10)
        if computerQuestFA > 3:
            text = "You get him by surprise as he's trying to break down a wall in the neighboring house." 
            text = "Great kill."
            QuestFB()
        else:
            text = "Your slow to shoot him and he manages to jump around dodging your bullets then kills you."  
            text = "Get your game up."    
            text = "Please play again"  
            done()

    if myDialogueQuestFA == "2": 
        #80% chance of survival
        computerQuestFAA = randint(1,10)
        if computerQuestFAA > 2:
            text = "You both go in seperate directions hopeful to not run into him later." 
            QuestFB()
        else:
            text = "you run off but he manages to see you and engage."  
            text = "He then proceeds to mow you down with a SCAR."
            text = "Sorry, Please play again."
            done()

#stage 2
def QuestFB():  
    text = "The storm is forming around Pleasant Park."  
    text = "You looted everything so you leave salty springs."  
    text = "There's a small house on your route so you loot it out and gather some more ammo."
    text = "You see someone from a distance so you follow him. He's at a long distance..."
    #user input choice
    myDialogueQuestFB = screenText.textinput("Fortnite", "1. Start shooting at him? Or 2. continue following? Please Choose 1 or 2.")

    if myDialogueQuestFB == "1": 
        #50% chance or either surviving scenario
        computerQuestFB = randint(1,10)
        if computerQuestFB > 5:
            text = "You hit every shot with your rifle and he dies quickly."
            text = "Wow what great aim."
            QuestFC()
        else:
            text = "You miss some shots and he builds an instant fort. Uh oh get ready for battle."  
            text = "You build a fort and you guys are now in a fire fight."    
            text = "Another player starts shooting at him now too so now he's pinned. You both kill him and now he's shooting at you."
            #50% chance of survival
            computerQuestFBA = randint(1,10)
            if computerQuestFBA > 5:
                text = "You pull out your RPG and hit him two rockets which kill him."
                QuestFC()
            else:
                text = "You try shooting him with the rifle but he over powers you with a heavy machine gun."
                text = "Try again."
                done()

    if myDialogueQuestFB == "2": 
        #60% of survival
        computerQuestFBB = randint(1,10)
        if computerQuestFBB > 6:
            text = "You stay hidden but someone kills you for behind sorry."
            text = "Try again."
            done()
        else:
            text = "You follow him till starts gathering materials where you blow him to pieces with the RPG."  
            text = "Good work."
            QuestFC()
            

#stage 3
def QuestFC():
    text = "Your outside the safe zone from the storm so you move in and begin building a tall fort."
    text = "6 players left."
    text = "You RPG a few weak forts and the noobs get eliminated by other players in strong forts. Now it's the adults playing."
    text = "You watch two players battle it out till one dies."
    #50% chance of winning
    computerQuestFC = randint(1,10)
    if computerQuestFC > 5:
        text = "You use all the fire power you have left and kill the weakling."  
        text = "#1 VICTORY ROYALE"
        text = "Great job."  
        done()
    else:
        text = "You jump out and attack him but ended up with much more health and fire power."  
        text = "You tried your best but maybe stay in protection."  
        text = "Sorry."  
        text = "Please play again"  
        done() 