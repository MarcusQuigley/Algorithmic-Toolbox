def knapsack_with_repetitions(capacity, weights, values):
    if weights == None or values == None: return -1
    if len(weights) != len(values): return -1
    n = len(weights)
    results = [0] * (capacity + 1)
    for w in range(1, capacity + 1):
        for i in range(1, n + 1):
            weight = weights[i-1]
            if weight <= w:
                results[w] = max(results[w], results[w - weight] + values[i-1])
                # val = results[w - weight] + values[i-1]
                # if val > results[w]:
                #     results[w] = val
    return results[capacity]

T = dict()
def knapsack_recursive_with_repetitions_stpete(capacity, weights, values):
    if capacity not in T:
        T[capacity] = 0

    for i in range(len(weights)):
        weight = weights[i]
        if weight <= capacity:            
            maxVal = max(T[capacity], 
                knapsack_recursive_with_repetitions_stpete(capacity - weight, weights, values) + values[i])
            T[capacity] = maxVal
            print("T[{0}] is {1}",capacity,maxVal)
    return T[capacity]

# def knapsack_with_repetitions_stpete(weights, values, capacity):


