import sys

def lcs_of_two(str1, str2):
    if str1 == str2:
        return len(str1)

    rows = len(str1) + 1 
    cols = len(str2) + 1
    
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(1, rows):
        for j in range(1,cols):
            if str1[i-1] == str2[j-1]:
                matrix[i][j] = matrix[i-1][j-1] + 1
            else:
                matrix[i][j] = max(matrix[i][j-1], matrix[i-1][j])
    return matrix[i][j]


if __name__ == '__main__':
    # a_length = sys.stdin.readline()
    # a = sys.stdin.readline().split(' ')
    # b_length = sys.stdin.readline()
    # b = sys.stdin.readline().split(' ')

    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    result = lcs_of_two(a, b)
    print(result)
