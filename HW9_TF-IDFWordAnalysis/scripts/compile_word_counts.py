import json
import argparse
import pandas as pd

def count_word(pony,df):
    dict={}
    for index,row in df.iterrows():
        if pony in row['pony']:
            word_list=row['dialog'].split(" ")
            for word in word_list:
                if word.isalpha() is False:
                    continue
                if word in dict:
                    dict[word]=dict[word]+1
                else:
                    dict[word]=1
    # remove the word with frequency less than 5
    dict={key:val for key, val in dict.items() if val >= 5}

    return dict





def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('-o',required=True,help='Please provide the output json file',default='NA')
    parser.add_argument('input_file',help="Please provide the input dialog.csv")
    args=parser.parse_args()
    
    input_file=args.input_file
    df=pd.read_csv(input_file)
    # df convert punctuation and upper class
    df['dialog']=df['dialog'].replace('[()\[\],\-.?!:;#&]'," ", regex = True)
    df['dialog']=df['dialog'].str.lower()

    ponies=["Twilight Sparkle","Applejack","Rarity","Pinkie Pie","Rainbow Dash","Fluttershy"]
    ponies={"Twilight Sparkle":"twilight","Applejack":"applejack","Rarity":"rarity","Rainbow Dash":"rainbow","Pinkie Pie":"pinky","Fluttershy":"fluttershy"}
    output={}
    for pony in ponies:
        dict=count_word(pony,df)
        #output[pony]=dict
        pony_name=ponies[pony]
        output[pony_name]=dict
    with open(args.o,"w") as write_file:
        json.dump(output,write_file,indent=4)

    




if __name__ == "__main__":
    main()