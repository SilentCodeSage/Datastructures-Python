def find_saddle_point(matrix, r, c):
    for i in range(r):
        # Find the minimum element in the i-th row
        min_row_value = min(matrix[i])
        min_row_index = matrix[i].index(min_row_value)
        
        # Check if this minimum element is the largest in its column
        is_saddle_point = True
        for j in range(r):
            if matrix[j][min_row_index] > min_row_value:
                is_saddle_point = False
                break
        
        # If we find a saddle point, return 1
        if is_saddle_point:
            return 1
    
    # If no saddle point is found, return 0
    return 0

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    r = int(data[0])
    c = int(data[1])
    matrix = []
    
    index = 2
    for _ in range(r):
        row = list(map(int, data[index:index + c]))
        matrix.append(row)
        index += c
    
    result = find_saddle_point(matrix, r, c)
    print(result)

if __name__ == "__main__":
    main()
