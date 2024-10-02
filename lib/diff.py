from core.general import *

def diff(old, new):
    ans = []
    def new_text(x, category, course):
        category_name, category_url = category
        course_name, course_url = course

        info([x['text'], x['url']], ['New Text'])
        ans.append({'operate': 'New Text', 'title': x['text'], 'url': x['url'], 'category': {'title': category_name, 'url': category_url}, 'course': {'title': course_name, 'url': course_url}})
        return

    def text_modify(l, r, category, course):
        category_name, category_url = category
        course_name, course_url = course

        # l, r: ['text','url','ishomework']
        old, new = l.get('text'), r.get('text')
        ans.append({'operate': 'Text Modify', 'title': r['text'], 'url': r['url'], 'ishomework': r['ishomework'], 'old': {'title': l['text'], 'url': l['url']}, 'category': {'title': category_name, 'url': category_url}, 'course': {'title': course_name, 'url': course_url}})
        print(old, new)

    def new_course(title, url, id):
        info([title, url, id], ['New Course'])
        ans.append({'operate': 'New Course', 'title': title, 'url': url, 'id': id})
        return

    def new_category(title, url, course):
        course_name, course_url = course
        info([title, url, id], ['New Category'])
        ans.append({'operate': 'New Category', 'title': title, 'url': url, 'course': {'title': course_name, 'url': course_url}})
        return
    

    for i in new:
        if i not in old:
            new_course(new[i]['title'], new[i]['url'], i)
    
    for course in new:
        if course not in old: continue;
        l, r = old.get(course), new.get(course)
        for category in r['data']:
            if category['url'] not in [i['url'] for i in l['data']]:
                new_category(category['title'], category['url'], [r['title'], r['url']])
                continue
            left = l['data'][[i['url'] for i in l['data']].index(category['url'])]['data']
            right = category['data']
            for k in right:
                # if left['text'] != right['text']:
                if k['url'] == '':
                    if k['text'] not in [i['text'] for i in left]:
                        # info('ok')
                        new_text(k, [category['title'], category['url']], [r['title'], r['url']])
                    continue
                if k['url'] not in [i['url'] for i in left]:
                    new_text(k, [category['title'], category['url']], [r['title'], r['url']])
                    continue
                ll = left[[i['url'] for i in left].index(k['url'])]
                rr = k
                # if not ll['text'] == rr['text']: debug([ll, rr]);
                if ll['text'] != rr['text']:
                    text_modify(ll, rr, [category['title'], category['url']], [r['title'], r['url']])
                    
                # debug([left, right])
                # assert(left == right)
    return ans


def main(old, new):
    return diff(old, new)