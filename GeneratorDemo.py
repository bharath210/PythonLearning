def top_ten():
    n = 1
    while n <= 10:
        sq = n * n
        yield sq
        n += 1


val = top_ten()

for i in val:
    print(i)
