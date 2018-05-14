#stage 1
def QuestIA():
    text = "You land on a barn and start collecting a medkit, sniper, and a submachine gun."
    text = "You hear someone else in the stables."
    #user input choice
    myDialogueQuestIA = screenText.textinput("Fortnite", "1. Let him find you? 2. Or attack this guy? Please Choose 1 or 2.")

    if myDialogueQuestIA == "1":
        text = "You wait in some hay like a noob and kill him when he runs over." 
        text = "Good job but it's hard to win playing it safe like that."
        QuestIB()

    if myDialogueQuestIA == "2":
        text = "You sneakily walk into a stall as he's looting the room."  
        #70% chance of surviving
        computerQuestIA = randint(1,10)
        if computerQuestIA > 3:
            text = "You start unloading on this noob and obliterate him before he opens some chest."  
            text = "Great job."  
            QuestIB()
        else:
            text = "Your slow to shoot him and he manages to jump around dodging your bullets then kills you."  
            text = "Get your game up."    
            text = "Please play again"  
            done()

#stage 2
def QuestIB():
    text = "You open the chest and gather ammo, bandages, and some small shields."  
    text = "The storm is forming around Loot Lake."  
    text = "You looted everything so you dip away from Anarchy Acres."  
    text = "There's a tunnel on your route so you loot it out and gather ammo, building material, and a Legendary SCAR!!"
    text = "There's a fire fight from a distance so you go and investigate."
    #user input choice
    myDialogueQuestIB = screenText.textinput("Fortnite", "1. Engage from behind? Or 2. Let them battle? Please Choose 1 or 2.")

    if myDialogueQuestIB == "1":
        text = "You pop up from the hill and destroy one guy. You see the other guy so you plow him down too."
        text = "Wow that SCAR is really helpful."
        QuestIC()
    
    if my DialogueQuestIB == "2":
        text = "You let them battle it out and you go in the opposite direction." 
        text = "Let's hope either of them doesn't find you later." 
        QuestIC() 

#stage 3
def QuestIC():
    text = "Your outside the safe zone from the storm so you move in and begin building a tall fort."
    text = "11 players left."
    text = "You pummel down three noobs running into the safe zone and wait till the numbers windle down to 2."
    text = "You start getting RPG'd, your fort is destroyed, and your pinned with fire. You must engage."
    #50% chance of wining
    computerQuestIC = randint(1,10)
    if computerQuestIC > 5:
        text = "You jump out, dodge an RPG, and drill him with bullets to his death"  
        text = "#1 VICTORY ROYALE"
        text = "Good Job!!!"  
        done()
        
    else:
        text = "You jump out to shoot him but the RPG was too powerful."  
        text = "You tried your best, there was nothing else to do."  
        text = "Sorry."  
        text = "Please play again"  
        done() 