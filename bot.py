import tweepy
import time
from sportsipy.mlb.roster import Player
import datetime
x = datetime.datetime.now()

print('Twitter bot active', flush=True)

#API keys from twitter
#Add your own here
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_KEY = ""
ACCESS_SECRET = ""

auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)
api = tweepy.API(auth)

#Most recent tweet stored in text file
FILE_NAME = "last_seen_id.txt"

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    print (str(last_seen_id))
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
        #Different replies for different hashtags
        if "#starter" in mention.full_text.lower() or "#pitcher" in mention.full_text.lower():
            print("Hashtag found", flush=True)
            print("Responding back...", flush=True)
            api.update_status("@" + mention.user.screen_name + " " +
                    x.strftime("%A") +", "+ x.strftime("%B") +" "+ x.strftime("%d")+", "+ x.strftime("%Y") + "\n" + 
                    "Starting today: " + starting_pitcher + "\n" + 
                    "W/L: " + win_loss + "\n" + 
                    "ERA: " + era, mention.id)
        if "#gausman" in mention.full_text.lower() or "#kevin" in mention.full_text.lower():
            print("Hashtag found", flush=True)
            print("Responding back...", flush=True)
            gausman = Player("gausmke01")
            starting_pitcher = "Kevin Gausman"
            win_loss = str(gausman("2022").wins) + " - " + str(gausman("2022").losses)
            era = str(gausman("2022").era)
            whip = str(gausman("2022").whip)
            k_9 = str(gausman("2022").batters_struckout_per_nine_innings)
            games_started = str(gausman("2022").games_pitcher)
            innings = str(gausman("2022").innings_played)
            h_9 = str(gausman("2022").hits_against_per_nine_innings)
            api.update_status("@" + mention.user.screen_name + " " +
                    starting_pitcher + "\n" +
                    "GS: " + games_started + "\n" + 
                    "IP: " + innings + "\n" + 
                    "W/L: " + win_loss + "\n" + 
                    "ERA: " + era + "\n" +
                    "WHIP: " + whip + "\n" +
                    "H/9: " + h_9 + "\n" +
                    "K/9: " + k_9 + "\n" 
                    , mention.id)
        if "#manoah" in mention.full_text.lower() or "#alek" in mention.full_text.lower():
            print("Hashtag found", flush=True)
            print("Responding back...", flush=True)
            manoah = Player("manoaal01")
            starting_pitcher = "Alek Manoah 🔥🤘"
            win_loss = str(manoah("2022").wins) + " - " + str(manoah("2022").losses)
            era = str(manoah("2022").era)
            whip = str(manoah("2022").whip)
            k_9 = str(manoah("2022").batters_struckout_per_nine_innings)
            games_started = str(manoah("2022").games_pitcher)
            innings = str(manoah("2022").innings_played)
            h_9 = str(manoah("2022").hits_against_per_nine_innings)
            api.update_status("@" + mention.user.screen_name + " " +
                    starting_pitcher + "\n" +
                    "GS: " + games_started + "\n" + 
                    "IP: " + innings + "\n" + 
                    "W/L: " + win_loss + "\n" + 
                    "ERA: " + era + "\n" +
                    "WHIP: " + whip + "\n" +
                    "H/9: " + h_9 + "\n" +
                    "K/9: " + k_9 + "\n" 
                    , mention.id)
        if "#berrios" in mention.full_text.lower() or "#jose" in mention.full_text.lower():
            print("Hashtag found", flush=True)
            print("Responding back...", flush=True)
            berrios = Player("berrijo01")
            starting_pitcher = "José Berríos 🦾"
            win_loss = str(berrios("2022").wins) + " - " + str(berrios("2022").losses)
            era = str(berrios("2022").era)
            whip = str(berrios("2022").whip)
            k_9 = str(berrios("2022").batters_struckout_per_nine_innings)
            games_started = str(berrios("2022").games_pitcher)
            innings = str(berrios("2022").innings_played)
            h_9 = str(berrios("2022").hits_against_per_nine_innings)
            api.update_status("@" + mention.user.screen_name + " " +
                    starting_pitcher + "\n" +
                    "GS: " + games_started + "\n" + 
                    "IP: " + innings + "\n" + 
                    "W/L: " + win_loss + "\n" + 
                    "ERA: " + era + "\n" +
                    "WHIP: " + whip + "\n" +
                    "H/9: " + h_9 + "\n" +
                    "K/9: " + k_9 + "\n" 
                    , mention.id)
        if "#kikuchi" in mention.full_text.lower() or "#yusei" in mention.full_text.lower():
            print("Hashtag found", flush=True)
            print("Responding back...", flush=True)
            kikuchi = Player("kikucyu01")
            starting_pitcher = "Yusei Kikuchi 🇯🇵"
            win_loss = str(kikuchi("2022").wins) + " - " + str(kikuchi("2022").losses)
            era = str(kikuchi("2022").era)
            whip = str(kikuchi("2022").whip)
            k_9 = str(kikuchi("2022").batters_struckout_per_nine_innings)
            games_started = str(kikuchi("2022").games_pitcher)
            innings = str(kikuchi("2022").innings_played)
            h_9 = str(kikuchi("2022").hits_against_per_nine_innings)
            api.update_status("@" + mention.user.screen_name + " " +
                    starting_pitcher + "\n" +
                    "GS: " + games_started + "\n" + 
                    "IP: " + innings + "\n" + 
                    "W/L: " + win_loss + "\n" + 
                    "ERA: " + era + "\n" +
                    "WHIP: " + whip + "\n" +
                    "H/9: " + h_9 + "\n" +
                    "K/9: " + k_9 + "\n" 
                    , mention.id)
        if "#stripling" in mention.full_text.lower() or "#ross" in mention.full_text.lower():
            print("Hashtag found", flush=True)
            print("Responding back...", flush=True)
            stripling = Player("stripro01")
            starting_pitcher = "Ross Stripling 🍗"
            win_loss = str(stripling("2022").wins) + " - " + str(stripling("2022").losses)
            era = str(stripling("2022").era)
            whip = str(stripling("2022").whip)
            k_9 = str(stripling("2022").batters_struckout_per_nine_innings)
            games_started = str(stripling("2022").games_pitcher)
            innings = str(stripling("2022").innings_played)
            h_9 = str(stripling("2022").hits_against_per_nine_innings)
            api.update_status("@" + mention.user.screen_name + " " +
                    starting_pitcher + "\n" +
                    "GS: " + games_started + "\n" + 
                    "IP: " + innings + "\n" + 
                    "W/L: " + win_loss + "\n" + 
                    "ERA: " + era + "\n" +
                    "WHIP: " + whip + "\n" +
                    "H/9: " + h_9 + "\n" +
                    "K/9: " + k_9 + "\n" 
                    , mention.id)
        if "#ryu" in mention.full_text.lower() or "#hyunjin" in mention.full_text.lower():
            print("Hashtag found", flush=True)
            print("Responding back...", flush=True)
            ryu = Player("ryuhy01")
            starting_pitcher = "Hyun Jin Ryu 🇰🇷👹"
            win_loss = str(ryu("2022").wins) + " - " + str(ryu("2022").losses)
            era = str(ryu("2022").era)
            whip = str(ryu("2022").whip)
            k_9 = str(ryu("2022").batters_struckout_per_nine_innings)
            games_started = str(ryu("2022").games_pitcher)
            innings = str(ryu("2022").innings_played)
            h_9 = str(ryu("2022").hits_against_per_nine_innings)
            api.update_status("@" + mention.user.screen_name + " " +
                    starting_pitcher + "\n" +
                    "GS: " + games_started + "\n" + 
                    "IP: " + innings + "\n" + 
                    "W/L: " + win_loss + "\n" + 
                    "ERA: " + era + "\n" +
                    "WHIP: " + whip + "\n" +
                    "H/9: " + h_9 + "\n" +
                    "K/9: " + k_9 + "\n" 
                    , mention.id)
        if "#romano" in mention.full_text.lower() or "#jordan" in mention.full_text.lower():
            print("Hashtag found", flush=True)
            print("Responding back...", flush=True)
            romano = Player("romanjo03")
            starting_pitcher = "Jordan Romano 🍁"
            saves = str(romano("2022").saves)
            era = str(romano("2022").era)
            whip = str(romano("2022").whip)
            k_9 = str(romano("2022").batters_struckout_per_nine_innings)
            games_started = str(romano("2022").games_pitcher)
            innings = str(romano("2022").innings_played)
            h_9 = str(romano("2022").hits_against_per_nine_innings)
            api.update_status("@" + mention.user.screen_name + " " +
                    starting_pitcher + "\n" +
                    "GP: " + games_started + "\n" + 
                    "IP: " + innings + "\n" + 
                    "Saves: " + saves + "\n" + 
                    "ERA: " + era + "\n" +
                    "WHIP: " + whip + "\n" +
                    "H/9: " + h_9 + "\n" +
                    "K/9: " + k_9 + "\n" 
                    , mention.id)

def pitcher_gausman():
    gausman = Player("gausmke01")
    starting_pitcher = "Kevin Gausman"
    win_loss = str(gausman("2022").wins) + " - " + str(gausman("2022").losses)
    era = str(gausman("2022").era)
    return [starting_pitcher, win_loss, era]

def pitcher_manoah():
    manoah = Player("manoaal01")
    starting_pitcher = "Alek Manoah 🔥🤘"
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
    ryu = Player("ryuhy01")
    starting_pitcher = "Hyun Jin Ryu 🇰🇷👹"
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

#Hard-coded issue to be fixed
probable = "kikuchi"

while True:
    reply_to_tweets(pitcher(probable)[0],pitcher(probable)[1],pitcher(probable)[2])
    time.sleep(10)
