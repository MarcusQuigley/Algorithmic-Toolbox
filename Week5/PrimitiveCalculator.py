import sys

def calculate(n):
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

if __name__ == '__main__':
    amount = int(sys.stdin.read())
    operations = list(calculate(amount))
    print(len(operations))
    for op in operations:
        print(op, end=' ')
