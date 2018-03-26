from flask import Flask, render_template, request, redirect

app = Flask("MyApp")
  
@app.route("/")
def index():
	return render_template("index.html") 

@app.route('/signup', methods = ['POST'])
def signup():
    email = request.form['email']
    name = request.form['name']
    favourite_meme = request.form['favourite_meme']
    message = request.form['message']
    print("Their name is '" + name + "'. " + "Their email address is '" + email + "'. " + "Their favourite meme is '" + favourite_meme + "'. " + "Their message is '" + message + "'.")
    if favourite_meme == "Salt Bae": 
    	return redirect("/saltbae")
    if favourite_meme == "Evil Kermit": 
    	return redirect("/evilkermit")
    if favourite_meme == "Cash Me Outside": 
    	return redirect("/cashmeoutside")            
    if favourite_meme == "Damn Daniel": 
    	return redirect("/damndaniel")                    
    if favourite_meme == "Roll Safe":    
    	return redirect("/rollsafe")                                                                     
       
@app.route("/saltbae")
def saltbae():         
	return render_template("saltbae.html")                                       
     
@app.route("/evilkermit")
def evilkermit():
	return render_template("evilkermit.html")
   
@app.route("/cashmeoutside")              
def cashmeoutside():
	return render_template("cashmeoutside.html")
   
@app.route("/damndaniel")   
def damndaniel():
	return render_template("damndaniel.html")

@app.route("/rollsafe")
def rollsafe():
	return render_template("rollsafe.html")

@app.route("/about")
def about():
	return render_template("about.html") 

@app.route("/gallery")
def gallery():
	return render_template("gallery.html")            

@app.route("/generate")
def generate():
	return render_template("generate.html")
     
import tweepy
    


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
	meme_tweets = "~ " + tweet.user.name
for tweet in cfg_tweets:      
    meme_tweets1 = tweet.text   


cfg_tweets1 = twitter_api.search(
    q = "TheMemeMerchant" #Twitter handle you want to search by
)

for tweet in cfg_tweets1:
    meme_tweets2 = "~ " + tweet.user.name   
for tweet in cfg_tweets1:      
    meme_tweets3 = tweet.text 

 
cfg_tweets2 = twitter_api.search(
    q = "FreeMemesKids" #Twitter handle you want to search by
)

for tweet in cfg_tweets2:
    meme_tweets4 ="~ " +  tweet.user.name
for tweet in cfg_tweets2:      
    meme_tweets5 = tweet.text 


  
cfg_tweets3 = twitter_api.search(
    q = "theMemesBot" #Twitter handle you want to search by
)

for tweet in cfg_tweets3:
    meme_tweets6 ="~ " +  tweet.user.name
for tweet in cfg_tweets3:      
    meme_tweets7 = tweet.text 


@app.route('/trends')                         
def trends():
    return render_template('trends.html', variable=meme_tweets, variable1=meme_tweets1, variable2=meme_tweets2, vaiable3=meme_tweets3, variable4=meme_tweets4, variable5=meme_tweets5, variable6=meme_tweets6, variable7=meme_tweets7)
 		
 
app.run(debug=True) 
      
   

# @app.route('/result',methods = ['POST', 'GET'])
#def result():   
 #  if request.method == 'POST':
  #    result = request.form
   #   return render_template("result.html",result = result)
                  