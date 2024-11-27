import argparse
import json 
#from loadData import load_file
def load_file(input_file):
    tmp=[]
    with open(input_file) as file:
        for jsonObj in file:
            try:
                jdict=json.loads(jsonObj)
                tmp.append(jdict)
            except ValueError:
                continue
    return tmp

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('src_file', help='input file should be a json', default = 'NA')
    args=parser.parse_args()
    input_file=args.src_file

    tmp=load_file(input_file)
    acc=0.0
    for post in tmp:
        acc=acc+len(post['data']['title'])  
    print(round(acc/1000,2))


if __name__ == "__main__":
    main()
