from core.general import *
import json

def save(x):
    x = clean(x)

    write_to_file('last.json', json.dumps(x))
    return

    info([i['title'], i['url'], i['id']])
    for k in i['data']:
        warning((k['title'], k['url']))
        for j in k['data']:
            info([j['text'], j['ishomework']])
            # debug(j.keys())

def clean(x):
    for i in x:
        for j in i['data']:
            for k in j['data']:
                if 'html' in k:
                    del k['html']
    return x

def translate(x):
    x = clean(x)
    ans = {}
    for i in x:
        ans[i['id']] = i
    return ans

def get():
    return json.loads(read_from_file('last.json'))