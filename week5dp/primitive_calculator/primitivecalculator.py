import sys

def calculate_greedy(n):
    operations = []
    amount = int(n)
    total = 1
    operations.append(total)
    while total < amount:

        if total * 3 < amount:
            total = total * 3 
        elif total * 2 < amount:
             total = total * 2 
        else:
            total = total + 1
        operations.append(total)
    return operations

def calculate_dynamic(number):
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


if __name__ == '__main__':
    amount = int(sys.stdin.read())
    operations = list(calculate_greedy(amount))
    print(len(operations))
    for op in operations:
        print(op, end=' ')
