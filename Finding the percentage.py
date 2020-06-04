n = int(input())
total = dict()
for i in range(0, n):
    tokens = input().split()
    name = tokens[0]
    total[name] = float(tokens[1]) + float(tokens[2]) + float(tokens[3])

student = input()
print ("{0:.2f}".format(total[student] / 3))
