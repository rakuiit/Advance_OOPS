class BalanceException(Exception):
    pass


def checkbalance():
    money=10000
    withdram=9000
    balance=money-withdram
    if balance<=2000:
        raise BalanceException('Insufficient Balance')
    print(balance)


try:
    checkbalance()

except BalanceException as be:
    print(be)