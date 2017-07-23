# Prime Factorization Of The Date, Twitter Bot

A twitter bot that, each morning, tweets the prime factorization of the date converted to a whole number. According to the [Fundamental theorem of arithmetic](https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic), states that "that every integer greater than 1 either is prime itself or is the product of prime numbers, and that this product is unique." This quick bot is meant to illustrate how each day is similarly special.

Watch it go [@primedate_bot](https://twitter.com/primedate_bot)

## Details

The code is pushed to a Heroku app, and tweets once a day at 7am EDT using a Heroku scheduler, calling `tweet`. It can also be manually triggered to tweet by navigating to the local repository and running `heroku run tweet`.

## Acknowledgments

* Twitter API connection and basic structure taken from [this Science Friday tutorial](https://medium.com/science-friday-footnotes/how-to-make-a-twitter-bot-in-under-an-hour-259597558acf).
