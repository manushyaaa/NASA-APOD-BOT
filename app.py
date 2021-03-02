from nasapy import Nasa
import wget
import datetime
import os
import re
import tweepy
from time import sleep

KEY = os.environ['KEY']
access_token = os.environ['access_token']
access_token_secret = os.environ['access_token_secret']
consumer_key = os.environ['consumer_key']
consumer_secret = os.environ['consumer_secret']
nasa = Nasa(key=KEY)


def bot():
    dateToday = str(datetime.date.today())
    apod_image = nasa.picture_of_the_day(hd=True)
    print(apod_image['hdurl'])

    explanation = apod_image['explanation']
    explanation_list = re.split('[.!?]', explanation)

    status = f"{explanation_list[0]}. #NASA #APOD"
    print(status)

    image = f'./images/{dateToday}.jpg'

    wget.download(apod_image['hdurl'], f'./images/{dateToday}.jpg')

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    bot = tweepy.API(auth)
    bot.update_with_media(image, status)
    print("------------------------APOD UPLOADED------------------------")

    if os.path.exists('./images/' + dateToday + '.jpg'):
        print('Image is present')
        os.remove(image)
    else:
        print("Image not present")


while True:
    bot()
    print('------------------------SLEEPING------------------------')
    sleep(3600)
