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
    operations = []
    for i in range(0, number+1):
        operations.append(0)
 
    for i in range(2,number + 1):
        plus1 = (operations[i-1])
        mult2 = sys.maxsize
        mult3 = sys.maxsize
        if i % 3 == 0:
            mult3 = operations[int(i/3)]
        if i % 2 == 0:
            mult2 = operations[int(i/2)]
        minOp = min(plus1, mult2, mult3)
        operations[i] = minOp + 1

    return operations



if __name__ == '__main__':
    amount = int(sys.stdin.read())
    operations = list(calculate_greedy(amount))
    print(len(operations))
    for op in operations:
        print(op, end=' ')
