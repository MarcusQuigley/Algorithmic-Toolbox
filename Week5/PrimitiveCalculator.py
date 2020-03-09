import sys

def calculate(n):
    operations = []
    amount = int(n)
    counter = 0
    operations.append(amount)
    while amount>1:
        counter = counter + 1
        if amount % 3 == 0:
            amount = int(amount / 3)
        elif amount % 2 == 0:
            amount = int(amount / 2)
        else:
            amount = amount - 1
        operations.append(amount)
    return reversed(operations)

if __name__ == '__main__':
    amount = int(sys.stdin.read())
    operations = list(calculate(amount))
    print(len(operations))
    for op in operations:
        print(op, end=' ')
