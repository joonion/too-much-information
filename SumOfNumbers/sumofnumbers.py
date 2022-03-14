# N부터 M까지 모든 자연수의 합을 구하라.

from re import I


def sum0(N, M):
    S = sum(range(N, M+1))
    return S

def sum1(N, M):
    if N == M:
        return N
    else:
        return sum1(N, M - 1) + M

def sum2(N, M, S):
    if N == M:
        return S + N
    else:
        return sum2(N+1, M, S + N)

def sum3(N, M):
    if N == M:
        return N
    else:
        mid = (N + M) // 2
        return sum3(N, mid) + sum3(mid + 1, M)

def sum4(N, M):
    S = 0
    for i in range(M, N - 1, -1):
        S += i
    return S

def sum5(N, M):
    return (M*(M+1) - N*(N-1)) // 2

N, M = list(map(int, input().split()))
S = sum5(N, M)
print(S)

