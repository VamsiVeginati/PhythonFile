import shlex

class Account:
    tweet_id = ""
    followers = ""
    time = ""
    re_tweet = ""
    tweet = ""
    count = 0
    def __init__(self, tweet_id, time, followers,tweet , re_tweet, count):
        self.tweet_id = tweet_id
        self.followers = followers
        self.time = time
        self.re_tweet = re_tweet
        self.tweet = tweet
        self.count = count
    def fetch_tweet_id(self):
        return self.tweet_id
    def fetch_time(self):
        return self.time
    def fetch_followers(self):
        return self.followers
    def fetch_tweet(self):
        return self.tweet
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

    acc = Account(list1[0],list1[1][1:15],int(list1[-2]), line,int(list1[-1]),1)
    
    cou.append(acc)
    
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
        val.append(acc)
        hrs[list1[1][1:15]] = val
    elif list1[1][1:15] not in hrs:
        val1 = []
        val1.append(acc)
        hrs[list1[1][1:15]] = val1
    else:
        hr = []
        hr = list(hrs.pop(list1[1][1:15]))
        hr.append(acc)
        hrs[list1[1][1:15]] = hr
        

mostuser = open("mostusers.txt","w",encoding="utf-8")
mosthour = open("mosthours.txt","w",encoding="utf-8")
mostfollowers = open("mostfollowers.txt","w",encoding="utf-8")
mosttweets = open("mostretweets.txt","w",encoding="utf-8")

mostuser.write("The top "+ str(numbertoconsider) + " users who have tweeted the most for the entire timeline." + "\n")

tweets = list(ids.values())

max_count = tweets

max_count.sort(key=lambda x: x.count, reverse=True)

for x in range(0,numbertoconsider):
    mostuser.write(max_count[x].fetch_tweet()+"\n")
    mostuser.flush()

mosthour.write("The top "+ str(numbertoconsider) + " users who have tweeted the most for every hour." + "\n")

for key, value in hrs.items():
    a = []
    a = list(value)
    b = {}
    for i in a:
        if b is None:
            b[i.fetch_tweet_id()+i.fetch_time()] = i
        elif str(i.fetch_tweet_id()+i.fetch_time()) not in b:
            b[i.fetch_tweet_id()+i.fetch_time()] = i
        else:
            acc1 = b.pop(i.fetch_tweet_id()+i.fetch_time())
            acc1.increae_count()
            b[i.fetch_tweet_id()+i.fetch_time()] = acc1
    val = []
    val = list(b.values())
    
    max_count = val

    max_count.sort(key=lambda x: x.count, reverse=True)

    for x in range(0,numbertoconsider):
        mosthour.write(max_count[x].fetch_tweet() +"\n")
        mosthour.flush()
        
mostfollowers.write("The top "+ str(numbertoconsider) + " users who have the maximum followers." + "\n")
max_followers = cou

max_followers.sort(key=lambda x: x.followers, reverse=True)

for x in range(0,numbertoconsider):
    mostfollowers.write(max_followers[x].fetch_tweet()+"\n")
    mostfollowers.flush()    

mosttweets.write("The top "+ str(numbertoconsider) + " tweets which have the maximum retweet count." + "\n")

max_re_tweets = cou

max_re_tweets.sort(key=lambda x: x.re_tweet, reverse=True)

for x in range(0,numbertoconsider):
    mosttweets.write(max_re_tweets[x].fetch_tweet() +"\n")
    mosttweets.flush()    


