wordlist = ["Node","foo","framework","txt","micro"]
tweet = "This is an example tweet talking about Node and its framework"
print([w for w in wordlist if(w in tweet)])
#print(map(lambda x : x in tweet.split(), wordlist))