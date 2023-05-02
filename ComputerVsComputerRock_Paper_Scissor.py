import random 

def play():
    computerOne = random.choice(['rock', 'paper', 'scissors'])
    print(f"computerOne chose: {computerOne}")
    computerTwo = random.choice(['rock', 'paper', 'scissors'])
    print(f"computerTwo chose: {computerTwo}")

    if computerOne == computerTwo: 
        return 'tie'

    if is_win(computerOne, computerTwo):
        return 'ComputerOne won! ComputerTwo lost'
    
    return 'ComputerTwo won! ComputerOne lost'

def is_win(computerOne, computerTwo):
    #return true if computerOne wins
    #r>s s>p p>r
    if (computerOne == 'rock' and computerTwo == 'scissors') or (computerOne == 's' and computerTwo == 'p') or (computerOne == 'p' and computerTwo == 'r'):
        return True

print(play())


