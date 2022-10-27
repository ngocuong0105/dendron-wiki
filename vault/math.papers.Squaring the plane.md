---
id: lxaqy0rqb4x7h1zdupxiu9l
title: Squaring the plane
desc: ''
updated: 1666768643173
created: 1666766425439
---
[Squaring the plane](https://drive.google.com/file/d/1BX0tL1ksgh926C6rEN7QWUS8io4auXJg/view?usp=sharing) paper. Famous problem of creating a square of unique squares, also known as tiling. This paper solves the question of whether or not the infinite plane could be tiled using one copy of each square of integer side length: one
copy of the squares $(1×1), (2×2), (3×3)$, and so on.

Imperfect squares problem is if there could be repeated squares. You can use Fibonacci trick to get this easily.

The pape gives an algo which they prove that would fill in the infinite plane with squares.


1. Start with any perfect ell and square it up.
2. Create a new ell by attaching to the rectangle the smallest square not yet used.
3. Square (*rectanlge*) this ell up, making sure that new squares are added in all four directions.
4. Repeat steps 2 and 3 ad infinitum.


**Theorem.** It is possible to tile the plane with nonoverlapping squares using exactly one square of each integral side. Note the plane is a rectangle.

Related problem by [Numberphile](https://www.youtube.com/watch?v=NoRjwZomUK0)
