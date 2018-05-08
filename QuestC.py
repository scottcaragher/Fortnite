def QuestCA():
    text = "You land in the mine shafts and start collecting a medkit, sniper, and a submachine gun."
    text = "You hear someone else above you."
    myDialogueQuestCA = screenText.textinput("Fortnite", "1. Let him find you? 2. Or attack this guy? Please Choose 1 or 2.")

    if myDialogueQuestCA == "1":
        text = "You wait in a corner like a noob and kill him as he passes by." 
        text = "Good job but you can't win playing it safe like that."
        QuestCB()

    
    if myDialogueQuestCA == "2":
        text = "You move up some stairs and he's looting in a room."  
        computerQuestCA = randint(1,10)
        if computerQuestCA > 3:
            text = "You start unloading on this noob and mow him down before he opens the chest."  
            text = "Great job."  
            QuestCB()

        else:
            text = "Your slow to shoot him and he manages to jump around dodging your bullets then kills you."  
            text = "Get your game up."    
            text = "Please play again"  
            done()

def QuestCB():
    text = "You open the chest and gather ammo, bandages, and some small shields."  
    text = "The storm is forming around Greasy Grove."  
    text = "You looted everything so you dip away from Shifty Shafts."  
    text = "There's a small house on your route so you loot it out and gather ammo, building material, and a Golden SCAR. Now you better win"
    text = "There's gun fire from a distance so you go and investigate. A black Knight just killed someone and he looks like a pro."
    myDialogueQuestCB = screenText.textinput("Fortnite", "1. Engage from the high ground? Or 2. Let him pass? Please Choose 1 or 2.")

    if myDialogueQuestCB == "1":
        text = "You pop up from the hill and destroy this guy. Wow what a confidence booster! He must be so mad."
        QuestCC()
    else:
        text = "You let him pass even though you probably could've killed him."  
        text = "Let's hope he doesn't find you later." 
        QuestCC() 


def QuestCC():
    text = "Your outside the safe zone from the storm so you move in and begin building a tall fort."
    text = "12 players left."
    text = "You mow down two noobs running into the safe zone and wait till the numbers windle down to 2."
    text = "You start getting grenade launched, your fort is destroyed, and your pinned with fire. You must try and engage."
    computerQuestCC = randint(1,10)
    if computerQuestCC > 7:
        text = "You build a quick fort and drill him with bullets to his death"  
        text = "#1 VICTORY ROYALE"
        text = "Good Job!!!"  
        done()
        
    else:
        text = "You jump out to shoot him and an grenade slams you right in the chest."  
        text = "You tried your best, there was nothing else to do."  
        text = "Sorry."  
        text = "Please play again"  
        done()