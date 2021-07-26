from typing import List

def calc_min_val(n: int, m: int) -> int:
    white_cnt: int = 0
    black_cnt: int = 0

    for i in range(n, n+8):
        for j in range(m, m+8):
            if ((i+j) % 2 == 0):
                if boards[i][j] == "B":
                    white_cnt += 1
                else:
                    black_cnt += 1
            else:
                if boards[i][j] == "W":
                    white_cnt += 1
                else:
                    black_cnt += 1
    return min(white_cnt, black_cnt)


N, M = map(int, input().split())
boards: List[str] = [input() for _ in range(N)]

min_val: int = 64

for i in range(N-8+1):
    for j in range(M-8+1):
        cur_min_val: int = calc_min_val(i, j)
        if min_val > cur_min_val:
            min_val = cur_min_val

print(min_val)