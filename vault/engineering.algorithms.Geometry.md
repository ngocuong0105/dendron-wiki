---
id: bvywezxe342ge7lrslfg9ue
title: Geometry
desc: ''
updated: 1665395054525
created: 1664382853125
---


# Elementary operations
## Basic Geometry
- cross product checks for collinearity (line on one line)
```python
def collinear(u,v):
    sm = 0
    for i in range(len(u)):
        sm += u[i]*v[i]
    return sm == 0
```
# Finding the equation of a line for a segment
- [leetcode](https://leetcode.com/problems/check-if-it-is-a-straight-line/)
vertical lines have infinite slope, to avoid edge cases use above representaion of a line $Ax+By+C = 0$

        Intersection Point of Lines
        Check if two segments intersect
        Intersection of Segments
        Circle-Line Intersection
        Circle-Circle Intersection
        Common tangents to two circles
        Length of the union of segments
    Polygons
        Oriented area of a triangle
        Area of simple polygon
        Check if points belong to the convex polygon in O(log N)
        Minkowski sum of convex polygons
        Pick's Theorem - area of lattice polygons
        Lattice points of non-lattice polygon
    Convex hull
        Convex hull construction
        Convex hull trick and Li Chao tree
    Sweep-line
        Search for a pair of intersecting segments
        Point location in O(log N)
    Miscellaneous
        Finding the nearest pair of points
        Delaunay triangulation and Voronoi diagram
        Vertical decomposition
        Half-plane intersection - S&I Algorithm in O(N log N)
