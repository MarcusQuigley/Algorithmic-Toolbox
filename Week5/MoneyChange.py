import sys

def get_change(money):
    return "you have " + str(money)

if __name__ == '__main__':
    money = int(sys.stdin.read())
    print(get_change(money))