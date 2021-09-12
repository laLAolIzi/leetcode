def suqare(a):

    for i in range(a):
        yield i*i

s=suqare(1000000)
for _ in range(10):
    print(next(s))

