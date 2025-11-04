# N*Nの値からM*Mを取り出すときのパターン数を導き出す問題
# [[1, 1, 1], [2, 2, 2]]みたいにしてgrid_list[0][1]でアクセスして全探索しようとした
# 以下の答えでは文字列のままあつかって、sliceで切り出してsetに保存。setは同じ値は上書きされるので勝手に重複排除
# 最後にsetの長さを調べるだけでパターン数がわかる

N,M=map(int,input().split())
S=[input() for _ in range(N)]
grid_set=set()
for i in range(N-M+1):
  for j in range(N-M+1):
    grid = tuple(S[ii][j:j+M] for ii in range(i,i+M))
    grid_set.add(grid)
print(len(grid_set))