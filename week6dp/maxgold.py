def max_gold(capacity, gold):
    result = 0
    for i in reversed(range(len(gold))): # range(len(gold)-1,-1,-1):
        g = gold[i]
        if (result + g <= capacity):
            result += g
    return result