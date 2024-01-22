# **Wagner-Fisher Algorithm**

## Explanation of the algorithm

The Wagner–Fischer algorithm is a dynamic programming algorithm that computes the edit distance between two strings of characters.

The algorithm reserves a matrix to hold the edit distances between all prefixes of a string and all prefixes of another string, and then computes the values in the matrix by flood filling the matrix, and thus finds the distance between the two full strings as the last value computed (bottom-right corner of the matrix).

In the code implementation we calculate the edit distance between the each word in the dictionary and the inputed word, and output the 10 words with the smallest edit distance from the inputed word, thus finding the closest correct word to the possibly misspelled inputed word.