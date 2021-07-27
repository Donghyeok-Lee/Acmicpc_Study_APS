

# 25_Shortest_Path

## 목차

### [1. 1753. 최단경로](#1753.최단경로)



## [1753.최단경로](https://www.acmicpc.net/problem/1753)

### 오답 코드

```python
from typing import List, Tuple

def find_min(visited: List[bool], min_dis_list: List[int]) -> Tuple[int]:
    min_dis: int = 200000
    min_node: int = -1

    for i in range(V):
        if not visited[i] and min_dis > min_dis_list[i]:
            min_dis = min_dis_list[i]
            min_node = i

    return min_dis, min_node


def dijkstra() -> List[int]:
    min_dis_list: List[int] = [200000] * V
    min_dis_list[start_node - 1] = 0

    visited: List[bool] = [False] * V

    while True:
        min_dis, min_node = find_min(visited, min_dis_list)

        if min_dis == 200000:
            break

        visited[min_node] = True

        for i in range(V):
            if not visited[i] and min_dis_list[i] > min_dis_list[min_node] + edges[min_node][i]:
                min_dis_list[i] = min_dis_list[min_node] + edges[min_node][i]

    return min_dis_list


V, E = map(int, input().split())
start_node: int = int(input())

edges: List[List[int]] =[[200000] * V for _ in range(V)]

for _ in range(E):
    start, end, dis = map(int, input().split())
    edges[start-1][end-1] = dis

min_dis_list = dijkstra()

for i in range(V):
    print(min_dis_list[i] if min_dis_list[i] != 200000 else "INF")
```



### 주절주절

* 다익스트라를 오랜만에 해봤습니다. 맞을지는 모르겠네요. 왜냐면 오답 코드니까요!

    * 최솟값을 초기에 200000으로 설정한 건 정점이 최대 2만개 / 가중치가 최대 10이니까 단순하게 생각했습니다.

* 매 반복마다 최솟값과 노드를 찾는 과정을 넣어두니 코드가 너무 긴 것 같아서 따로 함수로 빼냈습니다.

* 아니 틀릴 리가 없다고 생각했는데... 문제 조건을 잘못 생각했네요...

    정점의 개수가 최대 2만개라는 건 인접 행렬 형태로 가중치를 저장하면 100% 터진다는 이야기였을 텐데...

    아직 공간 복잡도에 대해 깊게 생각하지 못 하는 것 같습니다.

* 인접리스트가 아니라 다른 방법으로 하는 건 시간이 늦은 관계로 내일 해볼 계획입니다.

* 요즘 잠을 잘 못자서 오늘도 회사에 지각을 했는데, 내일은 지각을 안 하길 기도해봅니다...

