import re
texts = [
   "Hello, World!",
   "The world is mine",
   "Hello, how are you?"
]
wordStats = {}
line = 0
for i in texts:
    for j in re.split('\W+',i.lower()):
        if(j == ''):
            continue
        elif(j not in  wordStats):
            wordStats[j] = {'word number': 1,'line number': line}
        else:
            wordStats[j]['word number'] = wordStats[j]['word number']+1
    line += 1

print('{0:10}{1:10}{2:10}'.format('word','count', 'first line'))
for i in wordStats:
    print('{0:10}{1}{2:10d}'.format(i, wordStats[i]['word number'], wordStats[i]['line number']))

    