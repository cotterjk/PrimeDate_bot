'''
Local Settings for a heroku_ebooks account. #fill in the name of the account you're tweeting from here.
'''

#configuration
MY_CONSUMER_KEY = 'Yzz1VaihjYqGQ4yADAyR4Tv43'
MY_CONSUMER_SECRET = 'BBxV8JBjI8sL9EAdPShZ0teBjxFw4EzxZ5Npyc7QwyOORD6xBc'
MY_ACCESS_TOKEN_KEY = '881263240541614082-yiW3hGqlyjZ12OYvSwJlo0hZl9iKCCY'
MY_ACCESS_TOKEN_SECRET = 'Ky5Pqi5i7SjAlqg9wwkcGjwEzIxzbPCLytPvzUjvW2WyV'

SOURCE_ACCOUNTS = [""] #A list of comma-separated, quote-enclosed Twitter handles of account that you'll generate tweets based on. It should look like ["account1", "account2"]. If you want just one account, no comma needed.
ODDS = 1 #How often do you want this to run? 1/8 times?
ORDER = 2 #how closely do you want this to hew to sensical? 1 is low and 3 is high.
DEBUG = False #Set this to False to start Tweeting live
STATIC_TEST = False #Set this to True if you want to test Markov generation from a static file instead of the API.
TEST_SOURCE = ".txt" #The name of a text file of a string-ified list for testing. To avoid unnecessarily hitting Twitter API. You can use the included testcorpus.txt, if needed.
TWEET_ACCOUNT = "primedate_bot" #The name of the account you're tweeting to.
