# 1676 : 팩토리얼 0의 개수
N = int(input())
fact = 1

for i in range(2, N + 1):
    fact *= i

fact = str(fact)
result = 0

for i in range(1, len(fact)):
    if fact[-i] == '0':
        result += 1
    else:
        break

print(result)