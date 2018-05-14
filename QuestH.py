def QuestHA():
    text = "You land on a restaurant and find a shotgun."
    computerQuestHA = randint(0,10)
    if computerQuestHA > 3:
        QuestHB()
        
    else:
        text = "Another player lands on the same building and kills you with a submachine gun."
        text = "You have been eliminated."
        text = "Sorry."
        text = "Please play again"
        done()

def QuestHB():
    text = "You collect an Assault Rifle, and a launch pad. The storm forms around tilted towers."
    text = "You head towards Tilted and see a piñata fall from the sky."
    myDialogueQuestHB = screenText.textinput("Fortnite", "1. Go check out the piñata? 2. Or keep moving? Please Choose 1 or 2.")

    if myDialogueQuestHB == "2":
        text = "You avoid the piñata which couldve been a potential trap." 
        QuestHC()

    
    if myDialogueQuestHB == "1":
        text = "You start opening the piñata."
        computerQuestHB = randint(0,10)
        if computerQuestHB > 4:
            text = "Someone snipes you because you didn't build protection around yourself."  
            text = "Always build protection."
            text = "please play again."
            done()

        else:
            text = "You gather an abundance of materials and ammo. Lucky you." 
            QuestHC()

def QuestHC(): 
    text = "There are 4 other players remaining as you head on to Tilted."  
    text = "Someone starts shooting at you from afar, you immediately build a great fort."  
    myDialogueQuestHC = screenText.textinput("Fortnite", "1. Use you Rifle? Or 2. Launch Pad outta there? Please Choose 1 or 2.")

    if myDialogueQuestHC == "1":
        computerQuestHC = randint(0,10)
        if computerQuestHC > 4:
            text = "Your slow to shoot him and he kills you."
            text = "Please try again."  
            done()
        else:
            text = "He's a noob so you kill him easily with such great protection of the base."
            QuestHD()

    if myDialogueQuestHC == "2":       
        text = "You see him running up so you take the easy road and evaid him with the launch pad."  
        QuestHD()

def QuestHD():
    text = "There's 3 players remaining and you build a fort in the zone. A guy lauches toward you."
    text = "You eliminate him in the air and now there's one opponent left."
    myDialogueQuestHD = screenText.textinput("Fortnite", "1. Engage him from 50 yards away? 2. Stay in your fort for protection? Please choose 1 or 2.")

    if myDialogueQuestHD == "1":
        text = "You begin attacking him and building for protection, your now real close. You pull out your shotgun and so does he but your faster to kill him."
        text = "#1 VICTORY ROYALE!"
        text = "Great work."
        done()
    
    if myDialogueQuestHD == "2":
        text = "Your rifle does little damage to his walls as he engages."
        computerQuestHB = randint(0,10)
        if computerQuestHB > 5:
            text = "You gather the few shotgun shells you have left and wait for his arrival."
            text = "You jump out at him kill him with 2 pumps to the head."
            text = "#1 VICTORY ROYALE!!!"
            text = "What a game."
            done()
        else:
            text = "He comes close as you make your last and final attack on him but he kills you with his sub machine gun."
            text = "Nice try, you'll get him next time."
            done()
        