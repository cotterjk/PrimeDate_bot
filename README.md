# Prime Factorization Of The Date, Twitter Bot

A twitter bot that, each morning, tweets the prime factorization of the date converted to a whole number. (For example, December 25, 1996 becomes 122596.)

According to the [fundamental theorem of arithmetic](https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic),
not only can every integer greater than 1 be represented as a product of primes, but each number has exactly one representation in this way. (122596 = 2 x 2 × 30649. 2, 2, and 30649 are the only primes that belong to 122596.)

My first bot, this is meant to illustrate how each day is similarly special and singular.

(At least, within its century, based on how I'm taking dates.)

Watch it go [@primedate_bot](https://twitter.com/primedate_bot)

## Details

The code is pushed to a Heroku app, and tweets once a day at 7am EDT using a Heroku scheduler, calling `tweet`. It can also be manually triggered to tweet by navigating to the local repository and running `heroku run tweet`.

## Acknowledgments

* Twitter API connection and basic structure taken from [this Science Friday tutorial](https://medium.com/science-friday-footnotes/how-to-make-a-twitter-bot-in-under-an-hour-259597558acf).
