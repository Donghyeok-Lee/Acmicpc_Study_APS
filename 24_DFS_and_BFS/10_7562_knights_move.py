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