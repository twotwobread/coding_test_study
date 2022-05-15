import copy
INF = int(1e9)
def init(size,data):
    for i in range(size):
        for j in range(size):
            if data[i][j]==-1:
                data[i][j]=INF #돌은 INF로 설정
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
            if 0<mtrx[row][col]<INF:#나무가 있는 곳
                count = 0
                for dx, dy in direction: #상하좌우 확인
                    x,y = row+dx, col+dy
                    if (0<=x<size and 0<=y<size) and 0<mtrx[x][y]<INF: #주위에 나무가 있으면 +1
                        count+=1
                mtrx[row][col]+=count # 주위 나무 수 만큼 성장
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
                    if 0<=x<size and 0<=y<size and mtrx[x][y]==0: #번식할 수 있는 땅 찾기
                        count+=1 #가능한 장소의 수 증기
                        field.append((x,y)) #번식 가능 위치를 저장
                if count!=0: #번식이 가능할 때에만 처리
                    val = mtrx[row][col]//count
                    for x,y in field:
                        temp[x][y]+=val
    #temp를 사용하여 처리한 이유는 '동시에' 나무가 번식 하기 때문임
    for row in range(size):
        for col in range(size):
            if temp[row][col]>0:
                mtrx[row][col]+=temp[row][col]
    return mtrx

def Find(size, mtrx, pos, scale):#불태우는 경우 잡초를 얼마나 태울 수 있는가 찾는 함수
    d = ((-1,-1),(-1,1),(1,-1),(1,1))
    val = mtrx[pos[0]][pos[1]] #현재 시작 위치를 value로
    for dx, dy in d:
        for i in range(1, scale+1):
            x,y = pos[0]+(dx*i), pos[1]+(dy*i) #제초제의 범위가 점점 넓어짐
            if 0 <= x < size and 0 <= y < size:#정상 범위 안에 있고
                if mtrx[x][y]==INF or mtrx[x][y]<=0: #돌을 만나거나 제초제가 뿌려진 땅을 만나면 더이상 처리할게 없으므로 루프 탈출
                    break
                elif 0<mtrx[x][y]<INF: #잡초발견하면 태운다
                    val+=mtrx[x][y]

            else:#정상범위를 벗어난 경우, 어차피 다음케이스도 범위를 벗어남
                break
    return val

def kill(size, mtrx, scale, maintain):
    case = []
    d = ((-1, -1), (-1, 1), (1, -1), (1, 1))
    flag = False #불태울 수 있는 잡초가 남아있는지 확인하기 위해
    for row in range(size):
        for col in range(size):
            if 0<mtrx[row][col]<INF:#잡초가 있어야 불이 펴저나가므로 잡초가 있는 위치를 잡아서
                flag=True
                count = Find(size, copy.deepcopy(mtrx), (row,col), scale)#한번 불태워 본다
                case.append([count, row, col])

    if flag ==True:#만약 False면 더이상 불태울 수 있는 잡초가 없는것
        case = sorted(case, key = lambda x:(-x[0], x[1], x[2]))#조건대로 벨류가 가장큰놈, 같다면 행이 적은놈, 같다면 열이 적은놈 순으로 정렬
        die = -maintain - 1 #매 라운드 시작시 불태운 위치를 하나씩 회복 => 문제 조건에 따르면 -(제초제가 남은 일 +1) 을 해줘야함
        mtrx[case[0][1]][case[0][2]]=die #불태우는 시작점

        #마찬가지로 불지르기
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
        if val==0: #val ==0이라면 더이상 나무가 없는것.
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

"""
3 2 1 0 0 0 0
4 0 4 0 2 1 4
4 4 4 0 2 0 4
0 0 0 0 3 4 4
2 1 3 2 0 0 0
2 0 0 2 0 0 0
2 2 2 2 0 0 0
"""
