
total = 0
for i in range(5):
    L = [j ^ (j >> i) for j in range(10000)]
    total += sum(L)
    del L # remove reference to L
