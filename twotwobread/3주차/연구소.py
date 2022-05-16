# < 연구소 >
# 문제 유형 : 백트래킹, DFS/BFS
# 자료 구조 : 2차원 리스트 - 빈 칸, 벽, 바이러스의 정보를 담기 위함.
#           1차원 리스트 - 빈 칸의 정보를 담아 둠. ( 이를 이용하여 백트래킹 )
#           2차원 리스트 - 벽을 세우고 바이러스를 퍼트린 후에 점수를 세기 위함.
# < 구현 순서 >
# 1. 먼저 2차원 리스트를 반복하여 빈 칸의 정보를 1차원 리스트에 담는다.
# 2. 그리고 1차원 리스트를 읽으면서 이전 벽보다 인덱스가 큰 놈부터 시작해서 result에 채운다.
# 3. 길이가 3개가 되었을때, 바이러스를 bfs로 퍼트리고 반복문을 돌면서 안전영역의 크기를 구한다.
# 4. 안전영역의 최대값을 찾으면 출력한다.
def score(virus, result):
    global maxValue
    new = [graph[i].copy() for i in range(n)]
    l_virus = [virus[i] for i in range(len(virus))]
    for r in result:
        new[r[0]][r[1]] = 1
    while l_virus:
        row, col = l_virus.pop()
        for i in range(4):
            adj_r, adj_c = row + dx[i], col + dy[i]
            if 0<=adj_r<n and 0<=adj_c<m and new[adj_r][adj_c] == 0:
                new[adj_r][adj_c] = 2
                l_virus.append((adj_r, adj_c))
    cnt = 0
    for i in range(n):
        for j in range(m):
           if new[i][j] == 0:
               cnt += 1
    if maxValue < cnt:
        maxValue = cnt
def findMax(empty, start, virus):
    if len(result) == 3:
        score(virus, result)
        return
    for i in range(start, len(empty)):
        result.append(empty[i])
        findMax(empty, i+1, virus)
        result.pop()
def solution():
    empty = []; virus = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0: # 빈 칸인 경우
                empty.append((i, j))
            elif graph[i][j] == 2:
                virus.append((i, j))
    findMax(empty, 0, virus)
if __name__ == "__main__":
    dx = (0, 1, 0, -1) # 동남서북
    dy = (1, 0, -1, 0)
    result = []
    maxValue = -1
    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    solution()
    print(maxValue)