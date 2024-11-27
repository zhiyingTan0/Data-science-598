import json
import argparse
import requests

def collect_post(name):
    n = 100
    sample = []
    #name='/r/politics'
    data = requests.get(f'http://api.reddit.com{name}/hot?limit={n}', headers={'User-Agent':'windows:requests (by /u/winnie)'}) 
    content=data.json()['data']['children']
    for post in content:
        if post['data']['stickied']:
            continue
        else:
            sample.append(post)

    for i in range(4):
        after=sample[len(sample)-1]['data']['name']
        data = requests.get(f'http://api.reddit.com{name}/hot?limit={n}&after={after}', headers={'User-Agent':'windows:requests (by /u/winnie)'})
        content=data.json()['data']['children']
        for post in content:
            if post['data']['stickied']:
                continue
            else:
                sample.append(post)

    return sample


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('-o',required=True,help='-i The output json file path and name',default='NA' )
    parser.add_argument('name',help='The <subreddit> is required',default='NA')
    args=parser.parse_args()
    path=args.o
    name=args.name
    
    #call collecting function
    sample=collect_post(name)
    with open(path, "w") as write_file:
        for dict0 in sample:
            json.dump(dict0, write_file)
            write_file.write('\n')
    








if __name__ == "__main__":
    main()
