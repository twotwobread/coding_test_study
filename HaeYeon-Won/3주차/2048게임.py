from copy import deepcopy
from collections import deque
def check(mtrx):
    ans = 0
    for i in mtrx:
        ans = max(ans, max(i))
    return ans

def move(n,mtrx, d):
    global direction
    start = ((n-1,0),(0,0),(0,n-1),(n-1,n-1))#위, 오른쪽, 아래쪽, 왼쪽
    for round in range(n):
        startRow, startCol = start[d][0]+(direction[(d+1)%4][0]*round), start[d][1]+(direction[(d+1)%4][1]*round)
        q = deque()
        for i in range(n): #한 줄씩
            nextRow, nextCol = startRow+(direction[d][0]*i), startCol+(direction[d][1]*i)
            if mtrx[nextRow][nextCol]!=0:
                q.append((nextRow, nextCol))
        targetRow, targetCol = startRow, startCol

        while q:
            nowRow, nowCol = q.popleft()
            if (nowRow, nowCol)==(targetRow, targetCol): #옮겨야 하는놈이 이미 끝부분에 있는 경우
                continue
            if mtrx[targetRow][targetCol]==0:#아무것도 없는 경우
                mtrx[targetRow][targetCol] = mtrx[nowRow][nowCol] #옮기는 방향으로 옮기고
                mtrx[nowRow][nowCol]=0 #원래자리 0

            elif mtrx[targetRow][targetCol]==mtrx[nowRow][nowCol]:# and flag[targetRow][targetCol]==True: #옮기는곳에 있는 두 숫자가 같고 합쳐진 적이 없을때
                mtrx[nowRow][nowCol]=0#현재 있는칸은 밀었으므로 0
                mtrx[targetRow][targetCol]=mtrx[targetRow][targetCol]*2 #target칸은 *2
                targetRow, targetCol = targetRow+direction[d][0], targetCol+direction[d][1] #해당칸은 합쳐졌으므로 다음칸을 타겟으로 변경

            else:#해당 부분이 가득 차 있고, 합칠수도 없을때
                targetRow, targetCol = targetRow + direction[d][0], targetCol + direction[d][1] #아무것도 할 수 없으므로 타켓칸 한칸 변경
                mtrx[targetRow][targetCol] = mtrx[nowRow][nowCol]  # 옮기는 방향으로 옮기고
                if (targetRow, targetCol)==(nowRow, nowCol):#타켓을 옮겼는데 자기 자신이라면
                    continue#그대로
                mtrx[nowRow][nowCol] = 0  # 원래자리 0
    return mtrx
def print_m(mtrx):
    for i in mtrx:
        print(i)
    print()
def solution(n, mtrx, d, depth):
    global result
    if depth == 5:
        temp = check(mtrx)
        result = max(result, temp)
        return
    if d!=-1:
        mtrx = move(n,mtrx,d)
    solution(n, deepcopy(mtrx), 0, depth + 1)
    solution(n, deepcopy(mtrx), 1, depth + 1)
    solution(n, deepcopy(mtrx), 2, depth + 1)
    solution(n, deepcopy(mtrx), 3, depth + 1)


if __name__ =="__main__":
    n = int(input())
    mtrx = [list(map(int, input().split())) for _ in range(n)]
    result = 0
    direction = ((-1,0),(0,1),(1,0),(0,-1)) #위에서 아래, 오른쪽에서 왼, 아래에서 위, 왼족 에서 오른쪽
    solution(n, mtrx,-1, -1)
    print(result)
"""
문제 
- 격자안에 숫자를 상, 하 좌, 우로 밀 수 있음
- 총 5번 이 행위를 반복했을 때 최고로 가질 수 있는 값은?
문제 유형 
- 백트래킹, BFS
자료구조 
- 2차원 리스트 : 기존값 저장, 갱신값 저장에 사용
- deque : 해당 round에서 밀 수 있는 숫자의 위치를 담아옴
사용한 아이디어
- 밀때 미는 방향의 제일 밑 부분 부터 밀기
- 탐지된 숫자는 큐에 담고, 큐에서 빼면서 하나씩 밀어본다.
- 만약 겹치지 않는다면 늦게온것을 뒤로 한칸 민다.
"""