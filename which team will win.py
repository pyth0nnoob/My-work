import random
teamno1 = (0)
teamno2 = (0)

arsenal = (7.5)
chelsea = (7.9)
manchestercity = (8.8)
liverpool = (9.3)
wolves = (7.0)
tottenham  = (7.2)
sheffield = (7.0)
manchesterunited = (7.4)
leicester = (8.4)

team1 = (input("What is the name of the first team in the game"))
team2 =(input("What is the name of the second team in the game"))

if team1 == ("arsenal"):
    teamno1 = (arsenal)
elif team1 == ("chelsea"):
    teamno1 = (chelsea)
elif team1 == ("manchestercity"):
    teamno1 = (manchestercity)
elif team1 == ("manchesterunited"):
    teamno1 = (manchesterunited)
elif team1 == ("tottenham"):
    teamno1 = (tottenham)
elif team1 == ("wolves"):
    teamno1 = (wolves)
elif team1 == ("sheffield"):
    teamno1 = (sheffield)
elif team1 == ("liverpool"):
    teamno1 = (liverpool)
elif team1 == ("leicester"):
    teanmno1 = (leicester)


if team2 == ("arsenal"):
    teamno2 = (arsenal)
elif team2 == ("chelsea"):
    teamno2 = (chelsea)
elif team2 == ("manchestercity"):
    teamno2 = (manchestercity)
elif team2 == ("manchesterunited"):
    teamno2 = (manchesterunited)
elif team2 == ("tottenham"):
    teamno2 = (tottenham)
elif team2 == ("wolves"):
    teamno2 = (wolves)
elif team2 == ("sheffield"):
    teamno2 = (sheffield)
elif team2 == ("liverpool"):
    teamno2 = (arsenal)
elif team2 == ("leicester"):
    teanmno2 = (leicester)    

additionscore = (teamno1) + (teamno2)
roundedadditionscore = round(additionscore,0)
randomnumber = random.randint(1,roundedadditionscore)
drawchance = random.randint(1,4)

if drawchance != (1):
    if (randomnumber) <= (teamno1):
        print (str(team1 + " won the game!"))
    elif (randomnumber) >= (teamno2) and (randomnumber) <= (additionscore) :
        print (str(team2 + " won the game!"))  
    
else:
   print ("The game ended in a draw!") 
        
        

