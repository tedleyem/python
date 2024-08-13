#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, render_template, redirect, request
import logging
from logging import Formatter, FileHandler
from wtforms import *

#----------------------------------------------------------------------------#
# Twitter Auth variables
#----------------------------------------------------------------------------#
#consumer_id = ""
#consumer_key = ""
#callback_uri = "oob"
#ACCESS_TOKEN = ""
#ACCESS_TOKEN_SECRET = ""
#auth = tweepy.OAuthHandler(consumer_id, consumer_key, callback_uri)
#auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
#api = tweepy.API(auth)

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#
# IG Scraper
def instasdetails():
    URL = "https://www.twitter.com/{}/"

# Twitter Scraper
def instascraper():
    URL = "https://www.instagram.com/{}/"



# Web Links.
@app.route('/', methods=['POST', 'GET'])
def home():
    return render_template("pages/home.html")
    instascraper

@app.route('/about')
def about():
    return render_template("pages/about.html")

@app.route('/bugs', methods=["GET"])
def dev_contact():
    return redirect('https://github.com/tedleyem', code=302)

@app.route('/refresh', methods=['POST', 'GET'])
def refresh():
    return render_template("pages/home.html")

@app.route('/twitter-woj', methods=["GET"])
def twitter_woj():
    return redirect('https://twitter.com/wojespn', code=302)

@app.route('/insta-woj', methods=["GET"])
def insta_woj():
    return redirect('https://www.instagram.com/wojespn', code=302)

@app.route('/espn-woj', methods=["GET"])
def espn_woj():
    return redirect('https://www.espn.com/nba/world-of-woj/', code=302)

@app.route('/wiki-woj', methods=["GET"])
def wiki_woj():
    return redirect('https://en.wikipedia.org/wiki/Adrian_Wojnarowski#:~:text=His%20scoops%20have%20been%20referred,%22%20gifs%2C%20for%20comedic%20effect', code=302)

@app.route('/donate', methods=["GET"])
def dontate():
    return redirect('https://buymeacoffee.com/techdadteddy', code=302)

@app.route('/contact', methods=["GET"])
def contact():
    return redirect('https://www.twitter.com/techdadteddy', code=302)

# Error handlers.
@app.errorhandler(500)
def internal_error(error):
    return render_template('errors/500.html'), 500

@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
