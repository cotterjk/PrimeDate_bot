import random
import re
import sys
import twitter
import time
from local_settings import *

def connect():
    api = twitter.Api(consumer_key=MY_CONSUMER_KEY,
                          consumer_secret=MY_CONSUMER_SECRET,
                          access_token_key=MY_ACCESS_TOKEN_KEY,
                          access_token_secret=MY_ACCESS_TOKEN_SECRET)
    return api

def getAllFactorsFor(remainder):
    factors = []
    for i in range(2, remainder, 1):
        while ((remainder % i) == 0):
            factors.append(i)
            remainder /= i
    return factors

def getStringFromFactors(factors):
    factorstr = ''
    if len(factors) == 0:
        factorstr = 'prime. Cool!'
    else:
        for i in range(len(factors)):
            factorstr += str(factors[i])
            if i != (len(factors)-1):
                factorstr += ' x '
        factorstr += '.'
    return factorstr

if __name__=="__main__":
    api=connect()

    date = time.strftime("%m/%d/%y")
    dateint = int(time.strftime("%m%d%y"))
    dateint = 70117

    tweet = 'Today is ' + date + '. ' + str(dateint) + ' is ' + getStringFromFactors(getAllFactorsFor(dateint))
    print (tweet)
    api.PostUpdate(tweet)
