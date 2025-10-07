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
    n, p = rm()
    p = p/100
    res = ((p ** ((n - 1)/n)) - p) * 100
    print(f"Case #{case}: {res}")

def run():
    cases = ri()
    for case in range(1, cases + 1):
        solve(case)

if __name__ == "__main__":
    run()
