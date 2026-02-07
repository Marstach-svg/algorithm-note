N = str(input())

result = set()
for char in N:
    result.add(char)

if len(result) == 1:
    print('Yes')
else:
    print('No')
