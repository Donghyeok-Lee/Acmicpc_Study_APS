from typing import List, Tuple

def dfs(i, j):
    global number
    apartments[i][j] = "0"
    
    for k in range(4):
        next_i: int = i + dirs[k][0]
        next_j: int = j + dirs[k][1]
        if (0 <= next_i < N) and (0 <= next_j < N) and apartments[next_i][next_j] == "1":
            number += 1
            dfs(next_i, next_j)


N: int = int(input())
apartments: List[str] = [list(input()) for _ in range(N)]

dirs: Tuple[Tuple[int]] = ((0, 1), (1, 0), (0, -1), (-1, 0))
result: List[int] = [0] # 각 단지의 수를 저장하기 위한 List 입니다.

for i in range(N):
    for j in range(N):
        if apartments[i][j] != "0":
            number: int = 1
            dfs(i, j)
            result.append(number)

result = sorted(result[1:])

print(len(result))
for i in range(len(result)):
    print(result[i])