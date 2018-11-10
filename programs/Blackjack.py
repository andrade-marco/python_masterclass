# Blackjack
import random
import tkinter


# Loading cards
def loadImages(cardImages):
    suits = ['heart', 'club', 'diamond', 'spade']
    faceCards = ['jack', 'queen', 'king']
    # For each suit retrive images for cards
    for suit in suits:
        # First number cards
        for card in range(1, 11):
            name = '../data/cards/{}_{}.png'.format(str(card), suit)
            image = tkinter.PhotoImage(file=name)
            cardImages.append((card, image))
        # Face cards
        for card in faceCards:
            name = '../data/cards/{}_{}.png'.format(str(card), suit)
            image = tkinter.PhotoImage(file=name)
            cardImages.append((10, image))


# Scoring hand
def scoreHand(hand):
    # Calculate the total score of all cards in the list
    # Only one ace can have the value of 11
    score = 0
    ace = False
    for card in hand:
        cardValue = card[0]
        if cardValue == 1 and not ace:
            ace = True
            cardValue = 11
        score += cardValue
        if score > 21 and ace:
            score -= 10
            ace = False
    return score


# Dealing cards
def dealCard(frame):
    # Pop the next card off the top of the deck
    nextCard = deck.pop(0)

    # add the image to a Label and display the label
    tkinter.Label(frame, image=nextCard[1], relief='raised').pack(side='left')

    return nextCard


def dealDealer():
    dealerScore = scoreHand(dealerHand)
    while 0 < dealerScore < 17:
        dealerHand.append(dealCard(dealerCardFrame))
        dealerScore = scoreHand(dealerHand)
        dealerScoreLabel.set(dealerScore)

    playerScore = scoreHand(playerHand)
    if playerScore > 21:
        resultText.set('Dealer wins!')
    elif dealerScore > 21 or dealerScore < playerScore:
        resultText.set('Player wins!')
    elif dealerScore > playerScore:
        resultText.set('Dealer wins!')
    else:
        resultText.set('Draw!')


def dealPlayer():
    playerHand.append(dealCard(playerCardFrame))
    playerScore = scoreHand(playerHand)
    playerScoreLabel.set(playerScore)
    if playerScore > 21:
        resultText.set('Dealer wins!')

# Starting a new game
def startNewGame():
    global dealerCardFrame
    global playerCardFrame

    # Update hands and results
    del dealerHand[:]
    del playerHand[:]
    resultText.set('')

    # Destroy and recreate card frames
    createCardFrames(False)
    initGame()

# Initializing game
def initGame():
    global deck
    deck = list(cards)
    random.shuffle(deck)
    dealPlayer()
    dealerHand.append(dealCard(dealerCardFrame))
    dealerScoreLabel.set(scoreHand(dealerHand))
    dealPlayer()


# Creating card frames
def createCardFrames(isNew):
    global dealerCardFrame
    global playerCardFrame

    if not isNew:
        dealerCardFrame.destroy()
        playerCardFrame.destroy()

    dealerCardFrame = tkinter.Frame(cardFrame, background='green')
    playerCardFrame = tkinter.Frame(cardFrame, background='green')
    dealerCardFrame.grid(row=0, column=1, sticky='ew', rowspan=2)
    playerCardFrame.grid(row=2, column=1, sticky='ew', rowspan=2)


# Function to actually run the game
def play():
    initGame()
    root.mainloop()


# Setting up root window
root = tkinter.Tk()
root.title('Black Jack')
root.geometry('640x480')
root.configure(background='green')

# Set up the screen and frames for the dealer and player
resultText = tkinter.StringVar()
result = tkinter.Label(root, textvariable=resultText)
result.grid(row=0, column=0, columnspan=3)

cardFrame = tkinter.Frame(root, relief='sunken', borderwidth=1, background='green')
cardFrame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

dealerScoreLabel = tkinter.IntVar()
playerScoreLabel = tkinter.IntVar()

tkinter.Label(cardFrame, text='Dealer', background='green', fg='white').grid(row=0, column=0)
tkinter.Label(cardFrame, textvariable=dealerScoreLabel, background='green', fg='white').grid(row=1, column=0)
tkinter.Label(cardFrame, text='Player', background='green', fg='white').grid(row=2, column=0)
tkinter.Label(cardFrame, textvariable=playerScoreLabel, background='green', fg='white').grid(row=3, column=0)

# Buttons
buttonFrame = tkinter.Frame(root)
dealerButton = tkinter.Button(buttonFrame, text='Dealer', command=dealDealer)
playerButton = tkinter.Button(buttonFrame, text='Player', command=dealPlayer)
newGameButton = tkinter.Button(buttonFrame, text='New Game', command=startNewGame)
buttonFrame.grid(row=3, column=0, columnspan=3, sticky='w')
dealerButton.grid(row=0, column=0)
playerButton.grid(row=0, column=1)
newGameButton.grid(row=0, column=2)

# Initializing game
# Initializing cards and hands
cards = []
dealerHand = []
playerHand = []

# Load cards, create frames for holding cards, and initialize game
loadImages(cards)
createCardFrames(True)


# Only execute the code if called directly (not imported as module)
if __name__ == '__main__':
    play()
