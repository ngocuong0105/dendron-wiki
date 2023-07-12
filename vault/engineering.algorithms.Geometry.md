---
id: bvywezxe342ge7lrslfg9ue
title: Geometry
desc: ''
updated: 1689087576910
created: 1664382853125
---


# Elementary operations
## Basic Geometry
- cross product checks for collinearity (line on one line)

<details>
<summary> <b>CODE</b> </summary>

```Python
def collinear(u,v):
    sm = 0
    for i in range(len(u)):
        sm += u[i]*v[i]
    return sm == 0
```
</details>

# Finding the equation of a line for a segment
- [leetcode](https://leetcode.com/problems/check-if-it-is-a-straight-line/)
vertical lines have infinite slope, to avoid edge cases use above representaion of a line $Ax+By+C = 0$

# Minimum enclosing circle

$O(N)$
[Erect the fence](https://leetcode.com/problems/erect-the-fence-ii/)

```python
def circle_three(arr):
    """arr is a list of 3 points"""
    (x0, y0), (x1, y1), (x2, y2) = arr
    A = x0*(y1-y2) - y0*(x1-x2) + x1*y2 - x2*y1
    B = (x0*x0 + y0*y0)*(y2-y1) + (x1*x1 + y1*y1)*(y0-y2) + (x2*x2+y2*y2)*(y1-y0)
    C = (x0*x0 + y0*y0)*(x1-x2) + (x1*x1 + y1*y1)*(x2-x0) + (x2*x2+y2*y2)*(x0-x1)
    D = (x0*x0 + y0*y0)*(x2*y1-x1*y2) + (x1*x1+y1*y1)*(x0*y2-x2*y0) + (x2*x2+y2*y2)*(x1*y0-x0*y1)
    return (-B/(2*A), -C/(2*A), sqrt((B*B+C*C-4*A*D)/(4*A*A)))

def inside(p,x,y,r):
    """return: is point p inside circle (x,y,r)"""
    return (p[0]-x)**2+(p[1]-y)**2 < r**2

def dist(a,b):
    return ((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5

def mec(i,R):
    """
    Minimum enclosing circle using Welzl’s algorithm
    R = points which need to be on the boundary
    return: MEC of all points[:i+1] where points in R are on the boundary
    """
    if len(R) == 3:
        return circle_three(R)
    if i == len(points):
        if len(R) == 0: return (0,0,0)
        elif len(R) == 1: return (R[0][0],R[0][1],0)
        elif len(R) == 2: 
            return (R[0][0]+R[1][0])/2,(R[0][1]+R[1][1])/2,dist(R[0],R[1])/2

    x,y,r = mec(i+1,R)
    if inside(points[i],x,y,r): return (x,y,r)
    return mec(i+1,R+[points[i]])

points = list(set(tuple(p) for p in points))
print("Result:", mec(0,[]))
```
        Intersection Point of Lines
        Check if two segments intersect
        Intersection of Segments
        Circle-Line Intersection
        Circle-Circle Intersection
        Common tangents to two circles
        Length of the union of segments
# Polygons
        Oriented area of a triangle
        Area of simple polygon
        Check if points belong to the convex polygon in O(log N)
## Check if convex polygon
[problem](https://leetcode.com/problems/convex-polygon/)
- cross product of three points (a,b,c) sign shows the direction of the turn

        Minkowski sum of convex polygons
        Pick's Theorem - area of lattice polygons
        Lattice points of non-lattice polygon
    Convex hull
        Convex hull construction
        Convex hull trick and Li Chao tree
# Sweep-line
## Search for a pair of intersecting segments
- [perfect rectangle](https://leetcode.com/problems/perfect-rectangle/)
Given  a list of rectangles we want to find if there is any overlap of two rectangles.

- Line sweep x-axis and add y1,y2 intervals into a SortedList data structure



## Point location in O(log N)
    Miscellaneous
        Finding the nearest pair of points
        Delaunay triangulation and Voronoi diagram
        Vertical decomposition
        Half-plane intersection - S&I Algorithm in O(N log N)
