#stage 1
def QuestBA():
    text = "You land on the roof of a house with another player"
    #user input choice
    myDialogueQuestBA = screenText.textinput("Fortnite", "1. Axe him to death? 2. Or break the roof and find a gun? Please Choose 1 or 2.")

    if myDialogueQuestBA == "1":
        text = "You run over and start axing him and land 2 hits dealing only 20% damage before he breaks the ceiling and grabs the shotgun." 
        text = "He shoots you three times and now you are dead."
        text = "Was it worth the low damage you caused?? Always go for the gun."
        text = "Please play again"
        done()
   
    if myDialogueQuestBA == "2":
        text = "You both start breaking the ceiling, there's a chest on his side but you see an Assault Rifle behind you."  
        #60% of survival
        computerQuestBA = randint(1,10)
        if computerQuestBA > 4:
            text = "You start unloading on this noob and mow him down before he opens the chest."  
            text = "Great job."  
            QuestBB()
        else:
            text = "Your slow to shoot him and he opens up the chest, grabs a legendary purple tactical shotgun and takes you down with a shot to the head."  
            text = "You tried your best."  
            text = "Sorry."  
            text = "Please play again"  
            done()

#stage 2
def QuestBB():
    text = "You open the chest and gather ammo, bandages, and some small shields."  
    text = "The storm is forming around Anarchy Acres."  
    text = "Your guns are not great so you dip away from Pleasant Park."  
    text = "There's a small house on your route so you loot it out and gather ammo, building material, and a Golden SCAR. Now you better win"
    text = "There's gun fire from a distance so you go and investigate. A black Knight just killed someone and he looks like a pro."
    #user input choice
    myDialogueQuestBB = screenText.textinput("Fortnite", "1. Engage from the high ground? Or 2. Let him pass? Please Choose 1 or 2.")

    if myDialogueQuestBB == "1":
        text = "You pop up from the hill and destroy this guy. Wow what a confidence booster! He must be so mad."
        QuestBC()
    else:
        text = "You let him pass even though you probably could've killed him."  
        text = "Let's hope he doesn't find you later." 
        QuestBC() 

#stage 3
def QuestBC():
    text = "Your outside the safe zone from the storm so you move in and begin building a tall fort."
    text = "12 players left."
    text = "You mow down two noobs running into the safe zone and wait till the numbers windle down to 3."
    text = "You start getting RPG'd, your fort is destroyed and your pinned with fire. You must try and engage."
    #40% chance of winning
    computerQuestBC = randint(1,10)
    if computerQuestBC > 6:
        text = "You build a quick fort and drill him with bullets to his death, you see the last noob hiding so you run up on him and kill him like a boss."  
        text = "#1 VICTORY ROYALE"
        text = "Good Job!!!"  
        done()
    else:
        text = "You jump out to shoot him and an RPG slams you right in the chest."  
        text = "You tried your best, there was nothing else to do."  
        text = "Sorry."  
        text = "Please play again"  
        done()