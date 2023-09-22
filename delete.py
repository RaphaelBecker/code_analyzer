def example_function(lst, matrix):
    total = 0                                       # O(1)

    # First loop, runs n times
    for num in lst:                                 # O(n)
        total += num                                # O(1)

    # Nested loops, run n * m times (if matrix is n x m)
    for row in matrix:                              # O(n)
        for elem in row:                            # O(m)
            total += elem                           # O(1)

    # Triple nested loops, run n * n * n times
    for i in range(len(lst)):                       # O(n)
        for j in range(len(lst)):                   # O(n)
            for k in range(len(lst)):               # O(n)
                total += lst[i] + lst[j] + lst[k]   # O(1)

    return total                                    # O(1)

# Overall time complexity is O(n + n*m + n^3) = O(n^3) assuming n >= m
