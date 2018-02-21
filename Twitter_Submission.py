import shlex

class TwitterAccount:
    tweet_id = ""
    followers = 0
    time = ""
    re_tweet = 0
    count = 0
    def __init__(self, tweet_id, time, followers, re_tweet, count):
        self.tweet_id = tweet_id
        self.followers = followers
        self.time = time
        self.re_tweet = re_tweet
        self.count = count
    def fetch_tweet_id(self):
        return self.tweet_id
    def fetch_time(self):
        return self.time
    def fetch_followers(self):
        return self.followers
    def fetch_re_tweet(self):
        return self.re_tweet
    def count_value(self):
        return self.count
    def increae_count(self):
        self.count = self.count + 1;

numbertoconsider = int(input("Enter a number :"))
cou = []
file = open('india.txt','r', encoding='utf-8')
ids = {}
hrs = {}
for line in file:
    list1 = line.split()

    acc = TwitterAccount(list1[0],list1[1][1:15],int(list1[-2]), int(list1[-1]),1)
    ac = TwitterAccount(list1[0],list1[1][1:15],int(list1[-2]), int(list1[-1]),1)
    
    cou.append(ac)
    
    if ids is None:
        ids[list1[0]] = acc
    elif list1[0] not in ids:
        ids[list1[0]] = acc
    else:
        acc1 = ids.pop(list1[0])
        acc1.increae_count()
        ids[list1[0]] = acc1
    
    if hrs is None:
        val = []
        val.append(ac)
        hrs[list1[1][1:15]] = val
    elif list1[1][1:15] not in hrs:
        val1 = []
        val1.append(ac)
        hrs[list1[1][1:15]] = val1
    else:
        hr = []
        hr = list(hrs.pop(list1[1][1:15]))
        hr.append(ac)
        hrs[list1[1][1:15]] = hr
        
mostuser = open("most_users.txt","w",encoding="utf-8")
mosthour = open("most_tweets.txt","w",encoding="utf-8")
mostfollowers = open("most_followers.txt","w",encoding="utf-8")
mosttweets = open("most_Retweets.txt","w",encoding="utf-8")

mostuser.write("The top "+ str(numbertoconsider) + " users who have tweeted the most for the entire timeline." + "\n")

tweets = list(ids.values())

max_count = tweets

max_count.sort(key=lambda x: x.count, reverse=True)

for x in range(0,numbertoconsider):
    mostuser.write("Tweet ID:"+max_count[x].fetch_tweet_id()+ ", Tweet Count:"+ str(max_count[x].count_value()) +"\n")
    mostuser.flush()

mosthour.write("The top "+ str(numbertoconsider) + " users who have tweeted the most for every hour." + "\n")

j = 0
for key, value in hrs.items():
    a = []
    a = list(value)
    
    b = {}
    for i in a:
        
        if b is None:
            b[i.fetch_tweet_id()] = i
        elif i.fetch_tweet_id() not in b:
            b[i.fetch_tweet_id()] = i
        else:
            acc1 = b.pop(i.fetch_tweet_id())
            acc1.increae_count()
            b[i.fetch_tweet_id()] = acc1
    j = j + 1
    val = []
    val = list(b.values())
    
    max_count = val

    max_count.sort(key=lambda x: x.count, reverse=True)

    for x in range(0,len(val)):
        mosthour.write("Tweet ID:"+max_count[x].fetch_tweet_id()+ ", Tweet Time:"+  max_count[x].fetch_time()+ ", Tweet Count:"+  str(max_count[x].count_value()) +"\n")
        mosthour.flush()
        
mostfollowers.write("The top "+ str(numbertoconsider) + " users who have the maximum followers." + "\n")
max_followers = cou

max_followers.sort(key=lambda x: x.followers, reverse=True)

for x in range(0,numbertoconsider):
    mostfollowers.write(max_followers[x].fetch_tweet_id()+ ", TwitterAccount Followers:"+  str(max_followers[x].fetch_followers())+"\n")
    mostfollowers.flush()    

mosttweets.write("The top "+ str(numbertoconsider) + " tweets which have the maximum retweet count." + "\n")

max_re_tweets = cou

max_re_tweets.sort(key=lambda x: x.re_tweet, reverse=True)

for x in range(0,numbertoconsider):
    mosttweets.write(max_re_tweets[x].fetch_tweet_id()+ ", Tweet Re_Tweet count:"+  str(max_re_tweets[x].fetch_re_tweet()) +"\n")
    mosttweets.flush()    


