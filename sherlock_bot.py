import os 
from markovbot import MarkovBot
#import twitter

#initalise a MarkovBot instance
tweetbot = MarkovBot()

#get the current directory's path
dirname = os.path.dirname(os.path.abspath(__file__))

#construct the path to the book
book = os.path.join(dirname, 'sherlock.txt')

#make your bot read the book!
tweetbot.read(book)


my_first_text = tweetbot.generate_text(25, seedword=['Irene', 'watson','Mycroft'])
print("tweetbot says:")
print(my_first_text)

# ALL YOUR SECRET STUFF!
# Consumer Key (API Key)
cons_key = 'AqYyIzu5jXXYhubZI83WtfmnV'
# Consumer Secret (API Secret)
cons_secret = 'QyqofLZtVJSjgS4L7EltzaxPJrcz23vgyN8zMNZ4dm88HdM1c6'
# Access Token
access_token = '751058612051648514-FGw6PEjNmkIdbWqrC3MfhVYEe8KJyCF'
# Access Token Secret
access_token_secret = 'PFKpoM7ra8rziOc0gs9ci4pT2TGRvn0fRXw5gw8PzYFnp'

# Log in to Twitter
tweetbot.twitter_login(cons_key, cons_secret, access_token, access_token_secret)

# Start periodically tweeting
tweetbot.twitter_tweeting_start(days=0, hours=0, minutes=1, keywords=None, prefix=None, suffix='#PyGaze')

# Use the following to stop periodically tweeting
# (Don't do this directly after starting it, or your bot will do nothing!)
#tweetbot.twitter_tweeting_stop()

# Set some parameters for your bot
targetstring = 'MarryMeSherlock'
keywords = ['marriage', 'ring', 'flowers', 'children', 'religion']
prefix = None
suffix = '#SherlockSaysIDo'
maxconvdepth = None


# Start auto-responding to tweets
# tweetbot.twitter_autoreply_start(targetstring, keywords=keywords, prefix=prefix, suffix=suffix, maxconvdepth=maxconvdepth)
 
# Use the following to stop auto-responding
# (Don't do this directly after starting it, or your bot will do nothing!)
#tweetbot.twitter_autoreply_stop()