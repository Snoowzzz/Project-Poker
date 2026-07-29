# poker hand guesser


def handguesser():
    if zero_count == 5:
        print("Bad Luck! You have a Bluff") 
    elif zero_count == 3:
        print("You have a one pair")
    elif zero_count == 0:
        print("WOOH!! Congrats you have a FULL HOUSE")
    elif zero_count == 2:
        print("Nice you have THREE of a kind")
    elif zero_count == 1 and twopaircount>0:
        print("Good You have a two pair")
    else:
        print("OH MY GOD!!! You have FOUR OF A KIND")
       # MAIN SECTION OF THE CODE
print("Welcome to Poker Master \nRules are print the number on your card")
print("For face cards use '11' for J '12' for Q '13' for K and '14' for Ace")
hand = []
i =0
hand_count = 0
while i in range(5):
    card = int(input("Enter the number on your hand: "))
    if 0< card<15:
     hand.append(card)
     i = i+1
      # if after this entry we have 5 cards, check they are not all identical
    if len(hand) == 5:
     for card_value in hand:
        if hand.count(card_value) == 5:
            print("Invalid! You cannot have five cards of the same kind!!")
            hand = []
            i = 0
            break
    # if invalid card value
    
    
print(f"Your hand is {hand}")
count = [0,0,0,0,0]
k = 0
l = 0
# Fixed counting section
for k in range(5):         
    for l in range(5):      
        if k != l:          
            if hand[k] == hand[l]:
                count[k] += 1
#The single factor which will decide what kind of pair you have
zero_count = 0
for i in range(5):
        if count[i] == 0:
            zero_count+=1
#Special section to check if it is four of a kind or two pair
twopaircount = 0

for i in range(5):
        if count[i] == 1:
            twopaircount+=1
handguesser()
