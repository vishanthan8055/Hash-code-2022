
like_lst =[]
dislike_lst =[]
items = []
lc = {}
dc = {}
with open('input.txt') as f:
    lines = f.readlines()
out = []
for i in range(len(lines)):
    out.append(lines[i].rstrip('\n').split(' '))
n = out.pop(0)
for i in range(len(out)):
    if i%2 == 0:
        like_lst.append(out[i])
    else:
        dislike_lst.append(out[i])
def get_items(like_lst,dislike_lst):
    items = []
    for i in like_lst:
        for j in i:
            if j.isdigit() != True:
                items.append(j)
    items = list(set(items))
    for i in dislike_lst:
        for j in i:
            if j.isdigit() != True:
                items.append(j)
    items = list(set(items))
    return list(set(items))
items = get_items(like_lst,dislike_lst)
# print(like_lst)
# print(dislike_lst)
def majority(like_lst,items,lc):
    for i in items:
        sum = 0
        for j in like_lst:
            if j.count(i) > 0:
                sum = j.count(i)
        lc[i] = sum
    return lc
lc = majority(like_lst,items,lc)
dc = majority(dislike_lst,items,dc)
print(lc)
print(dc)
'''
for i in items:
    for j in  like_lst:
        for k in j:
            if k == i:
'''