#自分の回答
S = input()

result_list = []
for s in S:
  if s != ".":
    result_list.append(s)

result = "".join(result_list)

print(result)

#解説の回答
S = input()
T = ""
for c in S:
  if c != '.':
    T += c
print(T)