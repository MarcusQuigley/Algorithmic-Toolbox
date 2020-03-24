import sys

def max_add_revenue(a, b):
    a.sort(reverse=True)
    b.sort(reverse=True)
    result = 0
    for i in range(len(a)):
        result += a[i] * b[i]
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_add_revenue(a, b))