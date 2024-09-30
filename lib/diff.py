from core.general import *

def diff(old, new):
    for i in new:
        if i not in old:
            new_course(new[i]['title'], new[i]['url'], i)
    
    for course in new:
        if course not in old: continue;
        l, r = old.get(course), new.get(course)
        for category in r['data']:
            if category['url'] not in [i['url'] for i in l['data']]:
                new_category(category['title'], category['url'], category)
            left = l['data'][[i['url'] for i in l['data']].index(category['url'])]['data']
            right = category['data']
            for k in right:
                # if left['text'] != right['text']:
                if k['url'] == '':
                    if k['text'] not in [i['text'] for i in left]:
                        # info('ok')
                        new_text(k)
                    continue
                if k['url'] not in [i['url'] for i in left]:
                    new_text(k)
                    continue
                ll = left[[i['url'] for i in left].index(k['url'])]
                rr = k
                if not ll['text'] == rr['text']: debug([ll, rr]);
                if ll['text'] != rr['text']:
                    text_modify(ll, rr)
                    
                # debug([left, right])
                # assert(left == right)

def new_text(x):
    info([x['text'], x['url']], ['New Text'])
    return

def text_modify(l, r):
    # l, r: ['text','url','ishomework']
    old, new = l.get('text'), r.get('text')
    print(old, new)

def new_course(title, url, id):
    info([title, url, id], ['New Course'])
    return

def new_category(title, url, refer):
    info([title, url, id], ['New Category'])
    return

def main(old, new):
    return diff(old, new)