from core.general import *
from lib.moodle import get_all_contents
from lib.diff import main
import lib.io
import json

f = get_all_contents()
lib.io.save(f)

# for i in f:
#     info([i['title'], i['url'], i['id']])
#     for k in i['data']:
#         warning((k['title'], k['url']))
#         for j in k['data']:
#             info([j['text'], j['ishomework']])
#             # debug(j.keys())
#     input()

lib.diff.main(lib.io.translate(json.loads(read_from_file('last.json.bkp'))), lib.io.translate(lib.io.get()))