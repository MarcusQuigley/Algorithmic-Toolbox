import sys

def money_change(money):
    coins = [10,5,1]
    change = 0
    for coin in coins:
        if money // coin > 0:
            val = money // coin
            change += val
            money -= (val * coin)
    return change

if __name__ == '__main__':
    money = int(sys.stdin.readline())
    print(money_change(money))
