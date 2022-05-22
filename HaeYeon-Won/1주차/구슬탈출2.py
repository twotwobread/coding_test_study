from copy import deepcopy
def init(n,m,data):
    ball=[]
    mtrx = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if data[i][j]=='#':
                mtrx[i][j]=-1
            elif data[i][j]==".":
                continue
            elif data[i][j]=="O":
                hole = (i,j)
            elif data[i][j]=="R":
                red = [i,j]
            elif data[i][j]=="B":
                blue = [i,j]
    ball.append(red) #무조건 red가 먼저
    ball.append(blue)
    return mtrx,ball,hole

def check(ball,hole):
    if (ball[0][0], ball[0][1]) == hole:
        if (ball[1][0], ball[1][1]) != hole:
            return True
    return False

def move(n,m,data,ball,d):
    direction = ((1, 0), (0, 1), (-1, 0), (0, -1))
    if d==-1: return ball
    redCnt = 0 #red가 움직인 시간
    blueCnt = 0 #블루가 움직인 시간

    Rrow, Rcol = ball[0][0], ball[0][1]
    Brow, Bcol = ball[1][0], ball[1][1]

    Rflag, Bflag = False, False #구멍 통과 여부
    #move Red
    while True:
        Rrow,Rcol = Rrow+direction[d][0], Rcol+direction[d][1]
        if data[Rrow][Rcol]==-1:
            Rrow, Rcol = Rrow-direction[d][0], Rcol-direction[d][1]
            break
        elif (Rrow, Rcol)==hole:
            Rflag=True
            break
        redCnt+=1

    #move Blue
    while True:
        Brow, Bcol = Brow + direction[d][0], Bcol + direction[d][1]
        if data[Brow][Bcol] == -1:
            Brow, Bcol = Brow - direction[d][0], Bcol - direction[d][1]
            break
        elif (Brow, Bcol) == hole:
            Bflag=True
            break
        blueCnt+=1
    if (Rflag and Bflag) or Bflag: #둘다 구멍에 빠지거나, 파란공이 구멍에 빠짐 => 실패이므로 굴리기 이전으로
        return ball
    if (Rrow, Rcol)==(Brow, Bcol): # 두 좌표가 같다면?
        if redCnt>blueCnt:
            Rrow -=direction[d][0]
            Rcol -= direction[d][1]
        else:
            Brow -= direction[d][0]
            Bcol -= direction[d][1]

    return [[Rrow, Rcol], [Brow, Bcol]]


def solution(n,m,data,ball,d,depth):
    global result
    if depth>10:
        return
    temp = move(n, m, data, ball, d)
    if temp == ball and depth!=0:  # 움직였는데 없으면 return
        return
    if check(temp, hole):
        result = min(result, depth)
        return
    solution(n, m, data, deepcopy(temp), 0, depth + 1)
    solution(n, m, data, deepcopy(temp), 1, depth + 1)
    solution(n, m, data, deepcopy(temp), 2, depth + 1)
    solution(n, m, data, deepcopy(temp), 3, depth + 1)


if __name__=="__main__":
    n,m = map(int, input().split())
    data = [list(input()) for _ in range(n)]
    data, ball, hole = init(n, m, data)
    result = 11
    solution(n,m,data,ball,-1,0)
    if result==11:
        print(-1)
    else:
        print(result)
"""
문제 
- 빨간구슬, 파란구슬을 넣은 뒤 빨간구슬을 빼내는 게임
- N*M 크기의 배열, 상하좌우로 이동가능, 구슬은 동시에 이동
- 파란구슬이 구멍에 빠지면 실패, 동시에 빠져도 실페
- 10번 이하로 움직여 뺄 수 있다면 -1 출력
문제 유형 
- BFS를 이용한 시뮬레이션
자료구조 
- 리스트(구슬, mtrx의 상태를 표현하기 위해서)
- deque : 구슬의 좌표를 담기 위해서
사용한 아이디어
- 재귀 깊이기 10 초과일 경우 return처리하여 불필요한 함수호출 제거
- 구슬 이동 시 만약 두 구슬이 겹치면 총 이동량을 보고 더 길게 움직인놈을 바로 직전칸으로 이동(겹치기 않게하기 위함)
- 만약 이동 후 구슬이 전 상태와 변함이 없다면 더이상 그 방향으로는 움직일 수 없는것 이므로 return 
- 구슬 이동 시 만약 파란구슬이 구멍으로 들어갔다면 의미없는 움직임 이므로, 움직이기 전 상태로 돌린다.
"""
