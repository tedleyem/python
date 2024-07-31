from flask import Flask, render_template
#from tweet_store import TweetStore

app = Flask(__name__)
#store = TweetStore()

@app.route('/')
def index():
    #tweets = store.tweets()
    return render_template('index.html',) # call index.html file with rendered header adn footer

@app.route("/contact")
def contact():
    return render_template('contact.html',) # call index.html file with rendered header adn footer

if __name__ == '__main__':
    app.run(debug=True) # run debug mode if something fails
