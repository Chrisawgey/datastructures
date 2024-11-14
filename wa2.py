# a. 2^n - 4n^2 + 5n
# Dominant term: 2^n
# Big-O classification: O(2^n)

# b. 3n^2 + 6
# Dominant term: 3n^2
# Big-O classification: O(n^2)

# c. n^2 + n^2 - n
# Dominant term: 2n^2
# Big-O classification: O(n^2)

#----------------------------------------------------

# Algorithm A: n^2 instructions
# Algorithm B: 1/2n^2 + 1/2n instructions

# Algorithm A does more work for large n due to its dominant term n^2.
# Algorithm B performs significantly better for large n because 1/2n^2 grows slower than n^2.
# For small n, both algorithms perform approximately the same amount of work.

#--------------------------------------------------------

# n^4 performs better than 2^n for large n due to the slower growth of polynomial functions.
# The crossover point occurs around n ≈ 15.
# For n ≥ 20, 2^n grows much faster than n^4, making n^4 perform better beyond n = 15.
