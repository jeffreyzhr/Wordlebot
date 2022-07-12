'''
//todo: 
'''

from operator import index


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
      
    def update(self, guess, outcome, allwords):
        Gamestate.pastwords.append(guess)
        guessword = [char for char in guess]
        curroutcome = [char for char in outcome]
        updatedwordlist = []
        #repeatedletters = [[i] for i in guessword if guessword.count(i) != 1]
        #repeatedletters = self.repeat_helper(guessword, curroutcome)

        #print(repeatedletters)
        print("guesssord: {}".format(guessword))
        
        for word in allwords:
            include = True
            iword = [char for char in word]
            for i in range(5):
                if curroutcome[i] == 'G':
                    #Gamestate.greenletters.append(guessword[i])
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
                updatedwordlist.append(word.strip())
                
        
        self.allwords = updatedwordlist
    
        
    def repeat_helper(self, guessword, curroutcome):
        wordarray = guessword.copy()
        print(wordarray)
        lst = [[i] for i in wordarray if guessword.count(i) != 1]
        for i in range(5):
            if wordarray[i] == lst[0]:
                print("lst: {}".format(lst[0]))
        return lst
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
        attempt_count = ['1st', '2nd', '3rd', '4th', '5th', '6th']
        print("\n" + "="*70)
        print("The possible words are as follows: \n")
        print(*self.allwords, sep= " ")
        print("\nThere are {} possible words after the {} guess.".format(len(self.allwords), attempt_count[len(Gamestate.pastwords) - 1]))
        print("="*70 + "\n")
        print(Gamestate.truecount)
        print(Gamestate.falsecount)
    


game = Gamestate()   
game.update(guess1.lower(), outcome1.upper(), game.allwords)
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