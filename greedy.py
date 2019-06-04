import random

# finalScore = int(input("Play to?"))
# onBoard = int(input("Points to get on board?"))
finalScore = 10000
onBoard = 750
dice = [1, 1, 1 ,1, 1, 1]

class Player():
    def __init__(self):
        self.currentScore = 0
        self.totalScore = 0
    def Roll(self, dice):
        #Roll Dice
        print("Rollin them bones!")
        for x in range(len(dice)):
            dice[x] = random.randint(1,6)
        print(dice)
        if not checkForPoints(dice):
            self.Bust()
        else:
            self.ChooseDice(dice)

    def ChooseDice(self, dice):
        #Get input from user for dice to keep
        print("Choose dice to keep (i.e. y n y y y n)")
        toKeep = input()
        keepList = toKeep.split()
        self.currentHand = []
        for x in range(len(keepList)):
            if keepList[x] == 'y':
                self.currentHand.append(dice[x])

        print("current hand:", self.currentHand)
        calculatePoints(self, self.currentHand)
        print("current score:", self.currentScore)
        for y in range(len(self.currentHand)):
            dice.pop(dice.index(self.currentHand[y]))
        if len(dice) > 0:
            print("Keep going?")
            cont = input()
            if cont == 'y' or cont == 'ye' or cont == 'yes':
                print("dice left", dice)
                self.Roll(dice)
            else:
                self.Keep()
        else:
            print("Save your points!")
            resetDice()
            self.Roll(dice)

    def Keep(self):
        #Keep current hand's points
        self.totalScore += self.currentScore
        self.currentScore = 0
        resetDice()
        print("Keep this good shit")
        print("Total Score:", self.totalScore)

    def Bust(self):
        #Lose current hand and pass turn
        resetDice()
        self.currentScore = 0
        self.currentHand = []
        print("RIP")

print("Playing to:", finalScore, "Points to get on the board:", onBoard)

def checkForPoints(hand):
    # Return true if points. False if no points
    counts = [hand.count(1), hand.count(2), hand.count(3), hand.count(4), hand.count(5), hand.count(6)]
    if counts[0] > 0:
        return True
    elif counts[4] >0:
        return True
    elif counts.count(3) > 0 or counts.count(4) > 0 or counts.count(5) > 0:
        return True
    elif counts.count(2) > 2 or counts.count(1) > 5:
        return True
    else:
        return False

def calculatePoints(user, currentHand):
    if not checkForPoints(currentHand):
        print("Pick dice that have points")
        return 0
    else:
        counts = [currentHand.count(1), currentHand.count(2), currentHand.count(3), currentHand.count(4), currentHand.count(5), currentHand.count(6)]
        if counts.count(1) == 6 or counts.count(2) == 3 or (counts.count(2) == 1 and counts.count(4) == 1):
            user.currentScore += 1500
            pass
        elif counts.count(3) == 1:
            triple = counts.index(3)
            triple += 1
            if triple == 1:
                user.currentScore += 1000
            else:
                user.currentScore += (100 * triple)
        if counts[0] > 0 or counts[4] > 0:
            user.currentScore += (counts[0] * 100)
            user.currentScore += (counts[4] * 50)



def resetDice():
    dice = [1, 1, 1 ,1, 1, 1]

def main():
    user = Player()
    granny = Player()
    user.Roll(dice)


main()
