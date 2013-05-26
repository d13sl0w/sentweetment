import sys
import json

#def hw():
#    	print type(tweet_file)
#
#def lines(fp):
#   	print str(len(fp.readlines()))
#
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

	for text in sentscore:
		i = 0	
		for word in text.split():
			if word in scores:
				i = i + scores[word]
		print i

if __name__ == '__main__':
    main()
