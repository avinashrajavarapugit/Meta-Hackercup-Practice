# src: Hi, I'm Avinash Rajavarapu

import sys
from collections import defaultdict, deque, Counter
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop
from math import gcd, sqrt, ceil, floor, inf
from functools import lru_cache, cache

def ri(): return int(input())
def rl(): return list(map(int, input().split()))
def rs(): return input().strip()
def rm(): return map(int, input().split())

@cache
def isprime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def sieve(N):
    is_prime = [True] * (N + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(N ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, N + 1, i):
                is_prime[j] = False
    return is_prime

def precompute(N):
    is_prime = sieve(N)
    twin = [0] * (N + 1)
    for i in range(3, N - 1):
        if is_prime[i] and is_prime[i + 2]:
            twin[i] = 1
    prefix = [0] * (N + 1)
    for i in range(1, N + 1):
        prefix[i] = prefix[i-1] + twin[i]
    return prefix

def solve(case, N, prefix):
    if N < 5:
        print(f"Case #{case}: 0")
        return
    res = prefix[N - 2] + 1
    print(f"Case #{case}: {res}")

def run():
    cases = ri()
    Ns = [ri() for _ in range(cases)]
    maxN = max(Ns)
    prefix = precompute(maxN)
    for idx, N in enumerate(Ns, 1):
        solve(idx, N, prefix)

if __name__ == "__main__":
    with open("input.txt", "r") as infile:
        sys.stdin = infile
        with open("output.txt", "w") as outfile:
            sys.stdout = outfile
            run()