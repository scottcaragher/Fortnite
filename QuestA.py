#first stage of questA
def QuestAA():
    text = "You land on a brick building and pick up a green pump shotgun."
    #70% chance of survival
    computerQuestAA = randint(1,10)
    if computerQuestAA > 3:
        #survived
        text = "Another player lands next to you and you quickly eliminate him with two shots. Good job!"
        QuestAB()
    #died
    else:
        text = "Another player lands on the roof, breaks the ceiling, and one pumps you in the head with a shotgun."
        text = "You have been eliminated."
        text = "Sorry."
        text = "Please play again"
        done()

#second stage of questA
def QuestAB():
    text = "You collect a big shield potion, an Assault Rifle, and a medkit. The storm forms around Loot lake. You drink the sheild and now you have 50% shield"
    text = "As your making your way down the building you hear footsteps getting closer and louder!"
    #user input to hide in bathroom or fight
    myDialogueQuestAB = screenText.textinput("Fortnite", "1. Hide in the bathroom? 2. Or wait for him to get close enough to battle it out? Please Choose 1 or 2.")

    #Hide choice
    if myDialogueQuestAB == "1":
        text = "He runs up the stairs, opens the door looking for ammo, and 360 no scopes you to the head." 
        text = "How are you suppose to win Fortnite Battle Royale hiding in the bathroom? Pathetic." 
        text = "Think about your actions and what kind of player you want to be then play again."
        done()

    #fight choice
    if myDialogueQuestAB == "2":
        text = "He runs up the stairs and you figure out that he's a noob."  
        #70% of survival
        computerQuestAB = randint(1,10)
        #survived
        if computerQuestAB > 3:
            text = "You shotgun him 3 times to the head and he is eliminated but, he hit you twice with the heavy shotgun."  
            text = "You now have 90 health and no sheild, but picked up his blue bolt action sniper."  
            text = "Tilted Towers seems quite now so you move in on loot lake."
            QuestAC()
        #died
        else:
            text = "Your slow to shoot him and he headshots you. Wow, your the real noob."  
            text = "You have been eliminated."  
            text = "Sorry."  
            text = "Please play again"  
            done()

#third stage of questA
def QuestAC():
    text = "Along the way you collect some wood material to build later on."  
    text = "There are 10 other players remaining."  
    text = "Someone starts shooting at you from 50 yards away, you immediately build up a fort."  
    #user input to choose which weapon to use
    myDialogueQuestAC = screenText.textinput("Fortnite", "1. Use your sniper? Or 2. Assault Rifle? Please Choose 1 or 2.")

    #sniper choice
    if myDialogueQuestAC == "1":
        text = "You missed several shots and he built up close to you and killed you with his submachine gun."
        text = "Please try again."  
        done()
    
    #Rifle choice
    if myDialogueQuestAC == "2":
        text = "You see him running up and start drilling him with the Assault Rifle."  
        text = "You eliminated him, easy peasy."  
        text = "5 players left and the storm is in the middle of your base. You improve and ready your fort."  
        text = "You hear some other players battling it out and one has an RPG."
        text = "You watch two fights go down and now there's 3 players left."
        text = "One of the players is healing up so you dome him in the head with your sniper, one enemy left."
        QuestAD()

#fourth stage of quest A
def QuestAD():
    text = "Your both outside the safe zone from the storm so you move in and begin building a tall fort."
    text = "You seem him hide in a small hut."
    #user input to fight or stay back
    myDialogueQuestAD = screenText.textinput("Fortnite", "1. Engage him? 2. Stay in your fort for protection? Please choose 1 or 2.")

    #engage and win
    if myDialogueQuestAD == "1":
        text = "You begin your way to the hut and shotgun him once, he hits you, you hit him again with the pump, he misses, and you kill him for the win."
        text = "#1 VICTORY ROYALE!"
        text = "Great work"
        done()
    
    #stay back
    if myDialogueQuestAD == "2":
        text = "You gave him time to heal and prepare to fight, he engages and now your pinned."
        text = "Your low with health now and he runs up on the fort and kills you."
        text = "You were so close but always engage."
        text = "Please play again."
        done()
        
    


