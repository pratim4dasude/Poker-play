def findPokerHand(hand):

    ranks=[]
    suits=[]
    possibleranks = []
    for card in hand:
        if len(card) ==2:
            rank=card[0]
            suit=card[1]
        else:
            rank=card[0:2]
            suit=card[2]
        # print(rank)
        if rank == 'A': rank = 14
        if rank == 'K': rank = 13
        if rank == 'Q': rank = 12
        if rank == 'J': rank = 11
        ranks.append(int(rank))
        suits.append(suit)

    # print(ranks,suits)

    # Royal Flush , straight , flush
    sortedranks = sorted(ranks)
    if suits.count(suits[0]) == 5:
        if 14 in sortedranks and 13 in sortedranks and 12 in sortedranks and 11 in sortedranks and 10 in sortedranks:
            possibleranks.append(10)
        elif all(sortedranks[i] == sortedranks[i-1]+1 for i in range(1,len(sortedranks))):
            possibleranks.append(9)
        else:
            possibleranks.append(6)

    #  straights
    # 10 11 12 13 14   --> 11 == 10+1

    if all(sortedranks[i] == sortedranks[i - 1] + 1 for i in range(1, len(sortedranks))):
        possibleranks.append(5)

    handuniqueval = list(set(sortedranks))
    #  fore of a kind
    #  3 3 3 3  # make it set so it will be unique and at last it will be 2 elemet ramiani

    if len(handuniqueval)==2:
        for val in handuniqueval:
            if sortedranks.count(val)==4: # 4 of a kind
                possibleranks.append(8)
            if sortedranks.count(val)==3: # full house
                possibleranks.append(7)

    #  3 of a kind
    #  3 unique value  and can be 2 pairs also
    if len(handuniqueval)==3:
        for val in handuniqueval:
            if sortedranks.count(val)==3: # three of a kind
                possibleranks.append(4)
            if sortedranks.count(val)==2: # two pairs
                possibleranks.append(3)

    # pair 4 uniqies

    if len(handuniqueval)==4:
        possibleranks.append(2)

    if not possibleranks:
        possibleranks.append(1)
        # pass

    pokerHandRanks = {10: "Royal Flush", 9: "Straight Flush", 8: "Four of a Kind", 7: "Full House", 6: "Flush",
                      5: "Straight", 4: "Three of a Kind", 3: "Two Pair", 2: "Pair", 1: "High Card"}
    # print(hand)
    output = pokerHandRanks[max(possibleranks)]
    print(hand , output)
    return output

if __name__ =="__main__":
    findPokerHand(["KH", "AH", "QH", "JH", "10H"])  # Royal Flush
    findPokerHand(["QC", "JC", "10C", "9C", "8C"])  # Straight Flush
    findPokerHand(["5C", "5S", "5H", "5D", "QH"])  # Four of a Kind
    findPokerHand(["2H", "2D", "2S", "10H", "10C"])  # Full House
    findPokerHand(["2D", "KD", "7D", "6D", "5D"])  # Flush
    findPokerHand(["JC", "10H", "9C", "8C", "7D"])  # Straight
    findPokerHand(["10H", "10C", "10D", "2D", "5S"])  # Three of a Kind
    findPokerHand(["KD", "KH", "5C", "5S", "6D"])  # Two Pair
    findPokerHand(["2D", "2S", "9C", "KD", "10C"])  # Pair
    findPokerHand(["KD", "5H", "2D", "10C", "JH"])  # High Card

