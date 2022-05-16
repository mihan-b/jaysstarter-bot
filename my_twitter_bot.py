import tweepy
import time
from sportsipy.mlb.roster import Player
import datetime
x = datetime.datetime.now()

print('Twitter bot active', flush=True)

#API Keys go here
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_KEY = ""
ACCESS_SECRET = ""

auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = "last_seen_id.txt"

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    print ("id"+str(last_seen_id))
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

last_seen_id = retrieve_last_seen_id(FILE_NAME)
mentions = api.mentions_timeline()

def reply_to_tweets(starting_pitcher, win_loss, era ):
    print("Searching for and replying to tweets...", flush=True)
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(last_seen_id, tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id) + "-" + mention.full_text, flush=True)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if "#starter" in mention.full_text.lower() or "#pitcher" in mention.full_text.lower():
            print("Hashtag found", flush=True)
            print("Responding back...", flush=True)
            api.update_status("@" + mention.user.screen_name + " " +
                    x.strftime("%A") +", "+ x.strftime("%B") +" "+ x.strftime("%d")+", "+ x.strftime("%Y") + "\n" + 
                    "Starting today: " + starting_pitcher + "\n" + 
                    "W/L: " + win_loss + "\n" + 
                    "ERA: " + era, mention.id)

def pitcher_gausman():
    gausman = Player("gausmke01")
    starting_pitcher = "Kevin Gausman"
    win_loss = str(gausman("2022").wins) + " - " + str(gausman("2022").losses)
    era = str(gausman("2022").era)
    return [starting_pitcher, win_loss, era]

def pitcher_manoah():
    manoah = Player("manoaal01")
    starting_pitcher = "Alek Manoah 🤘"
    win_loss = str(manoah("2022").wins) + " - " + str(manoah("2022").losses)
    era = str(manoah("2022").era)
    return [starting_pitcher, win_loss, era]

def pitcher_berrios():
    berrios = Player("berrijo01")
    starting_pitcher = "José Berríos 🦾"
    win_loss = str(berrios("2022").wins) + " - " + str(berrios("2022").losses)
    era = str(berrios("2022").era)
    return [starting_pitcher, win_loss, era]

def pitcher_kikuchi():
    kikuchi = Player("kikucyu01")
    starting_pitcher = "Yusei Kikuchi 🇯🇵"
    win_loss = str(kikuchi("2022").wins) + " - " + str(kikuchi("2022").losses)
    era = str(kikuchi("2022").era)
    return [starting_pitcher, win_loss, era]

def pitcher_stripling():
    stripling = Player("stripro01")
    starting_pitcher = "Ross Stripling 🍗"
    win_loss = str(stripling("2022").wins) + " - " + str(stripling("2022").losses)
    era = str(stripling("2022").era)
    return [starting_pitcher, win_loss, era]

def pitcher_ryu():
    ryu = Player("bryuhy01.")
    starting_pitcher = "Hyun Jin Ryu"
    win_loss = str(ryu("2022").wins) + " - " + str(ryu("2022").losses)
    era = str(ryu("2022").era)
    return [starting_pitcher, win_loss, era]

def pitcher (probable):
    if probable == "gausman":
        return pitcher_gausman()
    if probable == "manoah":
        return pitcher_manoah()
    if probable == "berrios":
        return pitcher_berrios()
    if probable == "kikuchi":
        return pitcher_kikuchi()
    if probable == "stripling":
        return pitcher_stripling()
    if probable == "ryu":
        return pitcher_ryu()
    else:
        print ("error")
        
#pitcher is hard-coded in this version, will be improved
probable = "kikuchi"

while True:
    reply_to_tweets(pitcher(probable)[0],pitcher(probable)[1],pitcher(probable)[2])
    time.sleep(10)
