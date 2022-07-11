'''
//todo: 
'''

guess1 = input("\nHey! This is WordleBot! What's your first guess? \nGuess: ")
if len(guess1) != 5:
    print("ERROR: Words must be 5 letters long\n")
    exit()
outcome1 = input("\nWhat is the outcome? Input the colours you see! \n[ G for Green, B for black, Y for yellow ]\nInput: ")
if len(outcome1) != 5:
    print("ERROR: Outcome must be 5 letters long\n")
    exit()


class Gamestate:
    pastwords = []
    greenletters = []
    truecount, falsecount = 0, 0
    
    def __init__(self):
        words = open(r"5lwords.txt", "r")
        self.allwords = words.readlines()
      
    def updatewordlist(self, guess, outcome, allwords):
        Gamestate.pastwords.append(guess)
        guessword = [char for char in guess]
        curroutcome = [char for char in outcome]
        updatedwords = []
        for word in allwords:
            include = True
            iword = [char for char in word]
            for i in range(5):
                if curroutcome[i] == 'G':
                    Gamestate.greenletters.append(guessword[i])
                    if self.green(guessword[i], iword[i]) == False:
                        Gamestate.falsecount += 1
                        include = False
                        break
                elif curroutcome[i] == 'B':
                    if self.black(guessword[i], iword[i]) == False:
                        include = False
                        break
                elif curroutcome[i] == 'Y':
                    #include = self.yellow(guessword[i], iword[i])
                    break
            
            if include:
                updatedwords.append(word.strip())
                
        
        self.allwords = updatedwords
    
    def green(self, guesschar, ichar):
        if guesschar != ichar:
            return False
    
    def yellow(self, guesschar, ichar):
        if guesschar == ichar:
            return False
    
    def black(self, guesschar, ichar):
        if guesschar == ichar:
            return False
    
    def evaluate():
        return
    
    def printer(self):
        print("\nThe possible words are as follows: \n")
        print(*self.allwords, sep= " ")
        print("\nThere are {} possible words after {} guess.\n".format(len(self.allwords), len(Gamestate.pastwords)))
        print(Gamestate.truecount)
        print(Gamestate.falsecount)
    


game = Gamestate()   
game.updatewordlist(guess1.lower(), outcome1.upper(), game.allwords)
game.printer()

"""
guess2 = input("\nIf puzzle has been solved, input "Done", else input second guess \nGuess: ")
if guess2.lower() == "done":
    print("Congrats!")
    exit()
elif len(guess1) != 5:
    print("ERROR: Words must be 5 letters long\n")
    exit()
outcome2 = input("\nWhat is the outcome? Input the colours you see! \n[ G for Green, B for black, Y for yellow ]\nInput: ")
if len(outcome1) != 5:
    print("ERROR: Outcome must be 5 letters long\n")
    exit()
    
"""