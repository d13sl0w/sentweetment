import sys
import json
from pprint import pprint

#def hw():
#       print type(tweet_file)
#
#def lines(fp):
#       print str(len(fp.readlines()))
#
def main():
        data = []
        with open(sys.argv[1]) as f:
                for line in f:
                        data.append(json.loads(line))
        sentscore = []
        for objext in data:
                if "text" in objext:
                        sentscore.append(objext["text"])
	wordcount = {}
        for text in sentscore:
                for word in text.split():
                        if word in wordcount:
				wordcount[word] = wordcount[word] + 1
                        else:
				wordcount[word] = 1
	
	total = sum(wordcount.itervalues())
	
	freq = {}
	for key in wordcount:
		freq[key] = (float(wordcount[key]) / total)

	for key in freq:
		print"%s %f" % (key, freq[key])

if __name__ == '__main__':
    main()

