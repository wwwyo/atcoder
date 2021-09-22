# https://atcoder.jp/contests/abc211/tasks/abc211_d
import sys
import queue
n,m = map(int,input().split())
# ab = [list(map(int,input().split)) for _ in range(n)]
ab = []
for s in sys.stdin.readlines():
    ab.append(list(map(int,s.split())))

visited = set()
q = queue.Queue()
visited.add()
q.put()

while not q.empty():
    