def Union(A, B):
    C = []
    m = len(A)
    n = len(B)

    i, j = 0, 0

    while i < m and j < n:
        if A[i] < B[j]:
            i += 1
        elif A[i] > B[j]:
            j += 1
        else:  # A[i] == B[j]
            C.append(A[i])
            i += 1
            j += 1

    return C

print(Union([1, 2, 3], [3, 4, 5]))  # Output: [3]
