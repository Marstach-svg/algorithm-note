# atcoder 391 B
# ギブアップ
# a, bの値を固定して下で調べていくイメージ
N, M = map(int, input().split())
S = [input() for _ in range(N)]
T = [input() for _ in range(M)]

for a in range(N-M+1):
    for b in range(N-M+1):
        ok = True
        for i in range(M):
            for j in range(M):
                if S[a + i][b + j] != T[i][j]:
                    ok = False

        if ok:
            print(a+1, b+1)