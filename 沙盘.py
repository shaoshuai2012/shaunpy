score = {'ss': 100, 'cc': 99, 'kk': 101}
paihang = sorted(score.items(), key=lambda d: d[1], reverse=True)
chengji = ''
for i in range(len(paihang)):
    chengji = chengji + '第' + str(i+1) + '名：' + '姓名：' + paihang[i][0] + '  成绩：' + str(paihang[i][1]) + '分\n'
print(chengji)
