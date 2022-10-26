This script works with matrices of different dimensions using the capabilities of the NumPy library.

### The first part is responsible for creating 3 matrices: 
> - 3x5 matrix filled with ones
> - 3x4 matrix filled with numbers from 0 to 60 with step of 5
> - 10x10 matrix filled with random numbers from 0 to 1.

### Next, the following functions were implemented:

✨ **matrix_multiplication** takes two matrices, multiplies them according to the appropriate rules and outputs the resulting matrix. The method numpy.dot was used, which allows to perform matrix multiplication.

✨ **multiplication_check** takes a list with matrices, and outputs `True` if they can be multiplied by each other in the order in which they are in the list, and `False` if they cannot be multiplied. The used lambda function and pairwise consistency check *(the number of columns in the first multiplier equals the number of rows in the second)*.

✨ **multiply_matrices** which takes a list with matrices and gives the result of multiplication if they can be obtained, or returns `None` if they cannot be multiplied.  The enumeration of matrices from the list is implemented through a loop, and the multiplication with the function `numpy.dot`.

✨ **compute_2d_distance** takes 2 one-dimensional arrays with a pair of values (as coordinates of a point in the plane) and calculates the distance between them. Implemented with the function `numpy.linalg.norm` to calculate the Euclidean distance.

✨ **compute_multidimensional_distance** takes 2 one-dimensional arrays with any number of values (but equal) and calculates the distance between them. The implementation is similar to the previous one.

✨ **compute_pair_distances** gets 2d matrices, where each row is an observation and each column is a fit. The function calculates a matrix of pairwise distances and gives it to the user. The implementation is almost similar to the previous two functions. 

### What should be input:
>- matrix_multiplication: two arrays
>- multiplication_check: list with arrays
>- multiply_matrices:  list with arrays
>- compute_2d_distance: 2 one-dimensional arrays with a pair of values. 
>- compute_multidimensional_distance: 2 one-dimensional arrays. **Make sure they are the same length!**
>- compute_pair_distances: 2d array. 
