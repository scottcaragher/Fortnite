#stage 1
def QuestDA():
    text = "You land in a store building and pick up a green pump shotgun."
    #70% chance of survival
    computerQuestDA = randint(1,10)
    if computerQuestDA > 3:
        text = "Another player lands next to you and you quickly eliminate him with two shots. Good job!"
        QuestDB()
    else:
        text = "Another player lands on the roof, breaks the ceiling, and pumps you in the head with a shotgun."
        text = "You have been eliminated."
        text = "Sorry."
        text = "Please play again"
        done()

#stage 2
def QuestDB():
    text = "You collect a big shield potion, an Assault Rifle, crossbow, and a medkit. The storm forms around Shifty Shafts."
    text = "As your making your way around Greasy Grove, you hear footsteps in a house."
    #user input choice
    myDialogueQuestDB = screenText.textinput("Fortnite", "1. Hide in a bush and let him pass? 2. Or get ready to fight him? Please Choose 1 or 2.")

    if myDialogueQuestDB == "1":
        text = "He sees you from the roof, 360 no scopes you to the head, and starts giving you the L-Dance." 
        text = "How are you suppose to win Fortnite Battle Royale hiding in a bush? Noob status." 
        text = "Think about your actions and what kind of player you want to be then play again."
        done()

    if myDialogueQuestDB == "2":
        text = "You enter the house and he's on the second floor, you walk up the stair and then..."  
        #60% chance of survival
        computerQuestDB = randint(1,10)
        if computerQuestDB > 4:
            text = "you start shooting him with your shotgun till he's dead."  
            text = "good job, 2 kills!"  
            QuestDC()
        else:
            text = "He set up a trap on the ceiling and you accidently walk right into it."  
            text = "Hey, it happens to the best of us."  
            text = "Make sure to always check for traps."  
            text = "Please try again."  
            done()

#stage 3
def QuestDC():
    text = "Along the way you collect some wood material to build later on."  
    text = "There are 10 other players remaining."  
    text = "Someone starts shooting at you for 50 yards away, you immediately build up a fort."  
    #user input choice
    myDialogueQuestDC = screenText.textinput("Fortnite", "1. Use your crossbow? Or 2. Assault Rifle? Please Choose 1 or 2.")

    if myDialogueQuestDC == "1":
        text = "You missed several shots becuase the crossbow is terrible and he built up close to you and killed you with his submachine gun."
        text = "The only useful thing for a crossbow is the scope."
        text = "Play again."  
        done()
    
    if myDialogueQuestDC == "2":
        text = "You see him running up and start drilling him with the Assault Rifle."  
        text = "You eliminated him, easy peasy."  
        text = "5 players left and the storm is in the middle of your base. You improve and ready your fort."  
        text = "You hear some other players battling it out and one has an RPG."
        text = "You watch two fights go down and now there's 3 players left."
        text = "One of the players is healing up so you light him up with your rifle, one enemy left."
        QuestDD()

#stage 4
def QuestDD():
    text = "Your both outside the safe zone from the storm so you move in and collect some loot from your kills."
    text = "You pick up a, wait for it..., Golden RPG."
    text = "You engage instantly."  
    #70% chance of winning
    computerQuestDD = randint(1,10)
    if computerQuestDD > 3:
        text = "you start blowing him to pieces."
        text = "#1 VICTORY ROYALE!"
        text = "feels good to have this much power."
        done()
     else:
        text = "He dodges your shot, and you take too long to reload so he pummels you to your death."  
        text = "With great power comes great responsibility of knowing how to aim."  
        text = "An embarrassing way to die but maybe next time you'll do better."  
        text = "Play again."  
        done()


