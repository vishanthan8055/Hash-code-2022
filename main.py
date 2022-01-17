n = int(input())
like_lst =[]
dislike_lst =[]
items = []
for i in range(n):
    like_lst.append(input().split())
    dislike_lst.append(input().split())
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
print(items)