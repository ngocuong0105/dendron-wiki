
# Algorithms

**Steps**

1.  Ask questions:
    1.1 about input (size, values, all constraints, sorted, duplicates)
    1.2 find solution -> chekcif there is input data for which the solution does not exist
2. Play around with a examples (Visualize problem)
    2.1 Think edge cases (especially linked lists)
TTD Write tests before writing code!!!
3. Get brute force solution
4. Write all steps of the algorithm before actually writing it.
    4.1 Write interface functions first each, then implement!
    4.2 Power of abstraction, encapsulate your code by naming
             different  logics - get your spell!
5. Test code in you head out loud without running it


When you are asked about another solution to the problem:
- recursion vs iteration
- mention call stack, python is 10000 
- recursion smart way to procastinate work to be done later
- recursion cannot control memory
- can do tail recursion in compiled languages (C, C++, Lisp) reduce memory from O(n) -> O(1)
- Online vs Offline (Given input upfront vs Data Stream) often for Online you'd use Balanced Binary Search Tree

# Strategies:
- directly writing code is BAD, think conceptually first- not like you do leetcodede!!!!
- strategy of wishful thinking- when using Data Structures that are not implemented yet just image you have them, solve the problem and only after that design them
- linked list questions modularize functions!! [see power](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/submissions/)
- linked list often use two pointers
-  finding good examples and playing around them
- for monotonic stack problems better go through example and write steps before that

# Topics
- BST delete procedure picture of cases from Intro to algo book page 297, dbabichev recursive!
- power of 2 table 1KB,1MB..
- latency table in System Design book An insider guide
- BIT visualization
- Manachers Algorithm + example to go through + exaplnation of O(n)
- Morris Traversal of a tree O(1) memory! no stack or recursion
- Popular questions like Median of two sorted lists, REgular expression matching 
see in leetcode popular questions for the company you are interviewing
- Palindrome question patterns: around center check, Manacher, DP (dp(i,j) usually), rolling hash
-  Stream processing (one way to have conventional interface)
[enumerate] ---- [map] ------ [filter] ------- [accumulate]
range(n)            
stream creation------ map(fib,stream)------ filter(isodd,stream)-------sum(stream), tuple(stream)
- Trie Implementation

# Knowledge
- OOP > Function programming,  Message passing and dispatch is much neater?
oriented programming whose idea of message passing scales better?
- Functional programming > OOP as it is mathematical. No assingment in Functional
    and this does not break mathematics. In OOP we use environmenta model of
    computation to understand the process of program execution. Can be messy.
- DP two key ingredients: Optimal substructure + Overlapping subproblems.
 1. Determine subproblem space + choice -> See if there is Optimal substructure
    ie if an optimal solution to the problem contains within it optimal solutions t subproblems.
    - To characterize the space of subproblems, a good rule of thumb says to try to
    keep the space as simple as possible and then expand it as necessary.
2. Recursive equation
3. Reconstruct solution by keeping extra decision table in point 2
- Top- down(Memo) vs Bottom up:
    if all subproblems must be solved at least once, a bottom-up
    dynamic-programming algorithm usually outperforms the corresponding top-down
    memoized algorithm by a constant factor, because the bottom-up algorithm has no
    overhead for recursion and less overhead for maintaining the table. Moreover, for
    some problems we can exploit the regular pattern of table accesses in the dynamic-
    programming algorithm to reduce time or space requirements even further. Alter-
    natively, if some subproblems in the subproblem space need not be solved at all,
    the memoized solution has the advantage of solving only those subproblems that
    are deﬁnitely required.
- Greedy. How can we tell whether a greedy algorithm will solve a particular 
    optimization problem? No way works all the time, but the greedy-choice property 
    and optimal substructure are the two key ingredients.
4. Dnamyc bindings in python environmental model
    4.1 def modify(ls,m):
                ls[0]= 1
                m += 1
                ls= [222,3]
            m = 0 # m not changed
            ls = [3,2,1] # changes ls[0] to 1 but does not assign ls, argument  passed by value
            where the value is a copy of the reference. Similar thing in Java!
            objects are passed by copy of reference, primitive types ae copy of themselves
            modify(ls,m)
5. Binary Search problems often can be solved with Two pointers! They have the same underlying idea of restring the search space in a consistent way
6. Loop invariant proofs of correctness
7. Before using Tries - consider using rolling hash of the string


# Probability, Brain teasers

- Start with extreme numbers (either very small or very large).
- Symmetry
- Bayesian theorem
- ask as many questions as you need, especially during technical interviews
- break down approach into small manageable steps
- 
