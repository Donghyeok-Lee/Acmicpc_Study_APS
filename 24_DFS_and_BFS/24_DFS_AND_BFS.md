# [7562. 나이트의 이동](https://www.acmicpc.net/problem/7562)



## 풀이 코드

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



## 주절주절

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

    

    