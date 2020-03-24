import sys

def money_change(money):
    coins = [10,5,1]
    change = 0
    for coin in coins:
        while coin <= money:
            money -= coin
            change += 1
    return change

if __name__ == '__main__':
    money = int(sys.stdin.readline())
    print(money_change(money))
