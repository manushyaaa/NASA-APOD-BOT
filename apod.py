from nasapy import Nasa
import wget
import datetime
import os
import re
import tweepy
from time import sleep

KEY = "qxsEkJhi52IftWxPAcfzmbFvSFGqHtoxGZzImnhx"

access_token = "1316993009037111297-QRWNgFrcI8kudT1NOmQ5qo01MZOD6l"
access_token_secret = "415nEzYGq0vTdagRKGZHuESZujX3XUuffsVVUR0DVsNUN"
consumer_key = "hju9PIe1eNLOi0Kg2HDnGZNkZ"
consumer_secret = "vN47kaaKohrV7csZqZEc8Qqr3jAYjZ0ZSzJ2EiSNrN5puo2NN6"


nasa = Nasa(key=KEY)


def bot():
    dateToday = str(datetime.date.today())
    apod_image = nasa.picture_of_the_day(hd=True)
    print(apod_image['hdurl'])

    explanation = apod_image['explanation']
    explanation_list = re.split('[.!?]', explanation)

    status = f"{explanation_list[0]}. #NASA #APOD #SpaceX"
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


bot()
