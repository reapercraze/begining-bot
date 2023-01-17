import random

class Card():
    def __init__(self, suit, face, value):
        self.suit = suit
        self.face = face
        self.value = value
        
    #A dunnder method to get card names 
    def __str__(self):
        return self.face + " of " + self.suit
        
class DeckOfCards():
    #blueprints for decks of cards
    def __init__(self):
        self.deck = []
        self.suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.faces = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        self.values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
        self.play_idx = 0
        
        for suit in self.suits:
            i = 0
            for i in range(len(self.faces)):
                self.deck.append(Card(suit, self.faces[i], self.values[i]))
                
    def shuffle_deck(self): #shuffle deck
        random.shuffle(self.deck)
        
    def print_deck(self): #print deck
        i = 0
        for card in self.deck:
            if i == 0:
                print(card.face, "of", card.suit, end = "")
                i +=1
            else:
                print(", ", card.face, "of", card.suit, end = "")
                i += 1
        return ""
    
    def deal_card(self): #Deal card to as next card in sequence 
        self.play_idx += 1
        return self.play_idx - 1

#createing the deck  
deck1 = DeckOfCards()

#printing and shuffling the deck
deck1.print_deck()
deck1.shuffle_deck()
print("\n\n")
deck1.print_deck()
print("\n\n\n\n")

#setting up the game
player_card1 = deck1.deck[deck1.deal_card()]
dealer_card1 = deck1.deck[deck1.deal_card()]
player_card2 = deck1.deck[deck1.deal_card()]
dealer_card2 = deck1.deck[deck1.deal_card()]
sum_player = player_card1.value + player_card2.value
sum_dealer = (dealer_card1.value + dealer_card2.value)

#Telling the user the game details
print("Thses are your cards:", player_card1, "and", player_card2)
print("Your score", sum_player)

#checking for blackjack
if sum_player == 21:
    print("You got Blackjack! You Won!!")
    exit()

#telling the user the dealer's face up card
print("The face up dealer card is:", dealer_card1)
print()


#ask user if they want to hit
good_input = 0
while good_input == 0:
    hit = input("Do you wish to hit? Yes/No: ")
    hit = hit[0].lower()
    if hit == "y":
        x = 0
        good_input += 1
    elif hit == "n":
        x = 1
        good_input += 1
    else:
        print("That wasn't Yes or No. Please try again: ")
        
# Continue hitting
while x == 0:
    sum_player += deck1.deck[deck1.deal_card()].value
    print("You got dealt a", deck1.deck[deck1.play_idx - 1])
    #to check if the user busted
    if sum_player > 21:
        print("Your score is:", sum_player)
        print("You busted. The dealers wins")
        exit()
    print("Your score is", sum_player)
    print()
    
    good_input2 = 0
    while good_input2 == 0:
        hit = input("Do you wish to hit? Yes/No: ")
        if hit == "y":
            good_input2 += 1
        elif hit == "n":
            good_input2 += 1
        else:
            print("That wasn't Yes or No. Please try again: ")
    if hit == "n":
        x += 1
        

#to deal for the dealer
print()
print("The dealer cards are", dealer_card1, "and", dealer_card2)
print("The dealer score is:", sum_dealer)
print()
while sum_dealer < 17:
    sum_dealer += deck1.deck[deck1.deal_card()].value
    print("The dealer got dealt a", deck1.deck[deck1.play_idx - 1])
    print()
if sum_dealer > 21:
    print("The dealer busted. You won!!")
    exit()
else:
    print("The dealer stands at", sum_dealer)
print()

#to see who wins
if sum_player > sum_dealer:
    print("Your score is higher than the dealer! You win!!")
elif sum_player < sum_dealer:
    print("Your score is less than the dealer. You lose.")
else:
    print("Your score is the same as the dealer. You push(tie) with the dealer")

#to ask the user if they want to play again