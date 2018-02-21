import os


numbertoconsider = int(input("Enter a number :"))
                         
array = []
with open("india.txt", "r",encoding="utf-8") as f:
  for line in f:
    array.append(line)

userData = []

class TwitterUser:
     def __init__(self, name, followers, tweets):
         self.name = name
         self.followers = followers
         self.tweets = tweets
     def __repr__(self):
         return repr((self.name, self.followers, self.tweets))
     def __eq__(self,other):
        return self.name==other.name
     def __hash__(self):
        return self.followers

for i in range(0,len(array)):
    data = array[i].split(" ")
    xfollowers = len(data)-2
    xtweets = len(data)-1
    #print(data[xtweets].replace("\n",""))
    userObj = TwitterUser(data[0],int(data[xfollowers]),int(data[xtweets].replace("\n","")))
    userData.append(userObj)
    #userData.append(data[0]+" "+data[datalen])

noduplicates = list(set(userData))

sortedFollowerList  = sorted(noduplicates, key=lambda twitter: twitter.followers,reverse=True)
sortedTwitterList  = sorted(noduplicates, key=lambda twitter: twitter.tweets,reverse=True)



mostfollowers=open("mostfollowers.txt","w",encoding="utf-8")

for x in range(0,numbertoconsider):
    mostfollowers.write(sortedFollowerList[x].name+" "+ str(sortedFollowerList[x].followers) +"\n")
    mostfollowers.flush()

mostfollowers=open("mosttweets.txt","w",encoding="utf-8")

for x in range(0,numbertoconsider):
    mostfollowers.write(sortedTwitterList[x].name+" "+ str(sortedTwitterList[x].tweets) +"\n")
    mostfollowers.flush()

print(len(sortedFollowerList))
