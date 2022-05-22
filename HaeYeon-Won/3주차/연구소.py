from collections import deque
from copy import deepcopy
def init(n,m,data):
    virus = deque()
    for i in range(n):
        for j in range(m):
            if data[i][j]==2:
                virus.append((i,j))
    return virus
def check(n,m,mtrx,virus):
    global direction
    while virus:
        row, col = virus.popleft()
        for dx, dy in direction:
            x,y = row+dx, col+dy
            if 0<=x<n and 0<=y<m and mtrx[x][y]==0:
                mtrx[x][y]=2
                virus.append((x,y))
    result = 0
    for rows in mtrx:
        result+=rows.count(0)
    return result

def solution(n, m, mtrx, virus, depth):
    global result
    if depth==3:
        temp = check(n,m,deepcopy(mtrx),deepcopy(virus))
        result = max(result, temp)
        return
    for row in range(n):
        for col in range(m):
            if mtrx[row][col]==0:
                mtrx[row][col]=1
                solution(n,m,mtrx,virus, depth+1)
                mtrx[row][col]=0

if __name__=="__main__":
    n,m = map(int, input().split())
    mtrx = [list(map(int, input().split())) for _ in range(n)]
    virus = init(n,m,mtrx)
    direction = ((1,0),(0,1),(-1,0),(0,-1))
    result = 0
    solution(n,m,mtrx,virus, 0)
    print(result)
"""
문제 
- 0은 빈칸, 1은 벽, 2는 바이러스
- 벽을 새우고 나서 얻을 수 있는 안전영역의 최대 크기는?
문제 유형 
- 백트래킹, BFS
자료구조 
- 1차원 리스트 : 기존값 저장, 갱신값 저장에 사용
사용한 아이디어
- 백트레킹을 이용하여 하나씩 벽을 새우고 depth==3이 되면 check 함수를 통해 바이러스를 퍼트린 후 남는 칸의 수를 확인
"""
