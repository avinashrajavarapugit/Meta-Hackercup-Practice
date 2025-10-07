# src: Hi, I'm Avinash Rajavarapu

import sys
from collections import defaultdict, deque, Counter
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop
from math import gcd, sqrt, ceil, floor, inf
from functools import lru_cache

def ri(): return int(input())
def rl(): return list(map(int, input().split()))
def rs(): return input().strip()
def rm(): return map(int, input().split())

def solve(case):
    n, k = rm()
    mn1 = float('inf')
    mn2 = float('inf')
    for _ in range(n):
        a = ri()
        if a < mn1:
            mn2 = mn1
            mn1 = a
        elif a < mn2:
            mn2 = a
    
    rem = n - 1
    if n == 1:
        req = mn1
    else:
        req = mn1 * (2 * n - 3)
    print(f"Case #{case}: {'YES' if req <= k else 'NO'}")

def run():
    cases = ri()
    for case in range(1, cases + 1):
        solve(case)

if __name__ == "__main__":
    run()
