# Progress
My first ever submission in leetcode was on 8th of January 2021. Did some Hackerrank for 2-3 months before that as I did
not know how to code (found it hard to press quickly stuff on the keyboard...). Started leetcoding more seriously mid Feb
2021 and have been doing it for 1.5 years so far (24 Jul 2022). Current leetcode count is solved **1526** problems. Main progress
stages were:
- first 3 months good learning curve Feb-Apr, but copy-pasted lost of solutions and failed to solve most of the problems alone. Got good progress on easy questions, mediums were very hard for me, hard were impossible.
- May rested a bit and slowed down the leetcoding
- June - August great learning curve, started to solve confidently easy questions, working way through medium alone. Hard
questions are still impossible to solve alone, but can understand solutions
- Sep - Dec stayed put and interviewed at companies so was chilling leetcode and tried to keep up the pace
- (2022) Feb - July: great learning curve, confidently solved easy and mediums. Started making progress on hards and for
some I am able to do by myself. Had one hard asked during interview and managed to finish in 40 minutes with working solution.

In summary: for now I am on descent coding level for interviews. For competitive programming, its another story... In leetcode I manged to be in top 2% with 2000+ rating, but in codeforces I would be blown out by those guys.

# Plans for the future
Ideally I would become a descent competitive programmer in 1-2 years (written in August 2022). Need to:
- do more leetcode competitions
- learn more advanced topics in CLRS
- take the MIT advance courses for algorithms and data structures
- learn C++
- start codeforces
- join Google/Facebook coding jams


Two years later Oct 2024 I haven't become a competitive programmer.
- I've bruteforced Leetcode and focused on quantity over quantity [MISTAKE]
- Now I'm trying to change that and I really spend time on solving hard problems, thiinking on them and solving them more than one time


**23.07.2022**

Went to my 21st competition. Solved 3/4 questions. The last one was hard level but it was super easy if you could get the idea. SUPER easy. I kind of gave up when saw that is hard level and there was big mental barrier. I should work on removing this mental barrier from my head. This increases significantly my chances of solving the question.
I lost 22 points in rating after the competition (2020 points now). Messed up one of the previous questions as well and got time penalties. Overall, I underperformed.


**08.10.2022**

Had 3 bad compatitions and lost a bit of rating. Last competiton went good - solved 4 problems under an hour and got rank around 600. Now rating is 2037. I started doing USACO and am currently in bronze division (easies one). Competitive programming problems seem much harder than leetcode. Some questions in bronze are diffficult,though most of them I am able to solve. But CP is whole another level compared with leetcoding.
Overall last two months I have been doing standard and a bit more hards unseen problems on leetcode and started competitive programming. Leetcode $\neq$ CP. In future I would probably need to learn C++, as Python code is sloooow. Also ordered a Leetcode pack (7800 leetcoins). It is flying from China to here!
I am more confident in solving hard questions in Leetcode now - say 5.5/10. Easy I am 10/10, medium I am 8.5/10.
Current leetcode count **1743** (08.10.2022)

**30.10.2022**

My best competition performance was yesterday - rank 125 on Biweekly 90. Today I hit new milestone **1800** Leetcode problems solved.


**20.01.2023**

Last year in December I hit the **2000** problems solved mark. Now I solve Leetcode casually and focus more on Kaggle.


**09.02.2023**

Hit another milestone of **2100** problems solved. **Two years of Leetcode.**

**26.02.2023**

Hit another milestone of **2200** problems solved.

**03.03.2023**

Solved all easy questions in leetcode and hit another milestone of **2300** problems solved. BG NAD VSICHKO

