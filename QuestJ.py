def QuestJA():
    text = "You land on a house right in the middle of loot lake."
    text = "You collect a sniper and sub machine gun."
    text = "The storm is forming near Retail Row so you head that way."
    text = "You see a play running about 200 yards away."
    myDialogueQuestJA = screenText.textinput("Fortnite", "1. Let him go? 2. Or take the shot? Please Choose 1 or 2.")

    if myDialogueQuestJA == "1":
        text = "He's so far away so you end up losing him."
        QuestJB()

    
    if myDialogueQuestJA == "2":
        computerQuestJA = randint(0,10)
        if computerQuestJA > 6:
            text = "You scope him out and somehow nail the shot and kill him for that distance."  
            text = "Wow great shot."  
            QuestJB()

        else:
            text = "You miss your shot but it scares him away so he hides somewhere unknown."
            QuestJB()

def QuestJB(): 
    text = "There's a house on your route so you loot it out and gather ammo and building materials."
    text = "You hear someone running outside."
    myDialogueQuestJB = screenText.textinput("Fortnite", "1. Engage? Or 2. Let him pass? Please Choose 1 or 2.")

    if myDialogueQuestJB == "1":
        text = "He's running in a straight line and you scope him out and nail him in the back of his head."
        text = "Dang your an elite snipe."
        QuestJC()
    
    if my DialogueQuestIB == "2":
        text = "You let him pass even though you could have killed him. Be more confident." 
        QuestJC() 


def QuestJC():
    text = "Your outside the safe zone from the storm so you move in and begin building a fort."
    text = "6 players left."
    text = "You snipe a few guys hiding behind trees."
    text = "Now there's 2 others left."
    computerQuestJC = randint(0,10)
    if computerQuestJC > 6:
        text = "You get sniped in the head. Wow you were doing so well."
        text = "Sorry maybe next time."
        text = "Please play again."
        done()
        
    else:
        text = "You snipe one guy and see the other running up to you."  
        text = "You get out your sub machine gun and get ready."  
        computerQuestJCA = randint(0,10)
        if computerQuestJCA > 5:
            text = "You jump out and dominate this guy."
            text = "#1 VICTORY ROYALE!!!"
            text = "Great work."
            done()

        else:
            text = "He jumps right ontop of you with his shotgun and ends you."
            text = "Be more ready next time. Please play again."
            done()