N = int(input())
A_list = list(map(int, input().split()))

len_A = len(A_list)
result = set()
num_set = set()

for num in A_list:
    num_set.add(num)

if len(num_set) == 1 and N % 2 != 0:
    print(max(num_set))

else:
    if len(num_set) == 1:
        result.add(max(num_set))

    if len(num_set) == 2 and min(num_set) * 2 == max(num_set):
            result.add(max(num_set))
    
    if N % 2 == 0:
        result_dict = {}
        for num in num_set:
            result_dict[num] = 0
        for num in A_list:
            result_dict[num] += 1
        if len(num_set) == 2:
            if result_dict[max(A_list)] ==  result_dict[min(A_list)]:
                sum_sort = max(A_list) + min(A_list)
                result.add(sum_sort)
        else:
            sum_sort = max(A_list) + min(A_list)
            result.add(sum_sort)

    print(*result)
