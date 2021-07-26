# 15_Dynamic_Programming_1

## 목차

### [1. 1018. 체스판 다시 칠하기](#1018. 체스판 다시 칠하기)





## [1018. 체스판 다시 칠하기](https://www.acmicpc.net/problem/1018)

### 풀이 코드

```python
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
```



### 주절주절

* 이전에 제출한 기록이 있는 문제 였습니다.

    이전] 메모리 : 123424 KB / 시간 : 200ms

    현재] 메모리 :   33904 KB / 시간 : 180ms

    * 이번에는 예전보다 뭔가 좀 발전한 것 같습니다. 칭찬합시다.

    * 근데 지금보니 이전 코드를 Pypy3로 제출했었네요.

        다시 Python3로 제출해보니 오히려 메모리, 시간이 현재보다 적어졌습니다. 칭찬은 취소입니다.

* 체스판을 실제로 바꾸지는 않을 거라서 그냥 문자열 List로 만들었습니다.

* min_val은 최악의 경우라도 64는 넘지 않을 거라고 생각했습니다.

    (사실 32인 것 같은데... 뭐 상관없죠!)

* 각 위치에서 오른쪽으로 8칸 / 아래로 8칸을 칠하는 최소 갯수를 카운트했습니다.

* 정말 무식하게 풀었지만 .... 뭐 시간도 넉넉하고 메모리도 충분하네요.

* 지금 상태 혹은 함수를 검은색 / 흰색으로 나누어서 백트래킹을 한다면 좀 더 좋은 효과를 볼 수 있을까요?

    * 닭 잡는데는 닭 잡는 칼을 쓰는 겁니다. 이런데에 쓸 체력이 없는게 아쉽군요...

