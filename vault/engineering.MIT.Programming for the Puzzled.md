---
id: 2ic3ljkold03g223cujfbjz
title: Programming for the Puzzled
desc: ''
updated: 1660926370468
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