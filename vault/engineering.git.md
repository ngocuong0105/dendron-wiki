---
id: 78ld05rlq10336r34dz8sxc
title: Git
desc: ''
updated: 1668338731838
created: 1668288491690
---

My notes on [Learn Git Branching](https://learngitbranching.js.org/).


# Commits and branches

A **commit** in a git repository records a snapshot of all the (tracked) files in your directory. It's like a giant copy and paste, but even better!

**commit = snapshot of the project = lightweight safe of project state** 

Commits can be visually represented as nodes.

- create a commit
```
git commit -m 'commit message'
```

**Branches = pointer to a specific commit**

*'branch early, and branch often'*

Branches are super lightweight and have no storage/memory overhead

Branches are pointers. To get yourself to a branch you need to *checkout* there

- create a new branch
```
git branch new_branch
```

- go to the branch
```
git checkout new_branch
```

- shortcut
```
git checkout -b new_branch
```

# Merge

**Merge** = combining work from two different branches together.

Merging in Git creates a special commit that has two unique parents.

![before_merge.png](assets/images/before_merge.png)


![after_merge.png](assets/images/after_merge.png)

Above we merge bugFix into main and main contains all the work.

- merge
```
git checkout -b bugFix
git commit -m 'Blah'
git checkout main
git merge bugFix
```

# Rebase

The second way of combining work between branches is **rebasing**. Rebasing essentially takes a set of commits, "copies" them, and plops them down somewhere else.

Rebasing makes a nice linear sqauce of commits. Commit log of the repo will be cleaner.

![before_rebase.png](assets/images/before_rebase.png)


![after_rebase.png](assets/images/after_rebase.png)

Here we have two branches yet again; note that the bugFix branch is currently selected (note the asterisk)

We would like to move our work from bugFix directly onto the work from main. That way it would look like these two features were developed sequentially, when in reality they were developed in parallel.


C3 still exists, and the rebase creates a copy C3'
- **rebase**
```
git checkout -b bugFix
git commit -m 'Blah'
git checkout main
git commit
git checkout bugFix
git rebase main
```

- interactive rebase (can squash commits)
```
git rebase -i main
```

# HEAD

**HEAD** is the symbolic name for the currently checked out commit -- it's essentially what commit you're working on top of.

HEAD is hiding underneath our work on the repo/branches.

HEAD normally point to the branch you are currently working on

**Detaching** HEAD just means attaching it to a commit instead of a branch.

Example: on main branch with one commit:

HEAD -> main -> C1

`git checkout C1 ` makes HEAD ->  C1


To checkout to a commit you need to use its hash (C1)

To see commits hashes:
```
git log
```

# Moving around git

OPERATORS `^ ~`

Specifying commits by their hash isn't the most convenient thing ever, which is why Git has relative refs

saying **main^** is equivalent to "the first parent of main
- go to parent commit
```
git checkout main^
```

You can also reference HEAD as a relative ref
```
git checkout HEAD^
```
- go to previous commit, if current commit is C4, the one below will go to C0
```
git checkout HEAD~4
```

# Branch forcing

One of the most common ways I use relative refs is to move branches around. You can directly r**eassign a branch to a commit** with the -f option

```
git branch -f main HEAD~3
```

![before_force.png](assets/images/before_force.png)

![after_force.png](assets/images/after_force.png)


# Reversing changes in Git

`git reset` reverses changes by moving a branch reference backwards in time to an older commit. In this sense you can think of it as "rewriting history;" `git reset`will move a branch backwards as if the commit had never been made in the first place.


![before_reset.png](assets/images/before_reset.png)

![after_reset.png](assets/images/after_reset.png)

```
git reset HEAD~1
```

reset does not work for remote branches. Need to use

```
git revert HEAD
```


# Moving Work Around

You know how to move around the source tree using reference operators `^ ~`.

The next concept we're going to cover is "moving work around" -- in other words, it's a way for developers to say "I want this work here and that work there"

- **cherry pick**
```
git cherry-pick <Commit1><Commit2>
```

says that you would like to copy a series of commits below your current location (HEAD).


- **interactive rebase**