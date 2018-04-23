QuestOne():
    textTurtle.write("You collect a big shield potion, an Assault Rifle, and a medkit. The storm forms around Loot lake. You drink the sheild and now you have 50% shield")
    textTurtle.write("As your making your way down the building you hear footsteps getting closer and louder!")
    myDialogueQuest1.1 = screenText.textinput("Fortnite", "Hide in the bathroom?(1) Or wait for him to get close enough to battle it out?(2) Please Choose 1 or 2")

    if myDialogueQuest1.1 == "1":
        textTurtle.write("He runs up the stairs and you figure out that he's a noob.")
    computerQuest1.1 = randint(1,10)
    if computerQuest1.1 > 3:
        textTurtle.write("You shotgun him 3 times to the head and he is eliminated but, he hit you twice with the heavy shotgun.")
        textTurtle.write("You now have 90 health and no sheild, but picked up his blue bolt action sniper.")
        textTurtle.write("Tilted Towers seems quite now so you move in on loot lake.")
        
    else:
        textTurtle.write("Your slow to shoot him and he headshots you. Wow, your the real noob.")
        textTurtle.write("You have been eliminated.")
        textTurtle.write("Sorry.")
        textTurtle.write("Please play again")
        done()

    textTurtle.write("Along the way you collect some wood material to build later on.")
    textTurtle.write("There are 10 other players remaining.")
    textTurtle.write("Someone starts shooting at you for 50 yards away, you immediately build up a fort.")
    myDialogueQuest1.2 = screenText.textinput("Fortnite", "Use your sniper?(1) Or Assault Rifle?(2) Please Choose 1 or 2")

    if myDialogueQuest1.2 == "1":
        textTurtle.write("You missed several shots and he built up close to you and killed you with his submachine")
        done()
    else:
        textTurtle.write("You see him running up and start drilling him with the Assault Rifle.")
        textTurtle.write("You eliminated him, easy peasy.")
        
    textTurtle.write("5 players left and the storm is in the middle of your base. You improve and ready your fort.")
    textTurtle.write("You hear some other players battling it out and one has an RPG.")
    textTurtle.write("")


