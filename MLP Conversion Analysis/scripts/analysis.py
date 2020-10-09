import pandas as pd
import sys
import os
import argparse
import json 
import io

from hw3.cleanData import cleanData
from hw3.verbosity import gen_verbosity
from hw3.mentions import gen_mentions
from hw3.follow import followOnComments
from hw3.dictionary import nonDictionary

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('src_file',help='the tweet file that will he used ... should be a csv')
    parser.add_argument('-output', help = 'The output json path and name', default = 'NA', nargs="?")
    args=parser.parse_args()
    src_file = args.src_file

    # data cleaning
    df=pd.read_csv(src_file)
    df_new=df.copy()
    cleanData(df_new)    
    df_new['index1']=[i for i in range (len(df_new))]
    df_new=df_new.set_index(df_new.index1)

    # call: verbosity
    verbosity = gen_verbosity(df_new) 

    # call: mentions
    mentions=gen_mentions(df_new)

    # call: follow_on_comments
    follow=followOnComments(df_new)

    # call: non_dictionary words
    DICTIONARY_PATH=os.path.join(os.path.dirname(__file__ ),'..','data','words_alpha.txt')
    word=pd.read_csv(DICTIONARY_PATH, header=None)
    #word=pd.read_csv('../data/words_alpha.txt', header=None)
    word.columns = ["word"]
    wordList=[i for i in word['word']]
    non_Dictionary=nonDictionary(df_new, wordList) 
    
    output = {"verbosity":verbosity,
            "mentions":mentions,
            "follow_on_comments": follow,
            "non_dictionary_words": non_Dictionary}

    if args.output == 'NA':
        print(json.dumps(output,indent=4))
    else:
        with open(args.output, "w") as write_file:
            json.dump(output, write_file, indent=4)



    





if __name__ == "__main__":
    main()