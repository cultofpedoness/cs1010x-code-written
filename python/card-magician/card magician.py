def card_magician(output, cards, trick):
    for card in cards:
        output = trick(output, card)
    return output

def compare_cards(card1, card2):
    c1 = 'Z' if card1[0] == 'A' else card1[0]
    c1 = 'Y' if card1[0] == 'K' else c1
    c1 = 'B' if card1[0] == 'T' else c1
    c2 = 'Z' if card2[0] == 'A' else card2[0]
    c2 = 'Y' if card2[0] == 'K' else c2
    c2 = 'B' if card2[0] == 'T' else c2
    return card1[1] > card2[1] if c1 == c2 else c1 > c2

cards = ('QS', 'AC', 'TD', 'JC', 'KH')

##def sort_deck(deck):
##    def sort_cards(output_tuple, card):
##        print(output_tuple)
##        output_final = ()
##        track = 0
##        for i in range(0, len(output_tuple)):
##            if compare_cards(card, output_tuple[i]):
##                output_final += (output_tuple[i],)
##                track += 1
##            else:
##                break
##        output_final += (card, output_tuple[track:])
##        return output_final
##                
##    a = (deck[0],)# Replace with your answer here.
##    b = deck[1:] # Replace with your answer here.
##    c = sort_cards # Replace with your answer here.
####    return card_magician(a, b, c)
##
##sorted_deck = sort_deck(cards)

#print(sorted_deck)

cards = ('7H', '3S', '6C', 'JH', '2H', '2S', 'TD')

def sort_suits(output, card):
    clubs = output[0]
    diamonds = output[1]
    hearts = output[2]
    spades = output[3]
    if card[1] == "C":
        clubs += (card,)
    elif card[1] == "D":
        diamonds += (card,)
    elif card[1] == "H":
        hearts += (card,)
    else:
        spades += (card,)
    
    return (clubs, diamonds, hearts, spades)

a = ((),(),(),(),) # Replace with your answer here.
b = cards # Replace with your answer here.
c = sort_suits # Replace with your answer here.

# Uncomment the following line.
split_deck = card_magician(a, b, c)

print(split_deck)


cards = ('AS', 'AC', 'TD', 'JC', 'AS', 'TD', 'QH')
 
a = ()
b = cards 
c = lambda tup, card: tup + (card,) if card not in tup else tup

unique_deck = card_magician(a, b, c)

print(unique_deck)

def card_magus(a, b, cards, trick, finalize):
    for card in cards:
        a, b = trick(a, b, card)
    return finalize(b, a)

def finalize(a, b):
    if not a:
        return b
    if not b:
        return a
    a = card_magus((), (), a, trick, finalize)
    b = card_magus((), (), b, trick, finalize)
    return a + b



def trick(a, b, card):
    if a == ():
        a += (card,)
    else:
        if compare_cards(card, a[0]):
            if b == ():
                b += (card,)
            else:
                if compare_cards(card, b[0]):
                    b += (card,)
                else:
                    a += (card,)
        else:
            a = (card,) + a
        
    return (a,b)        

# Uncomment the following line.
sorted_cards = card_magus((), (), ('TD', '4C', '6S', '9H', '3D', '5C', 'AH', 'KS', '2C', '7D', '8S', 'QC', 'JH'), trick, finalize)
print(sorted_cards)
