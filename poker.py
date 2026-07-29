# poker hand guesser
print("Welcome to Poker Master \n Rules are print the number on your card")
print("For face cards use '11' for J '12' for Q '13' for K and '14' for Ace")
hand = []
i =0
while i in range(5):
    card = int(input("Enter the number on your hand: "))
    if 0< card<15:  
     hand.append(card)
     i = i+1
    else:
     print("Plz enter a valid card number: ")
    
print(f"Your hand is {hand}")
count = [0,0,0,0,0]
k = 0
l = 0
# Fixed counting section
for k in range(5):          # Look at each card one by one
    for l in range(5):      # Look at all other cards
        if k != l:          # Don't compare a card to itself
            if hand[k] == hand[l]:
                count[k] += 1

print(count)