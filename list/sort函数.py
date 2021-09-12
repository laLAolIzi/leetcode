#list.sort( key=None, reverse=False)
def take2(li):
    return li[1]
random = [(2, 2), (3, 4), (4, 1), (1, 3)]
random.sort(key=take2)
print(random)