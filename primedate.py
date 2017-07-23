import random
import re
import sys
import twitter
import time
#Get tokens and keys to connect to the right account
from local_settings import *

#Connect to twitter API
def connect():
    api = twitter.Api(consumer_key=MY_CONSUMER_KEY,
                          consumer_secret=MY_CONSUMER_SECRET,
                          access_token_key=MY_ACCESS_TOKEN_KEY,
                          access_token_secret=MY_ACCESS_TOKEN_SECRET)
    return api

#Prime factor finder.
#Returns a list of remainder's prime factors in asending order.
def getAllFactorsFor(remainder):
    factors = []
    #Divides number by increasing natural numbers > 2,
    #which sifts out prime factors.
    for i in range(2, remainder, 1):
        while ((remainder % i) == 0):
            factors.append(i)
            remainder /= i
    return factors

#Generates tweet text from list of factors
#Includes special notices for prime and semiprime numbers
def getStringFromFactors(factors):
    factorstr = ''
    #getallFactorsFor() returns an empty list if the number is prime
    if len(factors) == 0:
        factorstr = 'prime. Cool!'
    else:
        for i in range(len(factors)):
            factorstr += str(factors[i])
            if i != (len(factors)-1):
                #Seperate factors with multiplication sign
                #len(factors)-1 prevents trailing 'x'
                factorstr += ' x '
        #End tweet with a period
        factorstr += '.'
        #Numbers with only 2 prime factors are called semiprime
        #which is still note-worthy, yeah?
        if len(factors) == 2:
            factorstr += ' That\'s semiprime!'
    return factorstr

if __name__=="__main__":
    #Connect
    api=connect()

    date = time.strftime("%m/%d/%y")
    #Get as a single int. August 12 1996 -> 81296
    dateint = int(time.strftime("%m%d%y"))

    #Generate tweet text using helper functions
    tweet = 'Today is ' + date + '. ' + str(dateint) + ' is ' + getStringFromFactors(getAllFactorsFor(dateint))
    print (tweet)
    #Tweet tweet
    api.PostUpdate(tweet)
