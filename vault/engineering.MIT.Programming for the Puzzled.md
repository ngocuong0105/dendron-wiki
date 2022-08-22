---
id: 2ic3ljkold03g223cujfbjz
title: Programming for the Puzzled
desc: ''
updated: 1661033911222
created: 1660838449536
---
# MIT 6.S095 - Programming for the Puzzled

Lecture [videos](https://www.youtube.com/watch?v=14UlXIZzwE4&list=PLUl4u3cNGP62QumaaZtCCjkID-NgqrleA&index=1&ab_channel=MITOpenCourseWare)

Lecture [notes](https://ocw.mit.edu/courses/6-s095-programming-for-the-puzzled-january-iap-2018/)

## Puzzle 1. You Will All Conform. Trick

Array of people and they have caps on their head. These caps can be forward or backward.

0, 1, 2, 3, 4, 5, 6

F, B, F, F, B, B, F

We want all caps to conform, that is all are forward or all are backward. Possible operations: You can say to a person "
Flip your cap". Or you can say "People from position from 2 to 3 flip your caps". Find minimum number of operations given
an array of people with caps.

---

Simple solution is just to count forward and backward intervals

```Python
arr = ['F','B','F','F','B','F','F']

def solve(arr):
    forward, backward = [],[]
    i = 0
    while i < len(arr):
        j = i+1
        while j < len(arr) and arr[j] == arr[i]:
            j += 1
        if arr[i] == 'F': forward.append([i,j])
        else: backward.append([i,j])
    return min(len(forward),len(backward))
```

---
First person in line gives up what set of commands you will say to the people. For example if arr[0] = 'F', then you would say to all 'B-s' to flip their caps.

```Python

def please_all_conform(arr):
    arr.append('END')
    for i in range(1,len(arr)):
        if arr[i] != arr[i-1]:
            if caps[i] != caps[0]:
                print(f'Please people in positions {i}', end = '')
            else:
                print(f' through {i - 1} flip your caps!')

```

'Nuances with how you solve a problem and how you code it.'

## Puzzle 2. The Best Time to Party. Line Sweep

Celebrities come at a party at particular times (intervals). When should you go to the party to max out the number of celebrities you will meet.

```
[('Beyonce',6,7), ('Taylor',7,9), ...]
```
Closed intervals on the left and open on the right.

Simple solution. Check all hours (starts and ends) and check how many intervals contain it. Depends on granularity of time

```Python
def solve(intervals):
    start = min([intervals[i][0] for i in range(len(intervals))])
    end = max([intervals[i][1] for i in range(len(intervals))])
    times = set(starts + ends)
    res = 0
    for t in range(start,end+1):
        res = max(res,count(t),intervals)
    return res

def count(t):
    return sum([ s <= t < e for s,e  in intervals])

```
---
'Lots of repeated computation = redundancy. Often you could reduce this redundancy by computing things incrementally.'

The only times that are interesting is when celebrities come and leave

The only time the result could change is if a celebrity enters or leaves.

Line sweep solution.  Relies on the fact that the result would change only when you reach an event.

```Python
def solve(intervals):
    events = []
    for s,e in events:
        events.append((s,1))
        events.append((e,0))
    events.sort()
    res,curr = 0,0
    for time,is_start in events:
        if is_start:
            curr += 1
        else:
            curr -= 1
        res = max(res,curr)
    return res
```


# Puzzle 3: You Can Read Minds

Given a deck of 52 cards. William takes 5 cards at random and shows to Devas 4 of them. Devas uses an algorithm to determine the 5th card. He uses the info from the 4 cards he sees to guess the fifth card.


Show 4 cards, 5th card could be 1 of 48.

How many bits of information can 4 cards show? Use the order of the 4 cards gets you $4! = 24$. We have just 24 bits of information but have to encode 48. Ordering just uses the numbers on the cards, we need to use the suits.

**Strategy:**
First card will give away the suit. By pigeonhole principle out of 5 cards there would be 2 with the same suits. The other 3 cards would give away the distance from the first card thinking in circular/modular computation.

**Example:** We pick King Diamond, A Diamond, 2 Spade, 3 Clubs, 5 Hearts.

William will hide the Ace and present  K, 2, 3, 5.

Devadas sees King of Diamond, hence the  hidden card is a diamond. 2,3,5 is the first permutation, hence the hidden card is 1 distance away from the Kind, that is and Ace.

Why this strategy works? The first card is the pivot card giving away the suit, hence there are 12 cards remaining that could possibly be the hidden card. we have 3 cards left t encode the 12 cards. Because we measure distance only in clockwise direction we are covered.


Is it possible to pick 4 random cards, hide one of it and encode it using the rest 3.

[Article](https://codegolf.stackexchange.com/questions/165390/professor-at-mit-can-read-minds)



