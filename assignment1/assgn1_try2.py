import sys
import json

tweets = []

for line in open(sys.argv[1]):
  try: 
    tweets.append(json.loads(line))
  except:
    pass

print 'Tweets:', json.dumps(tweets, indent=4)
print 'Keys in Tweets:',tweets[5].keys()

for i in range(1,len(tweets)):
    try:
        if 'text' in tweets[i]:
           print 'Tweet ', i,':',tweets[i]['text']
        else:
           print 'Everything ', i,':',tweets[i]
    
    except:
        print 'Exception: ',tweets[i]



