# CapitaLab


## Problem statement

Implement in python a poker hand comparison (5 cards vs 5 cards). Use it on the attached file (poker.txt) so that your program must tell within that file how many hands are won by player 1, by player 2 and how many are draws. Each row represents a new pair of hands. The first five cards of each row should be interpreted as the hand of player 1, and the second five cards represent the hand of player 2.

To make it simple, you can ignore the rule that higher cards win (i.e. assume that 4 Kings draw with 4 Aces)  and implement the following order:

Flush Straight (All cards are consecutive values of same suit) > Four of a Kind (Four cards of the same value) >  Full House (Three of a kind and a pair) > Flush (All cards of the same suit) > Straight (All cards are consecutive values) > Three of a Kind (Three cards of the same value) > Two Pairs (Two different pairs) > One Pair (Two cards of the same value) > Regular hand (No pair, no flush, no straight)


## Run Solution

Make sure your current working directory is the CapitaLab folder `path_to_folder/CapitaLab`. Then you can run the solution to see results:
```
python solution.py
```
After running the above command you should see in the terminal:
```
Player 1 won 235 hands.
Player 2 won 398 hands.
There were 367 ties.
```

At the end of the `solution.py` file we have the entry point:
```
if __name__ == '__main__':
    DEBUG_MODE = False
    player1, player2 = read_data()
    main(player1, player2)
```


- `DEBUG_MODE` variable is set to False by default. Change it to True if you want to print results from each individual hand of the players.

## Assumptions
- I assume each row of `poker.txt` has 10 hands, and each hand is a string of 2 characters.
- I assume the first 5 hands belong to the first player and the next 5 hands belong to the second player
- I assume card numbers are 2,3 ... 9, T, J, Q, K, A.

## Further improvements
- Check if data input is of valid hands (e.g nobody has 5 kings, player1 kings + player2 <= 4 )
- Run unit tests
- Include high cards rule

