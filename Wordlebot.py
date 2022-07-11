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
    allwords = []
    def __init__(self):
        words = open(r"5lwords.txt", "r")
        self.allwords = words.readlines()
      
    def update(self, guess, outcome, allwords):
        currword = [char for char in guess]
        curroutcome = [char for char in outcome]
        updatedwords = []
        include = True
        for word in allwords:
            iword = [char for char in word]
            for i in range(5):
                if curroutcome[i] == 'G':
                    self.green()
                elif curroutcome[i] == 'B':
                    self.black()
                elif curroutcome[i] == 'Y':
                    self.yellow()
                    pass
            
            if include:
                updatedwords.append(word)
        
        self.allwords = updatedwords
    
    def green():
        return
    
    def yellow():
        return
    
    def black():
        return
    
    def evaluate():
        return
    
    def printer(self):
        print("\nThere are {} possible words.".format(len(self.allwords)))
        print("The possible words are as follows: \n{}".format(self.allwords))
    


game = Gamestate()   
game.update(guess1.lower(), outcome1.upper(), game.allwords)
game.printer()
        