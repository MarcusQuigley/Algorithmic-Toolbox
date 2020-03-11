import sys

def get_change(money):
    coins = [1,3,4]
    minimumCoins = []
    #counter = 1
    minimumCoins.append(0)
    for m in range(1, money+1):
        minimumCoins.append(sys.maxsize)
        for coin in coins:
            if coin > m:
                break
            numCoins = minimumCoins[m - coin] + 1
            if numCoins < minimumCoins[m]:
                minimumCoins[m] = numCoins
    return minimumCoins[money]

if __name__ == '__main__':
    money = int(sys.stdin.read())
    print(get_change(money))