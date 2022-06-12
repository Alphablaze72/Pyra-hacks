import random
import time
ogre_health = 100
playerhealth = 100
def main():
    print('Hello fellow traveller Lets start you Journey')
    stdecision = input('You first make your way into a dungeon, you see a door what do you do?(open the door, head back up)')
    while stdecision != 'open the door':
        stdecision = input('You encounter a bear that is lbocking your way what do you do?(open the door, head back up)')
    count = 0
    while ogre_health > 0:
        if count == 0:
            secdecision = input('After you open the door, you see a ogre standing gurad over the treasure that is meant to be your. What do you do?(Jab the ogre in the eye,hit the ogre in the leg, sneak past the ogre')
        else:
            secdecision =input('What do you do now, the ogre is still standing(Jab the ogre in the eye,hit the ogre in the leg, try to sneak past hjim to teh trsture')
        if secdecision == 'Jab the ogre in the eye':
            if prob(80) == True:
                ogre_health = ogre_health-40
                print('That hit was effective')
            
        elif secdecision == 'hit the ogre in the eye':
            if prob(40) == True:
                ogre_health = ogre_health-20
                print('That hit was effective')
            else:
                ogre_health = ogre_health -10
                playerhealth = playerhealth-50
        elif secdecision == 'sneak past the ogre':
            if prob(90) == True:
                print('You have won the game, you have reacher the old treasure')
            else:
                print(' you have lost the game, while trying to sneak past the ogre, you missteppe4d on a piece of twig thus alerting the ogre of your presense and killing you entirely')
                
def prob(probability):
    dice_roll = random.randint(1, 100)
    if dice_roll>probability:
        return True
    else:
        return False
