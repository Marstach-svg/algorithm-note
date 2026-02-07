N, K= map(int, input().split())

count = 0
for num in range(1, N+1):
    str_num = str(num)
    result = 0
    for char in str_num:
        result += int(char)
    if K == result:
        count += 1

print(count)