score = {'ss': 100, 'cc': 99, 'kk': 101}
dict = sorted(score.items(), key=lambda d: d[1], reverse=True)
for i in range(len(dict)):
    print(dict[i][0])
    print(dict[i][1])