'''
Created on May 8, 2018

@author: mkhan
'''


mylist = ['cat', 'dog', 'horse', 'cow', 'cat', 'cat', 10, 'dog', 20, 'lion', 10]

d = {}

for item in mylist:
    
    if(item) in d:
        d[item] += 1
    else:
        d[item] = 1
    
print(d)


people = []
jack = {}
jack['name'] = 'jack sparrow'
jack['age'] = 12
jack['height'] = 52
sally = {}
sally['name'] = 'sally hemmings'
sally['age'] = 8
sally['height'] = 48

anotherdudette = {}
anotherdudette['name'] = 'tommy sally'
anotherdudette['age'] = 77
anotherdudette['height'] = 61

people.append(jack)
people.append(sally)
people.append(anotherdudette)
print(people)

for person in people:
        if 'sally' in person['name']:
            person['age'] +=1
        
print(people)