# poker hand guesser


def handguesser():
    if zero_count == 5:
        if temp_count == 5:
            print("Congo you have a flush")
        else:
            print("BAD LUCK!! You have a bluff!")
    elif zero_count == 0:
        print("WOOH!! Congrats you have a FULL HOUSE")
    elif zero_count == 3:
        print("You have a one pair")
    elif zero_count == 2:
        print("Nice you have THREE of a kind")
    elif zero_count == 1 and twopaircount>0:
        print("Good You have a two pair")
    else:
        print("OH MY GOD!!! You have FOUR OF A KIND")
       # MAIN SECTION OF THE CODE
print("Welcome to Poker Master \nRules are Enter the number on your card")
print("For Face Cards use '11' for J '12' for Q '13' for K and '14' for Ace")
print("For Symbols use 'H' for Hearts 'S' for Spades 'C' for Club and 'D' for Diamonds ")
hand = []
symbol = []
symbol_list = ['H','S','C','D']
i =0
hand_count = 0
temp_count = 0
while i in range(5):
    card = int(input("Enter the number on your hand: "))
    if 0< card<15:  
     hand.append(card)
     symbol_card = str(input("Plz enter the symbol on your card: "))
         # check symbol against allowed list; only accept once per valid input
     valid_symbol = False
     for k in range(8):
            if symbol_card == symbol_list[k]:
             symbol.append(symbol_card)
             i = i+1
             valid_symbol = True
             break
     if not valid_symbol:
             print("Plz enter a valid symbol")
        
    else:
        print("Plz enter a valid number!!")
      # if after this entry we have 5 cards, check they are not all identical
    if len(hand) == 5:
     for card_value in hand:
        if hand.count(card_value) == 5:
            print("Invalid! You cannot have five cards of the same kind!!")
            hand = []
            symbol = []
            i = 0
            break
    # if invalid card value

  # The distinction factor
    merged_hand = [f"{s},{t}" for s,t in zip(hand,symbol)]
    duplicate_found = False
    for m in range(len(merged_hand)):
        for n in range(m + 1, len(merged_hand)):
            if merged_hand[m] == merged_hand[n]:
                duplicate_found = True
                break
        if duplicate_found:
            break
    if duplicate_found:
        print("Invalid! Duplicate card entered.")
        break
if duplicate_found != True:
 print(f"Your hand is {merged_hand}")
for m in range(5):
    if symbol[m] == symbol[0]:
        temp_count+=1
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
