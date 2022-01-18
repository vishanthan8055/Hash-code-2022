out = []
like_lst =[]
dislike_lst =[]
items = []
lc = {}
dc = {}
result = []
with open('input.txt') as f:
    lines = f.readlines()
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

def remove_nested(lst):
    return [val for sublist in lst for val in sublist]
like_lst = remove_nested(like_lst)
dislike_lst = remove_nested(dislike_lst)
def remove_int(lst):
    no_int = [y for y in lst if not (y.isdigit() or y[0] == '-' and y[1:].isdigit())]
    return no_int
like_lst = remove_int(like_lst)
dislike_lst = remove_int(dislike_lst)
def count_items(lst,d):
    for i in items:
        count = lst.count(i)
        d[i] = count
    return d
lc = count_items(like_lst,lc)
dc = count_items(dislike_lst,dc)

for i in items:
    if lc[i] >= dc[i]:
        result.append(i)
print(result)
with open('output.txt','w') as f:
    f.write(str(len(result)) + ' ')
    for i in result:
        f.write(i + " ")
print(len(result))