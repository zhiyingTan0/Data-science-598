import argparse
import json 
import datetime
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
    parser.add_argument('-i',required=True,help='-i input file should be a json', default = 'NA')
    parser.add_argument('-o', required=True, help = '-o The output json path and name', default = 'NA')
    args=parser.parse_args()
    input_file = args.i
    
    #read input json into tmp
    tmp=load_file(input_file)
            
    for dict0 in tmp:
        if (dict0.get('title') is None) and (dict0.get('title_text') is None):
            tmp.remove(dict0)
        elif 'title_text' in dict0:
            dict0['title']=dict0.pop('title_text')

    for dict0 in tmp:
        if 'createdAt' in dict0:
            time=dict0['createdAt']
            try:
                time=datetime.datetime.strptime(time, '%Y-%m-%dT%H:%M:%S%z')
                utc_time=time.astimezone(datetime.timezone.utc)
                dict0['createdAt']=datetime.datetime.strftime(utc_time, '%Y-%m-%dT%H:%M:%S%z')
            except ValueError:
                tmp.remove(dict0)
                continue
    size=len(tmp[0].keys())         
    #output into several json (each line is one json dictionary)   {}{}{}        
    with open(args.o, "w") as write_file:
        for dict0 in tmp:
            json.dump(dict0, write_file)
            write_file.write('\n')
            #json.dump("\\n\\n",write_file)
            

    
    
    
    
    
if __name__ == "__main__":
    main()