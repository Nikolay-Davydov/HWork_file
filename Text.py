import os
from operator import itemgetter


dist_file = {}
os.chdir('sort')
sort = os.listdir()


for name in sort:
    if name != 'result.txt':
        path = os.path.join(os.getcwd(), name)
        with open(path, 'r', encoding='utf-8') as file:
            text_all = file.read()
            size = len(text_all.splitlines())
        dist_file[name] = [size, text_all, name]


dist_file = sorted(dist_file.values(), key=itemgetter(0))

with open('result.txt', 'w', encoding='utf-8') as f:
    for result in dist_file:
      f.writelines([result[2], "\n", str(result[0]), "\n"])
      f.write(result[1])
      f.writelines("\n")