

# 24_DFS_AND_BFS

## 목차

### [1. 7562. 나이트의 이동](#7562.나이트의이동)

### [2. 2667. 단지 번호 붙이기](#2667.단지번호붙이기)



## [7562.나이트의이동](https://www.acmicpc.net/problem/7562)

### 풀이 코드

```python
from collections import deque
from typing import List


def bfs(i: int, j: int) -> int:
    queue: deque = deque([[i, j, 0]])
    while queue:
        cur_data: List[int] = queue.popleft()
        cur_i = cur_data[0]
        cur_j = cur_data[1]
        cur_cnt = cur_data[2]

        if (cur_i == end_i) and (cur_j == end_j):
            return cur_cnt

        for k in range(8):
            next_i: int = cur_i + dirs[k][0]
            next_j: int = cur_j + dirs[k][1]
            if (0 <= next_i< l) and (0 <= next_j < l) and not visited[next_i][next_j]:
                visited[next_i][next_j] = True
                queue.append([next_i, next_j, cur_cnt+1])
    return -1


T: int = int(input())

for t in range(T):
    l: int = int(input())
    start: List[int] = list(map(int, input().split()))
    start_i: int = start[0]
    start_j: int = start[1]

    end: List[int] = list(map(int, input().split()))
    end_i: int = end[0]
    end_j: int = end[1]

    dirs: List[List[int]] = [[2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1]]

    visited: List[List[bool]] = [[False] * l for _ in range(l)]
    visited[start_i][start_j] = True

    result:int = bfs(start_i, start_j)

    print(result)
```



### 주절주절

* 기본적으로 BFS 알고리즘을 사용했습니다.

* 그냥 지금까지 위치와 이동 횟수를 저장하면서 도착점에 도착하는 순간 현재까지 이동 횟수를 return하게 했습니다.

* 최근 자바를 자주 보다 보니 파이썬의 type hint 기능을 너무 사용해보고 싶었습니다.

    근데 자세히 알지 못하고 되는대로 쓰다 보니 정말 비효율적이게 되었습니다.

    예를 들어, 아래 코드에서는 쓸데없이 더 많은 메모리를 쓰게 되었습니다. 

    ```python
    start: List[int] = list(map(int, input().split()))
    start_i: int = start[0]
    start_j: int = start[1]
    ```

    효율성을 버리지 않으면서 가독성을 챙기는 방향으로 더 발전시켜야겠습니다.

    

* 처음에는 정말 아무것도 기억 안 나서 한번 방문했던 곳을 여러 번 반복하게 했더니

    정말 많은... 시간이 걸렸던 것 같습니다. 그래도 빠르게 기억해낸 저 자신에게 칭찬을 한번 해주었습니다.






## [2667.단지번호붙이기](https://www.acmicpc.net/problem/2667)

### 풀이 코드

```python
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
```



### 주절주절

* 문제를 읽고, DFS로 풀까 BFS로 풀까 고민했습니다.

    그런데, 문제 조건에서 N은 25이하의 자연수라고 나와서 최악의 경우 약 625번 재귀 호출하게 될 거고..

    괜찮겠다! 라고 생각해서 충동적으로 DFS로 풀었습니다.

    사실 뭐.. 이전에 BFS로 풀었으니 이번엔 재귀를 이용한 DFS도 해보고 싶었어요.

* 기록을 보니 예전에는 반복문을 이용한 DFS로 헀었네요...

    그 외에는 정말 놀랍게도 하나도 변하지 않았습니다.

    ```python
    def dfs(cur_x, cur_y):
        stack = [[cur_x, cur_y]]
        temp_total = 0
        num_list[cur_x][cur_y] = 0
    
        while stack:
            temp_total += 1
            cur_x, cur_y = stack.pop()
            for i in range(4):
                temp_x = cur_x + dir_list[i][0]
                temp_y = cur_y + dir_list[i][1]
                if 0 <= temp_x < N and 0 <= temp_y < N and num_list[temp_x][temp_y] == 1:
                    stack.append((temp_x, temp_y))
                    num_list[temp_x][temp_y] = 0
    
        return temp_total
    
    
    N = int(input())
    num_list = [list(map(int, list(input()))) for _ in range(N)]
    dir_list = ((1, 0), (0, 1), (-1, 0), (0, -1))
    total = []
    for i in range(N):
        for j in range(N):
            if num_list[i][j]:
                temp_total = dfs(i, j)
                total.append(temp_total)
    
    total.sort()
    length = len(total)
    
    print(length)
    for i in range(length):
        print(total[i])
    ```

* 그런데 저는 왜 굳이 result에 초기값 0을 넣어놓고 나중에 제외시켰을까요?

    아마도 단지 번호랑 단지 수를 일치시키려고 한 것 같은데... 문제를 안 읽고 문제를 풀면 이렇게 됩니다.