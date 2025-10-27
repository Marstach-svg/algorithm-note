# AtCoder Begginer Contest 390 B
N = int(input())
A = list(map(int, input().split(' ')))

def geometric_progression(N, A):
    if len(A) <= 1:
        return 'No'
    ratio = A[1] / A[0]
    for i in range(0, N-1):
        if A[i] * ratio != A[i+1]:
            return 'No'
    return 'Yes'

if __name__ == '__main__':
    print(geometric_progression(N, A))


N = int(input())
A = list(map(int, input().split()))

# 丸め誤差（浮動小数点のせいでratioが丸められ、誤差が生じて、after contestで失敗)
ratio = A[1] / A[0]
for i in range(0, N-1):
    if A[i] * ratio != A[i+1]:
        print('No')
        break
else:
  print('Yes')

以下が正しいコード
for i in range(N-2):
    if A[i] * A[i+2] != A[i+1] * A[i+1]:
        print('No')
        break
else:
    print('Yes')
