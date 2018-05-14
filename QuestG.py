#stage 1
def QuestGA():
    text = "You land on a nice little house and pick up a pistol."
    #70% chance of survival
    computerQuestAA = randint(1,10)
    if computerQuestAA > 3:
        text = "Another player lands next to you and you quickly eliminate him. Good job!"
        QuestGB()
    else:
        text = "Another player lands on the roof, breaks the ceiling, and one pumps you in the head."
        text = "You have been eliminated."
        text = "Sorry."
        text = "Please play again"
        done()

def QuestGB():
    text = "You collect a pump shotgun, an Assault Rifle, and a medkit. The storm forms around Salty Springs."
    text = "You hear shots by the retail area."
    #user input choice
    myDialogueQuestGB = screenText.textinput("Fortnite", "1. Go towards Salty? 2. Or engage? Please Choose 1 or 2.")

    if myDialogueQuestGB == "1":
        text = "You leave anything that could have potentially harmed you." 
        text = "Why play the game if your not going to attack someone?" 
        QuestGC()

    if myDialogueQuestGB == "2":
        text = "You see 2 guys fighting so you wait till one dies."  
        #60% chance of survival
        computerQuestGB = randint(1,10)
        if computerQuestGB > 4:
            text = "You come up behind the player and use your shotgun to kill him. Good work."  
            QuestGC()
        else:
            text = "Your slow to shoot him and he headshots you with his shotgun."  
            text = "You have been eliminated."  
            text = "Sorry."  
            text = "Please play again"  
            done()

#stage 3
def QuestGC():
    text = "Along the way to Salty, you collect some wood material to build later on."  
    text = "There are 15 other players remaining."  
    text = "Someone starts shooting at you from afar, you immediately build up a fort."  
    #user input choice
    myDialogueQuestGC = screenText.textinput("Fortnite", "1. Use your pistol? Or 2. Assault Rifle? Please Choose 1 or 2.")

    if myDialogueQuestGC == "1":
        text = "Your pistol causes no damage and you die. Don't use a pistol."
        text = "Please try again."  
        done()
    
    if myDialogueQuestGC == "2":
        text = "You see him running up and start drilling him with the Assault Rifle."  
        text = "You eliminated him, easy money."  
        text = "5 players left and the storm is in the middle of your base. You improve and ready your fort."  
        text = "You hear some other players battling it out and one has an RPG."
        text = "You watch two fights go down and now there's 3 players left."
        text = "One of the players is healing up so you run up and kill him. One left."
        QuestGD()

#stage 4
def QuestGD():
    text = "Your both begin building and firing at each other."
    #user input choice
    myDialogueQuestGD = screenText.textinput("Fortnite", "1. make a move and attack? 2. Stay in your fort for protection? Please choose 1 or 2.")

    if myDialogueQuestGD == "1":
        text = "You begin attacking him and building for protection, your now real close. You pull out your shotgun build a ramp over his base, jump down on him and kill him with a headshot."
        text = "#1 VICTORY ROYALE!"
        text = "Great work."
        done()
    
    if myDialogueQuestGD == "2":
        text = "You run out of ammo with your rifle and now he's engaging."
        #50% chance of winning
        computerQuestGB = randint(1,10)
        if computerQuestGB > 5:
            text = "You gather the few shotgun shells you have left and wait for his arrival."
            text = "You jump out at him and barely kill him with 6 percent of health."
            text = "#1 VICTORY ROYALE!!!"
            text = "What a game."
            done()
        else:
            text = "He comes close as you make your last and final attack on him but he kills you with his hand cannon."
            text = "Nice try, you'll get him next time."
            done()
        

    