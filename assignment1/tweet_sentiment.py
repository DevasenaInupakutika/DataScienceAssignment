import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def json_python_dic(tweet_file):
    
    python_tweet_dic = {} # Initialising an empty python dictionary

    file_object = open('problem_1_submission.txt','r')
    file_object2 = file_object.read()

    tweet_file_string = open(tweet_file)

    for line in tweet_file_string:
           
                
       

def main():
    # sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    # hw()
    # lines(sent_file)
    lines(tweet_file)

    afinnfile = open(sys.argv[1])
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    print scores.items() # Print every (term, score) pair in the dictionary


if __name__ == '__main__':
    main()
