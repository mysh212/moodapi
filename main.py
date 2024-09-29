from core.general import *
import requests
from bs4 import BeautifulSoup as bs

url = 'https://moodle.ncku.edu.tw'
token = read_from_file('token.debug.tmp').strip()

def get_courses(token: str) -> list:
    html = requests.get(url, cookies = {'MoodleSession': token})
    write_to_file('homepage.html', html.text)

    soup = bs(html.text, 'html.parser')
    menu = soup.find('div', class_ = 'card-text content mt-3')

    #print(menu.find_all('ul')[0].get('class'))
    menu = [i for i in menu.find_all('ul') if 'unlist' not in i.get('class', [])]

    courses = [[[j.text, j.get('href', 'None')] for j in i.find_all('a')] for i in menu]
    for i in courses:
        for j in i:
            print(j)
        print('')

    return courses

def get_course_content(url: str):
    html = requests.get(url, cookies = {'MoodleSession': token})
    write_to_file('tmp.html', html.text)

    soup = bs(html.text, 'html.parser')
    pre = soup.find_all('div', class_ = 'content')
    
    # error([i.text for i in soup.find_all(class_ = 'assign')])
    # debug([len(pre)])

    ans = []

    for i in pre:
        try:
            title, url = (lambda x: [x.text, x.find('a').get('href', '')])(i.find('h3', class_ = 'sectionname'))
            host = (i.find_all('li'))[1:]
            debug((title, url))

            memo = i.find_all(dir = 'ltr')
            # error(memo)
            
            contents = [{'text': i.find('a').text, 'url': i.find('a').get('href',''), 'html': i, 'ishomework': 'assign' in i.get('class', [])} for i in host if i.find('a') is not None]

            contents += [{'text': i.text, 'url': '', 'html': i, 'ishomework': False} for i in memo]
            ans.append({'title': title, 'url': url, 'data': contents})
            # info(i.find_all('a'))
        except:
            pass
    return ans

def view_course_content(x):
    for i in x:
        warning([i['title'], i['url']])
        for j in i.get('data'):
            p = info
            if j['ishomework']: p = error
            p([j['text'], j['url']])

for i in get_courses(token)[0]:
    view_course_content(get_course_content(i[1]))
    input()
