from random import randint

def newcounter(lst, x):
    return sum([1 for t in lst if t == x])

word = lambda x: 'рази' if x % 10 in (2, 3, 4) else 'раз' if x in (1, ) else 'разів'

numlist = []
for _ in range(200):
    numlist.append(randint(1, 10))

numdict = {x: newcounter(numlist, x) for x in set(numlist)}
for el, cnt in numdict.items():
    print(f"Число {el} зустрічається у первісному списку {cnt} {word(cnt)}")