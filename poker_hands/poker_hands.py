from collections import Counter

SUITS = ["C", "D", "H", "S"]
RANKS = ["", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]

def straight(hand):
    ranks_high = sorted([(14 if card._rank == 1 else card._rank) for card in hand])

    return (
        (
            ranks_high[-1] - (len(hand) - 1) == ranks_high[0]
        )                                                        
        and len(set(hand)) == len(hand)                          
    )

def build_dict(hand):
    dict = {}

    for card in hand:
        dict[card._rank] = dict.get(card._rank, 0) + 1

    return dict

def full_house(hand):
    if pair(hand) and four_of_a_kind(hand):
        return True

def one_pair(dict):

    hand_dict = dict(Counter(hand))
    print(hand_dict)
    for i in hand:
        if hand_dict.get(i) == 2:
            return True

def two_pairs(dict):
    num = 0
    hand_dict = dict(Counter(hand))
    print(hand_dict)
    for i in hand:
        if hand_dict.get(i) == 2:
            num += 1
            if num == 2:
                return True

def three_of_a_kind(dict):

    hand_dict = dict(Counter(hand))
    print(hand_dict)
    for i in hand:
        if hand_dict.get(i) == 3:
            return True


""" def remove_suit(hand):
    num_list = []
    suits = 'DCSH '
    for i in hand:
        if not i in suits:
            num_list.append(i)
    return sorted(num_list)  """

def straight_flush(hand):
    if flush(hand) and straight(hand):
        return True
  

def flush(hand):
    Diamonds = []
    Clubs = []
    Spades = []
    Hearts = []

    hand_split = hand.split(' ')
    for suit in hand_split:
        for i in suit:
            if 'D' in i:
                Diamonds.append(i)
            if 'C' in i:
                Clubs.append(i)
            if 'S' in i:
                Spades.append(i)
            if 'H' in i:
                Hearts.append(i)

    if len(Diamonds) == 5:
        return True
    if len(Clubs) == 5:
        return True
    if len(Spades) == 5:
        return True
    if len(Hearts) == 5:
        return True

""" def high_card(hand):
    if not flush(hand)  """

def main():
    #allow the user to input hand one as well as give them instructions on how
    hand = input("Enter 5 cards beginning with the Value (denoted by 2, 3, 4, 5, 6, 7, 8, 9, T, J, K, A) and a suit (denoted by C, D, H, S) seperated by a space. The suit has no impact on the value. Ex. 2H 3D 5S 9C KD: ").upper()


    if straight(hand) == True:
        print("Straight")


main()



