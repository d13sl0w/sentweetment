import sys
import json
from pprint import pprint
import operator

def hw():
       print type(tweet_file)

def lines(fp):
       print str(len(fp.readlines()))

def main():
        data = []
        with open(sys.argv[1]) as f:
                for line in f:
                        data.append(json.loads(line))
	top = {}
        for tweet in data:
		if ("entities" in tweet):
			if len(tweet["entities"]["hashtags"]) != 0:
				for hashes in tweet["entities"]["hashtags"]:
					if hashes["text"] in top:
						top[hashes["text"]] = top[hashes["text"]] + 1
					else:
						top[hashes["text"]] = 1
							
       	sorted_top = sorted(top.iteritems(), key=operator.itemgetter(1), reverse=True)
	sorted_ten = sorted_top[0:10]
	for bump in sorted_ten:
		print "%s %d" % (bump[0], bump[1])

		

if __name__ == '__main__':
    main()

