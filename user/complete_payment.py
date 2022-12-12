import random


def CompletePayment():
    a = "abcdefghijklmnopqrstuvwxyz1234567890@#$%"
    transaction_id = ""
    for i in range(24):
        transaction_id += a[random.randint(0,len(a)-1)]
    return transaction_id