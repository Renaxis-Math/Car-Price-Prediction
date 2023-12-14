# https://leetcode.com/discuss/interview-question/3749874/Citadel-or-OA-or-2023

from collections import defaultdict
def solveLC(edges):
    G = defaultdict(list)
    for v,w in edges:
        G[v].append(w)
        G[w].append(v)
    ends = set()
    curmax = 0
    def dfs(u, v, d, ends):
        nonlocal curmax
        if d > curmax:
            ends.clear()
            curmax = d 
        if d == curmax:
            ends.add(v)
        for w in G[v]:
            if w == u: continue
            dfs(v, w, d+1, ends)
    dfs(-1, 0, 0, ends)
    v = next(iter(ends))
    nxtends = set()
    dfs(-1, v, 0, nxtends)
    return ends | nxtends