**06.06.2023**
Hit another milestone of **2405** problems solved. Only hard questions are left :(. 

**26.06.2023**
Hit another milestone of **2500** problems solved.

**07.09.2023**
Hit another milestone of **2600** problems solved.


# Tracking Leetcode Competitions

- Goal is to become **Guardian rating**

## Recap: Best Learnings
- The power of solving with pen and paper. The power of the hand.

## Biweekly Contest 141
- 12/10/2024
- Solved 3 problems

**What do I learned**
- Q4 was mathematical and I was rea;ly really close to solving it...
- binom and comb functions from scipy are not exact for large numbers
- `comb (exact = True)` !!
- For the hard problems you will need to do bottom up dp
- When I do competition I am much more focused and time flies quicker

## Weekly Contest 412
- 06/10/2024
- Solved 3 problems

**What do I learned?**
- I should have pushed further on the idea for problem 3! Was on right track and I knew what was wrong. Instead of trying to fix it I thought that the whole approach is wrong. In hindsight I know that there should have been some repetitive (cycle) idea otherwise the time constraints would be violated. I should have asked myself: "What are the things that I should definitely use here?". And after that try ideas for the not definite parts.
- 


## Biweekly Contest 138
- 04/10/2024
- Solved 3 problems

**What do I learned?**

- Last problem you should have followed your intuition. You started with a small example of two numbers and tried to generalize it. but you made a mistake in the generalizaton. When you played with the example you used the concrete numbers and based on the pattern you tried to generalize. Rather you should have tried to formalize with letters (ti*dj < tj*di) and this would have helped you to come up with a formula for two numbers then this would inspire you to generalize the correct way.

## Weekly Contest 413
- 03/10/2024
- Solved 3 problems

**What do I learned?**
- The third problem was a DP
- By looking at the problem constrained I should have thought sooner that I must have e problem subspace that is defined on the cell values
- [Fourth problem](https://leetcode.com/problems/maximum-xor-score-subarray-queries/description/). I was not able to solve it. I was on the right track and I should have looked at the drawing more. Again this problem could be solved only by hand first. Otherwise you'd not be able to solve it.


## BiWeekly Contest 140
- 02/10/2024
- Solved 2 problems (last two were very hard, 3rd has 16% AR, last one had 9% Acceptance rate)

**What do I learned?**
- [Third Problem](https://leetcode.com/problems/find-the-lexicographically-smallest-valid-sequence/description/)
- I tried solving the 3rd problem recursively going through all leaves of the tree. There was no way to DP the problem but I had clear idea of how to traverse the recursion tree
- Managed to write working solution but it TLE-ed.
- The reason I had to go from top to bottom of the tree is beacuse I needed forward looking information
- At this moment I should have started thinking of ways to store such information and fail fast
- Once I read the solution with the `last` array that stored the last chance of matching a letter in the target string, I could use this array (info) to **greedily** traverse the recursion tree
- This problem taught me to really understand the examples and whenever there is a choice to be made to be able to clearly formulate the choice (ideally in a programatic way)


## Weekly Contest 417

- 01/10/2024
- Solved all 4 problems

**What do I learned?**
- Don't be afraid of the hard. You solved the last hard problem without having any idea how to do it at first. You even thought about looking at the solution but you resisted the temptation.
- [Last problem] When you see thingsdoubleing in a problem, you should immediately think about bit manipulation, binary tree liftin etc
- [Third problem] writing down examples by hand was very powerful + writing the code etc. You should have this habbit, it will save you a lot of time. Don't just try it out in the code shell. This problem was a sliding window and it really helped to go with by hand.
- it also helped to come up with extra examples!

## Weekly Contest 416

- 30/09/2024
- Solved all 4 problems (with help for the last 2)


**What do I learned?**
- Last two problems were sliding window dictionary
- In order to solve this problem you really had to go through examples with hand
- Before you write code, you better go thorugh examples with hand. When you rush into coding it actually becomes slowe
- For sliding windows it is very important to:
    - get the indexing right
    - define the window structure, is it just 1 integer?, map + integer,set? etc. 
    - update the window structures correctly
    - when/how to add to the result
- come up with examples and WRITE DOWN WITH HAND

## Weekly Contest 414

Solved all 4 problems. 

**What do I learned?**
- Problem 3 [3282](https://leetcode.com/contest/weekly-contest-414/problems/reach-end-of-array-with-max-score/)
- Play around with example without looking at the expectedoutput. Just do it by yourself! Do no spoil the answer!
- This way you will likely try out the wrong path and understand the logic for going through the correct path
- In hindsight the problem looked like a DP, but in the end you were able to solve it using greedy. Often when problem constraints do not allow DP just think of Greedy approach

- Problem 4 [3283](https://leetcode.com/contest/weekly-contest-414/problems/maximum-number-of-moves-to-kill-all-pawns/)
- Two way DP function, where each DP depends on the other DP
- Often can see this in game theory problems with two players
- bitmasking, and just believe in yourself especially for problem 4
- the proper mindset will help you push through


## Weekly Contest 415

Solved only 2 problems. 

**What do I learned?**
- Problem 3 [3291](https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-i/description/)
- I learned how to implement a trie without adding a new class but just using a dictonary.
- I learned how to adhoc traverse the trie while I was solving the dp
- I learned in order to traverse the trie on demand it was important how to define the dp problem and its subspace/subproblems
- I learned that dp problems with string can be solved forward and backwards and they will result in different order of travering the problems. It turned out that going from right to left is better ad I could traverse the trie on demand character by character


- Problem 4 [3292](https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-ii/description/)
- I learned that KMP aaplication is ussually not obvious. You need to think a bit to reach to it
- KMP returns an array that tells you 'what is the longest preffix that is also a suffix'
