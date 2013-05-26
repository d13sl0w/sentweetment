import sys
import json
from pprint import pprint

def hw():
       print type(tweet_file)

def lines(fp):
       print str(len(fp.readlines()))

def main():
        sent_file = open(sys.argv[1])
        afinnfile = sent_file
        scores = {}
        for line in afinnfile:
                term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
                scores[term] = int(score)

        data = []
        with open(sys.argv[2]) as f:
                for line in f:
                        data.append(json.loads(line))
        placename = []
	sentscore = []
	twolists = []
	states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
        for objext in data:
                if "place" in objext and "text" in objext != None and objext["place"] != None:
                        placer = (objext["place"]["full_name"]).split()
			if (len(placer) != 1) and (placer[1] in states):
				twolists.append([placer[1], objext["text"]])

	statescores = {}
        for pair in twolists:
		i = 0
                for word in pair[1].split():
                        if word in scores:
                                i = i + scores[word]
                if pair[0] in statescores:
			statescores[pair[0]] = statescores[pair[0]] + i
		else:
			 statescores[pair[0]] = 0

	v = list(statescores.values())
	k = list(statescores.keys())
	print k[v.index(max(v))]

if __name__ == '__main__':
    main()
                                                                              
               
