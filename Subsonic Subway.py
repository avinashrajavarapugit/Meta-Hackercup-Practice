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
    n = ri()
    prevmx = float('inf')
    prevmn = float('-inf')
    flag = True
    for i in range(1, n + 1):
        a, b = rm()
        mx = float('inf') if a == 0 else i / a
        mn = i / b
        prevmn = max(prevmn, mn)
        prevmx = min(prevmx, mx)
        if prevmx < prevmn:
            flag = False
    if flag:
        print(f"Case #{case}: {prevmn}")
    else:
        print(f"Case #{case}: {-1}")


def run():
    cases = ri()
    for case in range(1, cases + 1):
        solve(case)

if __name__ == "__main__":
    # Redirect input from input.txt and output to output.txt
    # with open("input.txt", "r") as infile:
    #     sys.stdin = infile
    #     with open("output.txt", "w") as outfile:
    #         sys.stdout = outfile
    #         run()
    run()
