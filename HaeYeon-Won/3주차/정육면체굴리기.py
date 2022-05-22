from collections import defaultdict
def move(n,m,pos,mtrx,cube,d):
    global direction, relation, table
    nextRow,nextCol = pos[0]+direction[d][0], pos[1]+direction[d][1]
    if 0<=nextRow<n and 0<=nextCol<m:
        newcube = [0,0,0,0,0,0]
        for i in range(6):
            newcube[table[d-1][i]]=cube[i]

        if mtrx[nextRow][nextCol] == 0:
            mtrx[nextRow][nextCol] = newcube[5]
        elif mtrx[nextRow][nextCol] != 0:
            newcube[5] = mtrx[nextRow][nextCol]
            mtrx[nextRow][nextCol]=0
        print(newcube[0])
        return (nextRow,nextCol), newcube
    else:
        return pos, cube
def solution(n,m,mtrx,pos, plan):
    global relation
    cube = [0,0,0,0,0,0]
    for d in plan:
        pos, cube= move(n,m,pos,mtrx,cube,d)

if __name__ =="__main__":
    n, m, startRow, startCol, k = map(int,input().split())
    mtrx = [list(map(int,input().split())) for _ in range(n)]
    plan = list(map(int, input().split()))
    direction = ((0, 0), (0, 1), (0, -1), (-1, 0), (1, 0))  # 동 서 북 남
    relation = [5, 3, 4, 1, 2, 0]
    table = defaultdict(list)
    table[0] = [4,1,0,3,5,2]
    table[1] = [2,1,5,3,0,4]
    table[2] = [1,5,2,0,4,3]
    table[3] = [3,0,2,5,4,1]
    solution(n,m,mtrx,(startRow,startCol), plan)
"""
문제 
- 주사위를 굴릴때 칸에 있는 수가 0 -> 주사위 바닥 숫자가 칸으로 복사
- 칸에있는 수가 0 이 아님 -> 주사위 바닥으로 칸 수가 복사, 칸 수는 0
문제 유형 
- 시뮬레이션
자료구조 
- 2차원 리스트 : 칸 수 저장
- defaultdict : 각 움직임에 대한 주사위 눈 상태 변화 표시
- 1차원 리스트 : 주사위 값 저장
사용한 아이디어
- 주사위를 동, 서, 북, 남 으로 굴렸을때 변하는 눈을 각각 표시
- 매 움직임 마다 위 값을 바탕으로 주사위 눈의 값을 저장한 일차원 리스트 변경
"""