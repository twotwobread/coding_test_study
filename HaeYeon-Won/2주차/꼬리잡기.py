from collections import deque
def init(size, mtrx):
    headPos = deque()
    for row in range(size):
        for col in range(size):
            if mtrx[row][col]==1:
                headPos.append((row,col)) #머리 위치 저장
    return headPos

def move(size, mtrx, headPos):
    global direction
    newHead = deque()
    while headPos:
        row, col = headPos.popleft()
        for dx, dy in direction:
            x,y = row+dx, col+dy
            if 0<=x<size and 0<=y<size:
                if mtrx[x][y]==3:#선로가 가득 찬 경우
                    #진행 방향 찾기
                    bodyX, bodyY = getNext(size, mtrx, (x,y)) #꼬리쪽 진행방향 몸통 찾기
                    mtrx[bodyX][bodyY]=3 #찾은 몸통을 꼬리로 변경
                    mtrx[row][col] = 2 #머리쪽으로 몸통 밀기
                    mtrx[x][y]= 1 #꼬리 쪽으로 머리 밀기
                    newHead.append((x,y))
                    break

                elif mtrx[x][y]==4: #선로를 찾았다!
                    mtrx[x][y]=1 #선로 방향으로 머리를 옮김
                    newHead.append((x,y))
                    mtrx[row][col]=4 #기존 위치를 선로로
                    flag = True #기차의 꼬리까지 진행
                    visited = []
                    while flag:
                        for dx, dy in direction:
                            x, y = row+dx, col+dy
                            #꼬리를 찾아가며 한칸씩 이동
                            if 0 <= x < size and 0 <= y < size and (x,y) not in visited:
                                if mtrx[x][y]==2: #몸통 발견
                                    mtrx[row][col]=2 #선로였던 부분을 몸통으로 채우고
                                    visited.append((row,col))
                                    mtrx[x][y]=4#이동한 자리는 선로로 변경
                                    row, col = x,y#선로에서 다시 찾기 시작
                                elif mtrx[x][y]==3:#꼬리를 발견한 경우
                                    mtrx[row][col] = 3 #원래 위치를 꼬리로 바꾸고
                                    mtrx[x][y] = 4#기존에 위치를 선로로 변경해줌
                                    flag=False# 플레그 값을 변경하여 루프 탈출
                                    break
                    break
    return mtrx, newHead #갱신된 mtrx, headPos를 반환

def getHeadnTail(size, mtrx, start):
    global direction
    swap = {}
    if mtrx[start[0]][start[1]]==1:
        swap['head'] = (start[0], start[1])
    elif mtrx[start[0]][start[1]]==3:
        swap['tail'] = (start[0], start[1])
    q = deque([start])
    visited = [start]
    while q:
        row, col = q.popleft()
        for dx, dy in direction:
            x,y = row+ dx, col+dy
            if 0 <= x < size and 0 <= y < size:
                if mtrx[x][y] not in [0,4] and (x,y) not in visited:
                    if mtrx[x][y]==1:
                        swap['head'] = (x,y)
                    elif mtrx[x][y]==3:
                        swap['tail'] = (x,y)
                    q.append((x,y))
                    visited.append((x,y))
    return swap

def getNext(size, mtrx, head):#꼬리부터 칸수를 세기 시작하는것을 방지
    global direction
    for dx, dy in direction:#헤드기준 4방향 확인
        x,y = head[0]+dx, head[1]+dy
        if 0 <= x < size and 0 <= y < size and mtrx[x][y]==2: #범위내에 있고 몸통을 발견
            return (x,y)

