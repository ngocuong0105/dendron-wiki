
# Mаtrices

Matrix Multiplication, Inverse , Orthogonal Matrix, Gaussian Elimination

- tidy way to represent linear equations
- coefficients of the variables are the entries of the matrix
- matrix properties defines if and how many solutions the linear system has
- Matrix Multiplication is not commutative! It is $O(m*n*p)$ cost to multiply an $m x n$ matrix with an $n x p$ matrix.
- Set of square matrices under addition/multiplication is a Ring and a Group but is not Abelian (i.e. not commutative)
- Only square matrices can be inverted, rectangular matrices cannot be inverted
- For rectangular matrices we have the pseudo-inverse (the product is almost the same as the identity matrix)
- The inverse of a matrix is unique, if it exists
- A matrix is orthogonal if the inverse is equal to the transpose. $A*A^{T} = I = A^{T}*A$
- In orthogonal matrix, multiplying each tw rows (or columns) has dot produc zero (perpendicular). Multiplying the same vector gives the unit vector.
- Multiplying by orthogonal $A$ rotates and/or reflects vectors, but doesn’t change their lengths or angles between them.
- Gaussian elimination is the method you use to solve linear equations systematically. 1. Swap equation, to find the leftmost non-zero entry.
2. Scale the equation, so that the leftmost non-zero entry is 1. (divide by the coefficient)
3. Subtract appropriate multiples of the first equation from all other equations to eliminate the leftmost non-zero entry in those equations.
4. Now only one row has a non-zero entry in the first column. We will able to tell teh value of the first variable once we know the values of all other variables.
5. You will get a triangular matrix, where the first row has a non-zero entry in the first column, the second row has a non-zero entry in the second column, and so on.
-  A system of linear equations $Ax = b$. The augmented matrix is $A|b$.
- EROs (elementary row operations) on the augmented matrix $A|b$ are:
  1. Swap two rows
  2. Scale a row by a non-zero constant
  3. Add a multiple of one row to another row
- Each ERO is invertible and does not change the set of solutions
- Echelon form of a matrix is triangular, where the first non-zero entry in each row is 1, and all entries below it are 0. In Gaussian elimination, you bring a matrix using EROs to echelon form.
- **Theorem** An invertible $n x n$ matrix can be reduced to $I_{n}$ using EROs.
- **Theorem** I $A$ is invertible, then $Ax = b$ has a unique solution for every $b$. The solution is $A^{-1}b$


# Calculating the inverse

-- To calculate he inverse of a **square** matrix A, augment the identity and row reduce the augmented matrix to echelon form. If the echelon form is the identity, then the inverse is the other half of the augmented matrix.
- Idea is each EROs, can be represented by multiplying by an **elementary** matrix $E_{i}$.
- $E_k...E_2E_1A = I$
- so the product of the elementary matrices is the inverse of $A$.
- applying  EROs to identity records their combined effect
- $O(n^3)$