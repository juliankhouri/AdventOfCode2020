with open('D:/Advent2020/input.txt') as f:
    num = [int(i) for i in f]
print(len(num))
print(num)

def sum(l):

    for ki, i in enumerate(l):
        for kj, j in enumerate(l):
            for kk, k in enumerate(l):
                # To make sure we sum elements ONLY on different positions
                if kk != kj and kk != ki and kj != ki and i + j + k == 2020:
                    return l[ki]*l[kj]*l[kk]

    return 0

print(sum(num))