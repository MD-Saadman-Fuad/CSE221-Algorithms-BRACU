# -*- coding: utf-8 -*-
"""Lab 4 Task 4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xuJr_PW0-oaSVu9FDabA6lFpemCmgq1m
"""

txt_input=open("/content/input4.txt", "r")
txt_output=open("/content/output4.txt", "w")
N, M = map(int, txt_input.readline().split())
E = [tuple(map(int, txt_input.readline().split())) for i in range(M)]

def cycle(adj, x, s, n):
    x[n] = 1
    s[n] = 1
    for i in adj[n]:
        if not x[i]:
            if cycle(adj, x, s, i):
                return 1
        elif s[i]:
            return 1
    s[n] = 0
    return 0

def cycle_in_map(N, E):
    adj = [[] for i in range(N + 1)]
    for u, v in E:
        adj[u].append(v)
    x = [0]*(N + 1)
    s = [0]*(N + 1)
    for n in range(1, N + 1):
        if not x[n]:
            if cycle(adj, x, s, n):
                return "YES"

    return "NO"

cycle = cycle_in_map(N,E)

print(cycle, file = txt_output)
txt_output.close()