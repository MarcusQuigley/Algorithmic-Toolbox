import sys

def minimum_edit_distance(str1, str2):
    if str1 == str2:
        return 0

    rows = len(str1) + 1
    cols = len(str2) +1

    matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        matrix[i][0] = i

    for j in range(cols):
        matrix[0][j] = j

    for i in range(1, rows):
        for j in range(1, cols):
            if str1[i-1] == str2[j-1]:
                matrix[i][j] = matrix[i-1][j-1]
            else:
                minvalue = min(matrix[i][j-1], matrix[i-1][j], matrix[i-1][j-1])
                matrix[i][j] = minvalue + 1
    return matrix[i][j]

        

if __name__ == '__main__':
    str1 = sys.stdin.readline()
    str2 = sys.stdin.readline()

    result = minimum_edit_distance(str1, str2)
    print(result)

