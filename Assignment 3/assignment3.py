#Assignment 3
#Hannah Zontine

from sentiment import *
from twitter_util import *

popcornwords= []
def fillStopwords(popcornwords):
	data = open("popcornwords.txt", 'rb').read().split("\r\n")
	for line in data:
		try:
			popcornwords.append(line)
		except:
			print("JSON-unopenable tweet encountered")
	return popcornwords
popcornwords= fillPopcornwords(popcornwords)
print(popcornwords)
	
def get_rank_tweets(tweet_file, n):
	codes = get_sentiment_codes("../util-data-files/AFINN-111.txt")
	tweets = read_tweets(tweet_file)
	scores = {}
	sum = 0
	for line in tweets:
		if "text" in line.keys():
			txt = text(line, 'text').split()
			score = 0
			other_words = []
			for word in txt:
				sum += 1
				if word[0] == "@" or word[0] == "`" or word[0] == "#" or word[0] =="&" or word =="RT" or word[0] =="!" or word[0] =="?" or(word in popcornwords):
					continue
				if word in codes:
					score += codes[word]
				else:
					other_words.append(word)
					if word  not in scores.keys():
						scores[word] = [0,1]
					else: 
						scores[word] = scores[word]
						scores[word][1] += 1
				for word in other_words:
					scores[word][0] += score
		else:
			continue 	
	print(sum)
			
	#Normalize
	for s in scores:
		scores[s] = scores[s][0] / scores[s][1]

	#Order by Value
	sort = sorted(scores.items(),key = lambda x : x[1])
	
	#print first n
	print("Unhappiest words-----------------")
	for i in range(n):
		print(sort[i])
		print("\n")
	
	sort.reverse()
	print("Happiest words-------------------")
	for i in range(n):
		print(sort[i])
		print("\n")	
	
