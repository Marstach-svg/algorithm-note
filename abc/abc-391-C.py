# atcoder 391 C
# 以下のコードは時間制限　->　最初は全部の巣に1ずつだから操作した巣の鳩の数が1から2になったときにresultを+=1すればいい。
# 逆に2から1になったときにresultを-=1すればいい。2以上に増えた場合は複数の巣ということで全部同じ扱い。
N, Q = map(int, input().split())
queries = [input() for _ in range(Q)]
dict = {}

for i in range(1, N+1):
    dict[i] = [i]

for query in queries:
    query = list(map(int, query.split(' ')))
    if query[0] == 2:
        result = 0
        for i in range(1, N+1):
            if len(dict[i]) >= 2:
                result += 1
        print(result)
    else:
        P = query[1]
        H = query[2]

        for i in range(1, N+1):
            if i == H:
                continue
            for j in dict[i]:
                if j == P:
                    dict[i].remove(j)
                    dict[H].append(P)