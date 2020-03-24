import sys

#take most valuable item
def max_value_of_loot(capacity, weights, values):
    knapsack = 0
    result = 0
    #n = len(weights)
    while True:
        if knapsack == capacity:
           return result
        maxvalue=0
        maxindex=-1
        for j in range(len(weights)):
            val = weights[j] // values[j]
            if maxvalue < val:
                maxvalue = val
                maxindex = j
        value = values[maxindex]
        weight = weights[maxindex]
        if value <= (capacity - knapsack):
            knapsack += value
            result += weight
        else:
            fraction = (capacity - knapsack) / value
            result += float(str(round(fraction * weight,4)))
            knapsack += (capacity - knapsack)            

        weights.pop(maxindex)
        values.pop(maxindex)

if __name__ == '__main__':
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = max_value_of_loot(capacity, weights, values)
    print("{:.10f}".format(opt_value))



