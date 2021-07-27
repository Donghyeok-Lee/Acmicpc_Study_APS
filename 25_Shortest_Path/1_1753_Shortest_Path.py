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