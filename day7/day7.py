from collections import Counter

CARD_VALUES = {
    'A': 'm',
    'K': 'l',
    'Q': 'k',
    'J': 'j', 
    'T': 'i',
    '9': 'h',
    '8': 'g',
    '7': 'f',
    '6': 'e',
    '5': 'd',
    '4': 'c',
    '3': 'b',
    '2': 'a'
}

def rank_hand_part_one(hand):
    hand_count = Counter(hand[0])
    rank = 0
    if len(hand_count) == 1:
        rank = 6
    elif len(hand_count) == 2:
        if max(hand_count.values()) == 4:
            rank = 5
        else:
            rank = 4
    elif len(hand_count) == 3:
        if max(hand_count.values()) == 3:
            rank = 3
        else:
            rank = 2
    elif len(hand_count) == 4:
        rank = 1

    return str(rank) + "".join([CARD_VALUES[c] for c in hand[0]])

CARD_VALUES_PART_TWO = {
    'A': 'm',
    'K': 'l',
    'Q': 'k', 
    'T': 'i',
    '9': 'h',
    '8': 'g',
    '7': 'f',
    '6': 'e',
    '5': 'd',
    '4': 'c',
    '3': 'b',
    '2': 'a',
    'J': 'A',
}

def rank_hand_part_two(hand):
    hand_count = Counter(hand[0])
    j_count = 0
    if 'J' in hand_count:
        j_count += hand_count['J']
        del hand_count['J']
    
    rank = 0
    if len(hand_count) <= 1:
        rank = 6
    elif len(hand_count) == 2:
        if (max(hand_count.values()) + j_count) == 4:
            rank = 5
        else:
            rank = 4
    elif len(hand_count) == 3:
        if (max(hand_count.values()) + j_count) == 3:
            rank = 3
        else:
            rank = 2
    elif len(hand_count) == 4:
        rank = 1

    return str(rank) + "".join([CARD_VALUES_PART_TWO[c] for c in hand[0]])

def day7(rank_hand):
    with open('input.txt', 'r') as f:
        hands = [line.split() for line in f.read().split('\n')]
        hands.sort(key=rank_hand)

        return sum((rank + 1) * int(hand[1]) for rank, hand in enumerate(hands))

if __name__ == "__main__":
    print(day7(rank_hand_part_one))
    print(day7(rank_hand_part_two))