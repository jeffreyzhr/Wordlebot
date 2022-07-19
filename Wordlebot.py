from operator import index

class Gamestate:
    pastwords = []
    greenletters = []
    yellowletters = []
    
    def __init__(self):
        words = open(r"5lwords.txt", "r")
        self.allwords = words.readlines()
      
    def update(self, guess, outcome, allwords):
        Gamestate.pastwords.append(guess.upper())
        guessword = [char for char in guess]
        curroutcome = [char for char in outcome]
        self.updatecolour(guessword, curroutcome)
        updatedwordlist = []
        
        for word in allwords:
            include = True
                
            for y in Gamestate.yellowletters: #asserts that word must contain yellow letter, position unknown (1) - Y
                if y not in word:
                    include = False
                    break
            
            iword = [char for char in word]
            for i in range(5):
                if curroutcome[i] == 'G': # letter at index i must be guess[i] - G
                    if iword[i] != guessword[i]:
                        include = False
                        break
                elif curroutcome[i] == 'Y': # letter at index i cannot be guess[i], works with (1) to build yellow - Y
                    if iword[i] == guessword[i]:
                        include = False
                        break
                elif curroutcome[i] == 'B': 
                    if iword[i] == guessword[i]:
                        include = False
                        break
                    if iword[i] not in Gamestate.greenletters and iword[i] not in Gamestate.yellowletters: # - BY, BG, B
                        if guessword[i] in word:
                            include = False
                            break
                
            #implement GY letters??
            
            if include:
                updatedwordlist.append(word.strip())

        self.allwords = updatedwordlist
    
    def updatecolour(self, guessword, curroutcome):
        for i in range(5):
            if curroutcome[i] == 'G' and guessword[i] not in Gamestate.greenletters:
                Gamestate.greenletters.append(guessword[i])
            elif curroutcome[i] == 'Y' and guessword[i] not in Gamestate.yellowletters:
                Gamestate.yellowletters.append(guessword[i])
                
    
    def evaluate(self, allwords):
        
        return allwords[0]
    
    def printer(self, bestguess):
        attempt_count = ['1st', '2nd', '3rd', '4th', '5th', '6th']
        print("\n" + "="*75)
        print("The possible words are as follows: \n")
        print(*self.allwords, sep= " ")
        print("\nThere are {} possible words after the {} guess.".format(len(self.allwords), attempt_count[len(Gamestate.pastwords) - 1]))
        print("\nThe bot recommends playing ---> '{}'".format(bestguess.upper()))
        print("="*75 + "\n")
    
    def printstats(self):
        print("\n" + "="*75)
        print("\nThanks for using WordleBot! I hope you've had fun!\n")
        print("***** You played the following {} words: *****".format(len(Gamestate.pastwords)))
        print(*Gamestate.pastwords, sep= ", ")
        print("")
        print("Starting with 5757 words, you've narrowed it down to {} words in {} guesses".format(len(self.allwords), len(Gamestate.pastwords)))
        print("coming soon: more stats!")
        print("\n" + "="*75)
        exit()
    
    def status(self, attempt):
        if (attempt == 0):
            print("\nHey! This is WordleBot! What's your first guess?")
        else:
            print("Please input {} guess!".format(attempt.upper()))
            print("If puzzle has been solved (5 greens), input 'DONE' for some stats!")
        guess = input("Guess: ")
        if guess.lower() == "done":
            self.printstats()
        if len(guess) != 5:
            print("ERROR: Words must be 5 letters long\n")
            exit()
        outcome = input("\nWhat is the outcome? Input the colours you see! \n[ G for Green, B for black, Y for yellow ]\nInput: ")
        if len(outcome) != 5:
            print("ERROR: Outcome must be 5 letters long\n")
            exit()
        
        return [guess, outcome]
    


game = Gamestate()

status = game.status(attempt=0)
game.update(status[0].lower(), status[1].upper(), game.allwords)
bestguess1 = game.evaluate(game.allwords)   
game.printer(bestguess1)

status2 = game.status(attempt= 'second')
game.update(status2[0].lower(), status2[1].upper(), game.allwords)
bestguess2 = game.evaluate(game.allwords)  
game.printer(bestguess2)   

status3 = game.status(attempt= 'third')
game.update(status3[0].lower(), status3[1].upper(), game.allwords)
bestguess3 = game.evaluate(game.allwords)  
game.printer(bestguess3)  

status4 = game.status(attempt= 'fourth')
game.update(status4[0].lower(), status4[1].upper(), game.allwords)
bestguess4 = game.evaluate(game.allwords)  
game.printer(bestguess4)

status5 = game.status(attempt= 'fifth')
game.update(status5[0].lower(), status5[1].upper(), game.allwords)
bestguess5 = game.evaluate(game.allwords)  
game.printer(bestguess5)  

status6 = game.status(attempt= 'sixth')
game.update(status6[0].lower(), status6[1].upper(), game.allwords)
game.printstats
