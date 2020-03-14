import sys

def min_operations(number):
    operations = [0] * (number+1)
    
    for i in range(2, number+1):
        oneplus = operations[i-1]
        twotimes = sys.maxsize
        threetimes = sys.maxsize
        if i % 3 == 0:
            threetimes = operations[int(i/3)]
        if i % 2 == 0:
            twotimes = operations[int(i/2)]
        op = min(oneplus, twotimes, threetimes)
        operations[i] = op + 1
    return operations

def operations_list(ops, number):
    if number == 1:
        return [1] 
    result = []
    n = number
    while n > 0:
        result.append(n)
        if n % 3 > 0 and n % 2 > 0:
            n = n-1
        elif n % 3 == 0 and n % 2 == 0:
            n = n // 3
        elif n % 2 == 0:
            if ops[n-1] > ops[int(n//2)]:
                n = n // 2
            else:
                n = n - 1
        elif n % 3 == 0:
            if ops[n-1] > ops[int(n//3)]:
                n = int(n // 3)
            else:
                n = n-1
    return list(reversed(result))


if __name__ == '__main__':
    amount = int(sys.stdin.read())
    operations = min_operations(amount)
    result = operations_list(operations, amount)
    print(len(result)-1)
    for r in result:
        print(r, end=' ')
