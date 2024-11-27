import requests
import json
import os

def main():
    # write sample1
    sample1=[]
    sample1_subreddit=['funny','AskReddit','gaming','aww','pics','Music','science','worldnews','videos','todayilearned']

    for i in sample1_subreddit:
        data=requests.get(f'http://api.reddit.com/r/'+ i +'/new?limit=100',headers={'User-Agent':'windows:requests (by /u/winnie)'})
        content=data.json()['data']['children']
        for post in content:
            sample1.append(post)


    DICTIONARY_PATH1=os.path.join(os.path.dirname(__file__ ),'..','data','sample1.json')    
    with open(DICTIONARY_PATH1, "w") as write_file:
        for dict0 in sample1:
            json.dump(dict0, write_file)
            write_file.write('\n')

    # write sample 2
    sample2=[]
    sample2_subreddit=['AskReddit','memes','politics','nfl','nba','wallstreetbets','teenagers','PublicFreakout','leagueoflegends','unpopularopinion']
    for i in sample2_subreddit:
        data=requests.get(f'http://api.reddit.com/r/'+ i +'/new?limit=100',headers={'User-Agent':'windows:requests (by /u/winnie)'})
        content=data.json()['data']['children']
        for post in content:
            sample2.append(post)


    DICTIONARY_PATH2=os.path.join(os.path.dirname(__file__ ),'..','data','sample2.json')
    with open(DICTIONARY_PATH2, "w") as write_file:
        for dict0 in sample2:
            json.dump(dict0, write_file)
            write_file.write('\n')
    
    
    
    
if __name__ == "__main__":
    main()