# nxm
# 인접 : 상하좌우
# 몇일이 지나면 다 익는지, 최소 일수를 구하는 프로그램 작성.
# 상자 일부 칸에 토마토 없을 수 있음.
# 토마토 모두 익지 못하면 -1 출력
# 모든 토마토 익어있으면 0 출력.

# < 토마토 >
# 문제유형 - DFS/BFS 그 중 BFS
# - DFS처럼 쭉 안으로 깊게 들어가는 것이 아닌 단계별로 하나씩 퍼지는 느낌으로 풀 수 있다 생각
# 자료구조
# - 2차원 리스트 : 리스트에서 맨처음 원소를 꺼낼때 N 시간 복잡도라서 느린데 그것처럼 꺼낼
# 원소가 없고 토마토를 표현할 때 격자형식으로 푸는 것이 적합하다 생각.
# - deque : 익은 토마토가 동시에 같이 퍼져나가게 하려면 일단 익은 토마토 정보를 담아둬야한다
# 라고 생각했고 이 부분은 하나씩 첫번째 원소를 빼면서 접근하기 때문에 리스트 대신 deque 사용

# 1. 토마토가 익은 게 여러개면 동시에 퍼지기 시작해야 하기 때문에 deque에 다 담고 BFS
# 2. 상하좌우 중 0 ( 익지 않은 토마토 ) 가 있다면 내 값에서 1을 증가시켜서 넣어줌. 그리고
#    deque 담기
# 3. 반복문을 돌면서 가장 큰 값을 찾고 출력

from collections import deque

def outOfRange(r, c):
    if 0<=r<n and 0<=c<m: return True
    else: return False
def ripe():
    while ripeTomato:
        r, c = ripeTomato.popleft()
        for i in range(4): # 상하좌우
            adj_r, adj_c = r + dx[i], c + dy[i]
            if outOfRange(adj_r, adj_c) and tomato[adj_r][adj_c] == 0:
                tomato[adj_r][adj_c] = (tomato[r][c] + 1)
                ripeTomato.append((adj_r, adj_c))
def findMinDay():
    max = 1 # 값을 넣을때 원래 값에 +1을 시켜서 그것을 완화하기 위함.
    for i in range(n):
        for j in range(m):
            if tomato[i][j] == 0: return 0 # 익지 않은 토마토 존재
            if max < tomato[i][j]:
                max = tomato[i][j]
    return max
def solution():
    for i in range(n):
        for j in range(m):
            if tomato[i][j] == 1:
                ripeTomato.append((i, j)) # 튜플 삽입이유 = 좌표의 변화는 존재하지 않기 때문.
    ripe() # 익히기
    return findMinDay()

if __name__ == "__main__":
    ripeTomato = deque()
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)
    m, n = map(int, input().split(" "))
    tomato = [list(map(int, input().split(" "))) for _ in range(n)]
    print(solution()-1)

# 풀이시간 15분
