from typing import List, Tuple, Dict

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
            if (not visited[i]) and (i+1 in edges.get(min_node+1, [])):
                if min_dis_list[i] > min_dis_list[min_node] + edges[min_node+1][i+1]:
                    min_dis_list[i] = min_dis_list[min_node] + edges[min_node+1][i+1]

    return min_dis_list


V, E = map(int, input().split())
start_node: int = int(input())

edges: Dict[Dict[int]] = dict()

for _ in range(E):
    start, end, dis = map(int, input().split())
    if start not in edges:
        edges[start] = dict()
    edges[start][end] = dis

min_dis_list = dijkstra()

for i in range(V):
    print(min_dis_list[i] if min_dis_list[i] != 200000 else "INF")