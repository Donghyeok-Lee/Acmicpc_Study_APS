from typing import List

N: int = int(input())

wines: List[int] = [int(input()) for _ in range(N)]

dp: List[int] = [0] * N
dp[0] = wines[0]
if N >=2:
    dp[1] = wines[0] + wines[1]

    for i in range(2, N):
        dp[i] = max(dp[i-1], dp[i-3] + wines[i-1] + wines[i], dp[i-2] + wines[i])

print(dp[-1])