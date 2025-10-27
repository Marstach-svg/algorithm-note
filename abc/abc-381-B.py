# Atcoder Beginner Contest 381 B
# 同じkeyだと値が更新されてしまうdictの性質をつかった。
T = input()

def String_1122(T):
    len_T = len(T)
    dict = {}
    if len_T % 2 != 0:
        return 'No'
    for i in range(1, (len_T) // 2 + 1):
        if T[i*2-2] == T[i*2-1]:
            dict[T[i*2-2]] = T[i*2-1]
    if len(dict) == len_T // 2:
        return 'Yes'
    else:
        return 'No'


if __name__ == '__main__':
    print(String_1122(T))