# n x m
# 1 : 이동 가능, 0은 이동 불가
# (1, 1) -> (n, m)
# 최소의 칸 수 구하기
# 서로 인접한 칸만 이동가능
# 시작 위치, 도착 위치 칸 수 포함
# 항상 도착위치로 이동할 수 있는 경우만 주어짐.

# < 미로탐색 >
# 문제 유형 : DFS/BFS
# 자료구조 : 2차원 배열 - 미로 자체가 2차원 배열로 주어지고 값이 원하는 index에서 pop되는 것이 없기 때문에
#                      시간 복잡도가 낮아지지 않을 것이라 예상. 그리고 미로에 맞게 값을 대입하면서 풀 경우 빠를 것이라 예상
#          deque - n, m의 크기가 100이라서 DFS를 이용할 경우 시간 초과 예상. 그래서 bfs 사용. 인접한 인덱스를 넣으면서 처음 인덱스 빼서
#                  처리하기 위한 queue 구현이 필요하여 시간 복잡도 저하를 위해 deque 이용
# 1. 시작 인덱스부터 인접 인덱스를 처리
# 2. 이미 들렸던 곳은 들리지 않음. 그 이유는 depth가 아니라 breath로 탐색하기 때문에 같은 레벨에서의 모든 노드가 distance가 같기 때문.
#    즉, 모든 노드는 항상 최소 distance를 가짐.
# 3. n, m의 값을 리턴하면 답.

from collections import deque

def outOfRange(r, c):
    if 0<=r<n and 0<=c<m:
        return True
    else:
        return False
def bfs(queue):
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            adj_r, adj_c = r + dx[i], c + dy[i]
            if outOfRange(adj_r, adj_c) and maze[adj_r][adj_c] == 1 and (adj_r != 0 or adj_c != 0):
                maze[adj_r][adj_c] = maze[r][c] + 1
                queue.append((adj_r, adj_c))
    return maze[n-1][m-1]

if __name__ == "__main__":
    dx = (0, 0, -1, 1) # 좌우상하
    dy = (-1, 1, 0, 0)
    queue = deque()
    n, m = map(int, input().split(" "))
    maze = [list(map(int, input())) for _ in range(n)]
    queue.append((0,0))
    print(bfs(queue))

# 풀이시간 : 1시간