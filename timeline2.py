import tweepy


#encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding("utf8")


auth = tweepy.OAuthHandler("cLsFfKie7G90Pw6l1yUfToLLt","Jp3zJ7PWq5s2Jc9FXlHVlEmlekUUsbD1OfAXLZxl8etOj7CepC")
auth.set_access_token ("977602411081666560-2c2QSMWoDXkJ78BgJGWz14zs6jDzlQP", "tyMQgGQ3zRChLO48Fl2VgOW5rI4QBXrTeeHWyaCDEyCil")

twitter_api = tweepy.API(auth)

cfg_tweets = twitter_api.search(
	q = "thehoodmemes" #Twitter handle you want to search by
)

for tweet in cfg_tweets:
	print tweet.user.name + ": " + tweet.text +"\n"




#class StdOutListener(StreamListener):
#    ''' Handles data received from the stream. '''
 
 #   def on_status(self, status):
        # Prints the text of the tweet
  #      print('Tweet text: ' + status.text)
 
        # There are many options in the status object,
        # hashtags can be very easily accessed.
   #     for hashtag in status.entries['hashtags']:
    #        print(hashtag['text'])
 
     #   return true
 
    #def on_error(self, status_code):
     #   print('Got an error with status code: ' + str(status_code))
      #  return True # To continue listening
 
    #def on_timeout(self):
     #   print('Timeout...')
      #  return True # To continue listening
 
#if __name__ == '__main__':
#	listener = StdOutListener()
#auth = tweepy.OAuthHandler("cLsFfKie7G90Pw6l1yUfToLLt","Jp3zJ7PWq5s2Jc9FXlHVlEmlekUUsbD1OfAXLZxl8etOj7CepC")
#auth.set_access_token ("977602411081666560-2c2QSMWoDXkJ78BgJGWz14zs6jDzlQP", "tyMQgGQ3zRChLO48Fl2VgOW5rI4QBXrTeeHWyaCDEyCil")
 
#stream = Stream(auth, listener)
#stream.filter(follow=[38744894], track=['#pythoncentral'])