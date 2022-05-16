import copy
INF = int(1e9)
def init(size,data):
    for i in range(size):
        for j in range(size):
            if data[i][j]==-1:
                data[i][j]=INF
    return data
def heal(size, mtrx):
    for row in range(size):
        for col in range(size):
            if mtrx[row][col]<0:
                mtrx[row][col]+=1
    return mtrx

def grow(size, mtrx):
    global direction
    for row in range(size):
        for col in range(size):
            if 0<mtrx[row][col]<INF:
                count = 0
                for dx, dy in direction:
                    x,y = row+dx, col+dy
                    if (0<=x<size and 0<=y<size) and 0<mtrx[x][y]<INF:
                        count+=1
                mtrx[row][col]+=count
    return mtrx

def spread(size, mtrx):
    global direction
    temp = [[0 for _ in range(size)] for _ in range(size)]
    for row in range(size):
        for col in range(size):
            if 0<mtrx[row][col]<INF:
                count = 0
                field = []
                for dx, dy in direction:
                    x,y = row+dx, col+dy
                    if 0<=x<size and 0<=y<size and mtrx[x][y]==0:
                        count+=1
                        field.append((x,y))
                if count!=0:
                    val = mtrx[row][col]//count
                    for x,y in field:
                        temp[x][y]+=val
    for row in range(size):
        for col in range(size):
            if temp[row][col]>0:
                mtrx[row][col]+=temp[row][col]
    return mtrx
def Find(size, mtrx, pos, scale):
    d = ((-1,-1),(-1,1),(1,-1),(1,1))
    val = mtrx[pos[0]][pos[1]]
    for dx, dy in d:
        for i in range(1, scale+1):
            x,y = pos[0]+(dx*i), pos[1]+(dy*i)
            if 0 <= x < size and 0 <= y < size:
                if mtrx[x][y]==INF or mtrx[x][y]<=0:
                    break
                elif 0<mtrx[x][y]<INF:
                    val+=mtrx[x][y]
            else:
                break
    return val

def kill(size, mtrx, scale, maintain):
    case = []
    d = ((-1, -1), (-1, 1), (1, -1), (1, 1))
    flag = False
    for row in range(size):
        for col in range(size):
            if 0<mtrx[row][col]<INF:
                flag=True
                count = Find(size, copy.deepcopy(mtrx), (row,col), scale)
                case.append([count, row, col])
    if flag ==True:
        case = sorted(case, key = lambda x:(-x[0], x[1], x[2]))
        die = -maintain - 1
        mtrx[case[0][1]][case[0][2]]=die
    
        for dx, dy in d:
            for i in range(1, scale+1):
                x,y = case[0][1]+(dx*i), case[0][2]+(dy*i)
                if 0 <= x < size and 0 <= y < size:
                    if mtrx[x][y]==INF:
                        break
                    elif 0<mtrx[x][y]<INF:
                        mtrx[x][y]=die
                    elif mtrx[x][y]<=0:
                        mtrx[x][y] =die
                        break
                else:
                    break
        return mtrx, case[0][0]
    else:
        return mtrx, 0


def solution(size,loop,scale,maintain,mtrx):
    result = 0
    for i in range(loop):
        mtrx = heal(size, mtrx)
        mtrx = grow(size, mtrx)
        mtrx = spread(size, mtrx)
        mtrx, val = kill(size, mtrx, scale, maintain)
        if val==0:
            print(result)
            return
        result+=val
    print(result)

if __name__=="__main__":
    size,loop,scale,maintain = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(size)]
    mtrx = init(size, data)
    del data
    direction = ((1,0),(0,1),(-1,0),(0,-1))
    solution(size,loop,scale,maintain,mtrx)

"""
문제 
- mtrx size : n, 박멸이 진행되는 년 수 : m, 제초제 확산 범위 k,  제초제가 남아있는 년수 : c
- 나무의 성장, 번식 -> 제초제 순으로 진행될 때 최대 벌목 수?
문제 유형 
- BFS를 이용한 시뮬레이션
자료구조 
- 2차원 리스트 : mtrx 정보 저장
사용한 아이디어
- 순서대로 회복, 나무의 성장, 번식, 제거를 반복
- 바위는 INF로 설정하여 제초제와 구분을 두었음
- 루프 시작시 회복을 하기때문에 제거할때 값을 -maintain-1 로 설정
- 나무 제거 시작점을 찾기위해 lambda 함수를 사용하여 정렬의 우선순위 부여

"""
