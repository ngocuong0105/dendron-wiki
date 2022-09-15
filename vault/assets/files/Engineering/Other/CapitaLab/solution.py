from typing import List
from collections import Counter

def read_data(path = 'poker.txt'):
    with open (path, 'r') as myfile:
        hands = myfile.read().splitlines()
        player1 = [h.split(' ')[:5] for h in hands]
        player2 = [h.split(' ')[5:] for h in hands]
    return player1, player2

def is_straight_flush(hand: List[str]) -> bool:
    return is_flush(hand) and is_straight(hand)

def is_four_of_a_kind(hand: List[str]) -> bool:
    numbers = [s[0] for s in hand]
    counter = Counter(numbers)
    return any(val == 4 for val in counter.values())

def is_full_house(hand: List[str]) -> bool:
    numbers = [s[0] for s in hand]
    counter = Counter(numbers)
    if len(counter.keys()) != 2: return False
    key1,key2 = tuple(counter.keys())
    return min(counter[key1],counter[key2]) == 2 and max(counter[key1],counter[key2]) == 3

def is_flush(hand: List[str]) -> bool:
    suits = [s[-1] for s in hand]
    return len(set(suits)) == 1

def is_straight(hand: List[str]) -> bool:
    mp = {'T':10, 'J':11, 'Q': 12, 'K': 13, 'A':1}
    numbers = []
    for s in hand:
        if s[0] in mp:
            numbers.append(mp[s[0]])
        else:
            numbers.append(int(s[0]))
    numbers.sort()
    if numbers == [1,10,11,12,13]: return True
    return all(numbers[i] - numbers[i-1] == 1 for i in range(1,len(numbers)))

def is_three_of_a_kind(hand: List[str]) -> bool:
    numbers = [s[0] for s in hand]
    counter = Counter(numbers)
    return any(val == 3 for val in counter.values())

def is_two_pair(hand: List[str]) -> bool:
    numbers = [s[0] for s in hand]
    counter = Counter(numbers)
    pairs = 0
    for val in counter.values():
        pairs += (val==2)
    return pairs == 2

def is_one_pair(hand: List[str]) -> bool:
    numbers = [s[0] for s in hand]
    counter = Counter(numbers)
    pairs = 0
    for val in counter.values():
        pairs += (val==2)
    return pairs == 1

def get_hand_rank(hand: List[str]) -> int:
    if is_straight_flush(hand):
        return 8
    elif is_four_of_a_kind(hand):
        return 7
    elif is_full_house(hand):
        return 6
    elif is_flush(hand):
        return 5
    elif is_straight(hand):
        return 4
    elif is_three_of_a_kind(hand):
        return 3
    elif is_two_pair(hand):
        return 2
    elif is_one_pair(hand):
        return 1
    else:
        return 0

def compare_hands(hand1: List[str], hand2: List[str]) -> int:
    rank1 = get_hand_rank(hand1)
    rank2 = get_hand_rank(hand2)
    if rank1 > rank2:
        return 1
    elif rank1 < rank2:
        return -1
    else:
        return 0

def get_winner(player1: List[str], player2: List[str]) -> int:
    return compare_hands(player1, player2)

def main(player1: List[List[str]], player2: List[List[str]]) -> None:
    p1_wins, p2_wins, ties = 0, 0, 0
    for i in range(len(player1)):
        result = get_winner(player1[i], player2[i])
        if DEBUG_MODE:
            print()
            print('Rank P1: ', get_hand_rank(player1[i]),' ', 'Rank P2: ', get_hand_rank(player2[i]))
            print('P1:', player1[i], ' ', 'P2: ', player2[i])
        if result == 1:
            p1_wins += 1
        elif result == -1:
            p2_wins += 1
        else:
            ties += 1
    print("Player 1 won {} hands.".format(p1_wins))
    print("Player 2 won {} hands.".format(p2_wins))
    print("There were {} ties.".format(ties))


if __name__ == '__main__':
    DEBUG_MODE = False
    player1, player2 = read_data()
    main(player1, player2)