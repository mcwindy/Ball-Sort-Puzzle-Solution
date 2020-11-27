def forward(s):
    # move i_th tube top to j_th tube top
    # print('s:')
    # for i in s:
    #     print(i)
    # print()
    future = []
    for i in range(tubeNum):
        if len(s[i]) > 0:
            for j in range(tubeNum):
                if i != j and ((len(s[j]) == 0 or (len(s[j]) < 4) and s[i][-1] == s[j][-1])):
                    tmp1 = [[__ for __ in _] for _ in s]
                    tmp1[j].append(tmp1[i][-1])
                    tmp1[i].pop()
                    tmp2 = [[__ for __ in _] for _ in tmp1]
                    tmp1.sort(key=lambda x: tubeNum if len(x) == 0 else x[0])
                    if str(tmp1) not in sett:
                        future.append(tmp2)  # tmp1
                        statements.append('move ' + str(i + 1) + ' to ' + str(j + 1))
                        sett.add(str(tmp1))
    # for i in future:
    #     for j in i:
    #         print(j)
    #     print()
    # print()
    return future


def checkfin(s):
    for i in s:
        if 0 < len(i) < 4 or (len(i) == 4 and not (i[0] == i[1] == i[2] == i[3])):
            return False
    return True


tubeNum = int(input())
tube = []
# from bottom to top
for i in range(tubeNum - 2):
    tube.append(list(map(int, input().split())))
dic = {i: 0 for i in range(1, tubeNum - 1)}
for i in tube:
    for j in i:
        dic[j] += 1
for i in dic:
    if dic[i] != 4:
        print('error on number of', i)
tube.extend([[], []])
print('tube:', tube)


cur = 0
state = [tube]
fromlist = [0]
statements = ['']
sett = set(str(tube))
while not checkfin(state[cur]):
    if not cur % 10000:
        print(cur)
    tmp1 = forward(state[cur])
    state.extend(tmp1)
    fromlist.extend([cur] * len(tmp1))
    cur += 1


print('fin:', checkfin(state[cur]))
print(cur, len(state))
tmp = []
statement = []
while cur != 0:
    tmp.append(state[cur])
    statement.append(statements[cur])
    cur = fromlist[cur]
tmp.append(tube)
statement.append('initial:')
tmp, statement = tmp[::-1], statement[::-1]
for i, k in enumerate(tmp):
    print(str(i) + ' step:')
    print(statement[i])
    for j in k:
        print(j)
    print()


# 5
# 1 2 3 3
# 1 2 1 2
# 3 1 2 3

# level 23
# normal sort     746294 1015540
# +len sort       909408 960816
# -len sort       904565 957039
# tmp2=tmp1 sort  21286 21552
# current sort    28609 29223
# 9
# 1 2 3 4
# 3 2 5 6
# 4 7 4 6
# 3 1 5 6
# 3 7 2 6
# 7 1 1 2
# 5 5 4 7

# level 58
# 11
# 1 2 2 3
# 4 5 3 6
# 7 8 4 6
# 8 5 4 5
# 7 2 9 1
# 7 9 1 3
# 9 2 6 6
# 3 4 5 9
# 7 1 8 8

# level 107
# tmp2=tmp1 sort  58422 60882
# current sort    91585 98176
# 14
# 1 2 3 4
# 5 6 7 8
# 7 4 9 6
# 10 8 9 1
# 7 10 11 6
# 1 7 3 6
# 12 5 3 2
# 9 5 12 8
# 4 5 11 11
# 2 9 10 12
# 2 1 4 3
# 11 12 10 8
