import tweepy
import time

auth = tweepy.OAuthHandler("Tn8ve6WZQSLBuO7OVFlJKv8FJ", "vEpt1NxfNfHLGLuUW2wfrgqCJB81nxQtmf1m1MgCmjP7ZHGbVN")
auth.set_access_token("1470697400515710979-IejAM3FBT4bSqhdeHQdxL8XTbStM33",
                      "5Pz0hG2qwi4PZ94OPUdvRlskFQdZhYPNKQae638q4gvdZ")

api = tweepy.API(auth)

user = api.me()


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)


for follower in limit_handler(tweepy.cursor(api.followers).items()):
    if follower.name == "something":
        follower.follow()
        break




