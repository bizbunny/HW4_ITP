
>>> from hw4 import *

##### Problem 1 #####

Write a function indexes(word, char) that takes as input a word and a one-character letter (both are strings) and RETURNS a list of indexes at which the letter occurs in the word.

NOTE: enumerate built-in function might be useful for you here

>>> indexes('mississippi', 's')
[2, 3, 5, 6]
>>> indexes('mississippi', 'i')
[1, 4, 7, 10]
>>> indexes('mississippi', 'a')
[]
>>> indexes('banana', 'b')
[0]
>>> indexes('banana', 'a')
[1, 3, 5]
>>> indexes('banana', 'n')
[2, 4]



##### Problem 2 #####

Write a function hasLetterCount(lst, numChars) that takes as input a list of words lst and a number numChars and RETURNS a list of all words that are of that length.

>>> hasLetterCount(["My", "bologna", "has", "a", "first", "name", "it", "is", "oscar"], 5)
['first', 'oscar']
>>> hasLetterCount(["My", "bologna", "has", "a", "first", "name", "it", "is", "oscar"], 2)
['My', 'it', 'is']
>>> hasLetterCount(["My", "bologna", "has", "a", "first", "name", "it", "is", "oscar"], 10)
[]


##### Problem 3 #####

Write a function intersect(lst1, lst2) that takes as input two lists of numbers, lst1 and lst2 and RETURNS a list of unique numbers appearing in both lists.

>>> intersect([3, 4, 5, 8, 3, 4, 5], [5, 6, 7])
[5]
>>> intersect(list(range(0,10)), [1,2,3])
[1, 2, 3]
>>> intersect(list(range(0,10)), [1,2,3])
[1, 2, 3]


##### Problem 4 #####

Write a function describe(matrix) that takes as input a 2D array and RETURNS 'Square' if the matrix is square, 'Rectangular' if the matrix is rectangular, and 'Invalid' if neither.
Square matrices have the same number of rows and columns. This is a 5x5 square matrix:
1 2 3 4 5
2 3 4 5 6
3 4 5 6 7
4 5 6 7 8
5 6 7 8 9
Rectangular matrices can have different numbers of rows and columns, but each row is the same length. This is a 2x5 rectangular matrix:
1 2 3 4 5
0 2 4 6 8
Invalid matrices have inconsistent length in their rows. This is an invalid matrix:
1 2 3 4 5
5 4 3 2 1 0
8 6 2 9 1 
0 8 4 2 4 7
NOTE: All square matrices are also rectangular -- only RETURN 'Square' if it is square.

>>> describe([[0]])
'Square'
>>> describe([[0, 1, 2], [2, 1, 0], [3, 3, 3]])
'Square'
>>> describe([[0, 1, 2], [2, 1], [3, 3, 3]])
'Invalid'
>>> describe([[0, 1], [1, 0], [3, 3]])
'Rectangular'
>>> describe([[0, 1], [1, 0], [3, 3]])
'Rectangular'
>>> describe([[0, 1, 2, 3, 4, 5]])
'Rectangular'
>>> describe([[0, 1, 2, 3, 4, 5], [5, 4, 3, 2, 1, 0]])
'Rectangular'


##### Problem 5 #####

Write a function identityMatrix(rank) that takes as input a number rank and RETURNS a 2D array that is a square identity matrix of that rank.
The rank of a NxN square matrix is N.
An identity matrix has 1s along the diagonal and 0s everywhere else.
This is a 5x5, or rank 5, identity matrix:
1 0 0 0 0
0 1 0 0 0
0 0 1 0 0
0 0 0 1 0
0 0 0 0 1

>>> identityMatrix(1)
[[1]]
>>> identityMatrix(2)
[[1, 0], [0, 1]]
>>> identityMatrix(4)
[[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]


NOTE: the last 2 tests here will use both functions from problems 4 and 5 to ensure that your identityMatrix function is a square matrix
>>> describe(identityMatrix(10))=='Square'
True
>>> describe(identityMatrix(4))
'Square'

