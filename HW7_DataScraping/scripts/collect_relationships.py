import hashlib
import os
import os.path as osp
import json
import argparse
import requests
from bs4 import BeautifulSoup
#from loadData import load_file

def get_url_contents(cache,name,use_cache=True):
    url = 'http://www.whosdatedwho.com/dating/'+name
    fname=hashlib.sha1(url.encode('utf-8')).hexdigest()
    #full_path='/Users/winnietam/Desktop/HW7_260710889/cache/'+fname
    '''
    cache_dir=osp.join('scripts',cache_dir)
    full_path=osp.join(cache_dir,fname)
    if cache_path[0]=='~':
        cache_dir = osp.join(cache_path[0], cache_path[1])
        for i in range(2,len(cache_path)):
            cache_dir = osp.join(cache_dir, cache_path[i])
    else:
        cache_dir = osp.join(osp.dirname(__file__), cache_path[0], cache_path[1])
    '''
    cache_path = cache.split('/')
    cache_dir = osp.join(osp.dirname(__file__), cache_path[0])
    for i in range(1,len(cache_path)):
            cache_dir = osp.join(cache_dir, cache_path[i])
    if not osp.exists(cache_dir): 
        os.makedirs(cache_dir)
    
    full_path = osp.join(cache_dir, fname)
    
    
    if osp.exists(full_path) and use_cache is True:
        print('Loading from cache')
    else:
        print('Loading from source')
        r=requests.get(url)
        contents=r.text
        with open (full_path,'w') as fh:
            fh.write(contents)
    

    return full_path


def extract_relationships_from_candidate_links(candidate_links,name):
    person_url='/dating/'+name
    relationships=[]
    for link in candidate_links:
        if 'href' not in link.attrs:
            continue
        else:
            href=link['href']
            if href.startswith('/dating') and href != person_url:
                # href=/dating/susan-downey
                relationships.append(href[8:])
    return relationships




def extract_relationships(full_path,name):
    #name='robert-downey-jr'
    relationships=[]
    #url='http://www.whosdatedwho.com/dating/'+filename
    soup=BeautifulSoup(open(full_path,'r'), 'html.parser')

    #Current relationship
    status_h4=soup.find('h4','ff-auto-status')
    key_div=status_h4.next_sibling
    candidate_links=key_div.find_all('a')
    relationship=extract_relationships_from_candidate_links(candidate_links,name)
    relationships.extend(relationship)
    # at most one current relationship
    if len(relationships)>1:
        raise Exception ('Too many relationships - should have at most one')

    
    #Previous relationship 
    rels_h4= soup.find('h4','ff-auto-relationships')
    sib=rels_h4.next_sibling
    while sib is not None and sib.name=='p':
        candidate_links=sib.find_all('a')
        sib=sib.next_sibling
        relationships.extend(extract_relationships_from_candidate_links(candidate_links,name))
    return relationships




def load_file(input_file):
    '''
    tmp=[]
    with open(input_file) as file:
        for jsonObj in file:
            try:
                jdict=json.loads(jsonObj)
                tmp.append(jdict)
            except ValueError:
                continue
    '''
    tmp=[]
    try:
        file = open(input_file, "r").read()
        json_object = json.loads(file)
        tmp.append(json_object)
    except ValueError:
        print("error with loading json")

    return tmp

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('-c','--use_cache', action='store_true')
    parser.add_argument('input_file',help='Please tnter the input json file')
    parser.add_argument('-o', required=True, help = '-o The output json path and name', default = 'NA')
    args=parser.parse_args()

    input_file = args.input_file
    tmp=load_file(input_file)
    cache_dir=tmp[0].get('cache_dir')
    # Only 1 json
    name_list=tmp[0].get('target_people')
    dict={}
    for name in name_list:
        #url='http://www.whosdatedwho.com/dating/'+name
        full_path = get_url_contents(cache_dir,name)
        relationships=extract_relationships(full_path,name)
        dict[name]=relationships

    '''
    write dict into output json
    '''
    with open(args.o,"w") as write_file:
        json.dump(dict,write_file)
        # since there's only one 






    

if __name__ =='__main__':
    main()
