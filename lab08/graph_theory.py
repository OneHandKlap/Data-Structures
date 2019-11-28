#BFS
from Queue import queue
def bfs(g, start):
    start.setDistance(0)
    start.setPred(None)
    vertQueue=Queue()
    vertQueue.enqueue(start)
    while(vertQueue.size()>0):
        current