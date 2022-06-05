"""
문제
- n*m 격자 위에서 자동차가 주행
- 현재 방향 기준 왼쪽 방향으로 간적이 없다면 좌회전 해서 해당 방향으로 전진
- 왼쪽이 인도 or 방문 => 좌회전 하고 위를 반복
- 4방향 확인했는데 전직하지 못하면 바라본 방향 유지하고 후진
- 위를 시도했는데 뒷공간이 인도라면 정지
문제 유형
- 시뮬레이션
- BFS
자료구조
- 2차원 리스트 : 배열정보 저장
- tuple : 차량이 움직이는 방향 정의
- deque : 자동차의 진행 방향 파악에 사용
사용한 아이디어
- 방문 한 공간은 -1로 표시 하여 방문 여부 파악
- 방향 d는 0~3 북동남서 이므로 위와같이 direction 튜플 구성, 좌회전은 (현재방향-1)%4로 구현
"""
from collections import deque
def check(mtrx):
    result =0
    for rows in mtrx:
        result+=rows.count(-1)
    return result

def solution(n,m,pos, mtrx):
    direction = ((-1,0),(0,1),(1,0),(0,-1)) #북동남서
    q = deque([pos])
    mtrx[pos[0]][pos[1]]=-1
    while q:
        flag = False # 자동차의 이동 여부 파악
        row, col ,d = q.popleft()
        #1. 현재 방향을 기준으로 왼쪽방향으로 회전, 한번도 가본적 없다면 해당 방향으로 전진
        for i in range(1, 5):
            newD = (d-i)%4
            newRow, newCol = row+direction[newD][0], col+direction[newD][1] #좌회전 해서 전진한 칸
            #2. 만약 왼쪽 방향이 인도이거나 이미 방문한 도로인 경우 좌회전 하고 다시 1번 과정을 반복
            if mtrx[newRow][newCol] not in [-1,1]: #방문 or 인도가 아니라면
                mtrx[newRow][newCol] = -1
                q.append((newRow, newCol, newD))
                flag = True
                break
        if not flag: #4방향을 봤는데 이동을 못한다면
            newD = (d+2)%4 #반대 방향
            newRow, newCol = row+direction[newD][0], col+direction[newD][1] #후진한 칸
            if mtrx[newRow][newCol]==1: #후진하려 봤는데 인도
                break
            q.append((newRow, newCol, d)) # 방향은 유지한 채로 칸만 이동

    result = check(mtrx)
    print(result)
    return



if __name__ =="__main__":
    n,m = map(int, input().split())
    startRow, startCol, d = map(int, input().split())
    mtrx = [list(map(int, input().split())) for _ in range(n)]
    solution(n,m,(startRow, startCol, d), mtrx)
