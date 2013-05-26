import sys
import json
from pprint import pprint


def hw():
    print 'Hello, world!'

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
        sentscore = []
        for objext in data:
                if "text" in objext:
                        sentscore.append(objext["text"])
	org_sent = {}
	new_sent = {}
	final = {}
	j = 0
        for text in sentscore:
                i = 0
                for word in text.split():
                        if word in scores:
                                i = i + scores[word]
			elif word not in new_sent:
				new_sent[word] = [j]
			elif word in new_sent:
				new_sent[word].append(j)
       		org_sent[j] = i
		j = j + 1
	
	for key, value in new_sent.iteritems():
		k = 0
		for x in value:
			k = k + org_sent[x]
		final[key] = k	

	for key, value in final.iteritems():
		print "%s %d" % (key, value)
		
if __name__ == '__main__':
    main()