def change(size, mtrx, headPos, target):
    global direction
    flag = True
    if mtrx[target[0]][target[1]]==1: #시작위치를 골랐는데 머리라면 점수는 1
        point = 1
        flag = False
    
    swap = getHeadnTail(size, mtrx, target)
    q = deque()
    headRow, headCol = swap['head'][0], swap['head'][1]
    tailRow, tailCol = swap['tail'][0], swap['tail'][1]

    if flag: #head가 아닌 경우
        nextRow, nextCol = getNext(size, mtrx, (headRow, headCol)) #꼬리말고 다음위치 찾아오기
        q.append((nextRow, nextCol, 2)) #두번째칸(몸통)을 큐에 추가 -> head와 두번째 칸이 visited에 담겨있기 때문에 순방향으로 진행
        visited = [(headRow, headCol), (nextRow, nextCol)]
        while q:
            row, col, order = q.popleft()
            if (row, col)==target: #만약 (row,col)이 공을 맞는 위치와 같다면 점수 산출후 루프탈출
                point = order**2
                break
            for dx, dy in direction:
                x,y = row+ dx, col+dy
                if 0 <= x < size and 0 <= y < size and mtrx[x][y]!=0 and (x,y) not in visited:
                    q.append((x,y, order+1)) #칸수를 하나씩 증가시켜가며 진행
                    visited.append((x,y))

    #머리와 꼬리 부분 변경
    headPos.remove((headRow, headCol))
    headPos.append((tailRow,tailCol))
    mtrx[headRow][headCol], mtrx[tailRow][tailCol] = mtrx[tailRow][tailCol], mtrx[headRow][headCol]
    return mtrx, headPos, point

def getPoint(size, modRound, d, mtrx, headPos):
    global direction
    start = ((0,0),(size-1, 0), (size-1,size-1), (0,size-1))#각 던지는 방법 별 시작 위치
    #던지는 방법별 시작위치에서 direction[d-1][0 or 1]*modRound을 해주게 되면 해당 round에서 던져야 하는 행 or 열로 이동함
    pos = (start[d][0]+(direction[d-1][0]*modRound), start[d][1]+(direction[d-1][1]*modRound))
    q = deque([pos])
    while q:
        row, col = q.popleft()
        if 0<=row<size and 0<=col<size:
            if mtrx[row][col] not in [0,4]:
                return change(size, mtrx, headPos, (row,col)) #점수를 얻을 수 있을 때
            newRow, newCol = row+direction[d][0], col+direction[d][1]
            q.append((newRow, newCol))
    return mtrx, headPos, 0

def solution(size,loop,mtrx, headPos):
    result = 0
    d = 0
    for round in range(loop):
        mtrx, headPos = move(size, mtrx, headPos)
        mtrx, headPos, val = getPoint(size, (round%size), d, mtrx, headPos)
        result+=val
        if (round+1)%size==0: #모든 행(or열)에 다 공을 던져 봤으면
            d = (d+1)%4 #다음 던지는 방식으로 변경해줌
    print(result)

if __name__=="__main__":
    n,m,k = map(int, input().split())
    mtrx = [list(map(int,input().split())) for _ in range(n)] #0은 빈칸, 1은머리,2는 나머지, 3은꼬리, 4는 이동 선
    direction = ((0,1), (-1,0),(0,-1), (1,0))
    headPos = init(n, mtrx)
    solution(n,k,mtrx, headPos)
"""
문제 
- mtrx size : n, team의 수 : m, 반복횟수 k
- 머리 방향으로 이동-> 공을 던짐 순으로 반복 하였을때 최종 점수
문제 유형 
- BFS를 이용한 시뮬레이션
자료구조 
- 2차원 리스트 : mtrx 정보 저장
- deque : head칸의 정보, BFS시 사용
- 1차원 리스트 : BFS 진행 시 방문 여부 파악
사용한 아이디어
- 순서대로 머리쪽으로 이동, 공던지기 반복
- 머리위치에서 탐색 하였을때 선로가 탐지되면 선로가 가득차지 않은 경우, 꼬리가 탐지되면 선로가 가득 찬 경우로 생각하여 풀이
- 점수 계산시 꼬리부터 시작하는것을 방지하기 위하여 무조건 머리 다음칸 부터 탐색 시작
"""

