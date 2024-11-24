import json
import argparse
import math


def calculate_idf(tmp):
    dict={}
    num_words=0
    ponies=list(tmp.keys())
    # total number of words
    # number of instances of each words
    for pony in ponies:
        dict_pony=tmp[pony]
        word_list=list(dict_pony.keys())
        for word in word_list:
            word_frequency=dict_pony[word]
            num_words=num_words+word_frequency
            if word in dict:
                dict[word]=dict[word]+word_frequency
            else:
                dict[word]=tmp[pony][word] 
    #calculate idf
    for word in dict:
        dict[word]=math.log(num_words/dict[word])

    return dict

def calculate_new_idf(tmp):
    num_ponies=len(tmp)
    dict={}
    ponies=list(tmp.keys())
    for pony in ponies:
        dict_pony=tmp[pony]
        word_list=list(dict_pony.keys())
        for word in word_list:
            if word in dict:
                dict[word]=dict[word]+1
            else:
                dict[word]=1
    #calculate idf
    for word in dict:
        dict[word]=math.log(num_ponies/dict[word])
    return dict



def calculate_df_idf(tmp,dict,num):
    output={}
    ponies=list(tmp.keys())
    for pony in ponies:
        word_list=list(tmp[pony].keys())
        for word in word_list:
            tmp[pony][word]=(tmp[pony][word])*dict[word]
        # 5 largest tf-idf word 
        sorted_list=[k for k, v in sorted(tmp[pony].items(), key=lambda item: item[1],reverse=True)]
        output[pony]=sorted_list[0:int(num)]

        #output=sorted(tmp[pony].values() )
    print(json.dumps(output))
    #return output
        



def load_file(input_file):
   try:
       file = open(input_file, "r").read()
       json_object = json.loads(file)
   except ValueError:
       print("error with loading json")
 
   return json_object


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('-p',help='Please provide the flag',default='NA', action='store_true')
    parser.add_argument('input_file',help="Please provide the input json file")
    parser.add_argument('num_words',help="Please provide the number of words")
    args=parser.parse_args()

    input_file=args.input_file
    num=args.num_words

    tmp=load_file(input_file)
    if args.p =='NA':
        dict=calculate_idf(tmp)
    else:
        dict=calculate_new_idf(tmp)

    calculate_df_idf(tmp,dict,num)
    #print(calculate_df_idf(tmp,dict,num))
    








if __name__ =="__main__":
    main()