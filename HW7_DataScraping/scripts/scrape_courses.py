from bs4 import BeautifulSoup
import requests
import requests.auth
import hashlib
import csv
import io
import os.path as osp
import argparse  
import json 




def get_url_content(cache,page, use_cache = True):
    url = 'https://www.mcgill.ca/study/2020-2021/courses/search?page='+page 
    fname = hashlib.sha1(url.encode('utf-8')).hexdigest()

    cache_path = cache.split('/')
    cache_dir = osp.join(osp.dirname(__file__), cache_path[0])
    for i in range(1,len(cache_path)):
            cache_dir = osp.join(cache_dir, cache_path[i])

    if not osp.exists(cache_dir): 
        os.makedirs(cache_dir)
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

    full_path = osp.join(cache_dir, fname)
    if osp.exists(full_path) and use_cache: 
        print('Loading from cache') 
        contents = open(full_path, 'r',encoding='utf8').read()
    else: 
        print('Loading from source')
        r = requests.get(url)
        contents = r.text 
        with open(full_path, 'w',encoding='utf8') as file: 
            file.write(contents)

    return full_path

def extract_courses(path):
    courses = []
    soup = BeautifulSoup(open(path, 'r',encoding='utf8'), 'html.parser')
    contents = soup.find('div', {"id" :"main-column"})
    course_titles = contents.find_all('h4', 'field-content')

    for course in course_titles: 
        courses.append(course.text)

    return courses


def course_split(courses):

    course_list = []
    for course in courses: 
        tmp = []
        # split the course by spaces
        pointer = course.split(" ")
        # handle the special cases
        if pointer[len(pointer)-1] != "credits)":
            continue 

        tmp.append(pointer[0] + " " + pointer[1])
        course_name = ""
        for i in range(2, len(pointer)-3):
            course_name = course_name + pointer[i] + " "
        course_name = course_name + pointer[len(pointer)-3]
        course_name = course_name.replace("\n", "")
        
        tmp.append(course_name)
        tmp.append(pointer[len(pointer)-2].split("(")[1])
        course_list.append(tmp)

    return course_list 


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-c','--use_cache', action='store_true')
    parser.add_argument('cache',help='Please enter the cache path')
    parser.add_argument('page', help = 'Please enter the page number')
    args = parser.parse_args()
    cache = args.cache
    page=args.page


    path = get_url_content(cache, page, args.use_cache)
    courses = extract_courses(path)
    course_list = course_split(courses)

    title = ["CourseID","Course Name","# of credits"]
    # write the list in the form of csv file
    s = io.StringIO()
    csv_course_list = csv.writer(s)
    csv_course_list.writerow(title)

    for course in course_list: 
        csv_course_list.writerow(course)
    
    print(s.getvalue())



if __name__ =='__main__':
    main()
