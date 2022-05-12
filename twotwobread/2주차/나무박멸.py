# < 나무박멸 >
# 문제유형 : 시뮬레이션, DFS/BFS
# 자료구조 : 2차원 리스트 - 나무, 제초제 등과 같은 정보를 받기위해서 쓰고 제초제를 뿌리고
#                       나무 성장, 번식등을 위해 쓰기에 적합함.
#          deque - 동시에 일어난다를 구현하기에 가장 적합할 것으로 예상.
# < 동작 순서 >
# 1. 먼저 성장을 위해서 나무가 있는 인덱스를 찾고 이를 deque에 담아줌. 그리고 deque를
#    popleft하면서 해당 인덱스의 주위에 몇개의 갈 수 있는 인덱스가 있는지 확인 후 for가 끝나면
#    count만큼 방문 가능한 인덱스에 더할 예정. 그러기 위해선 방문 가능한 인덱스를
#    담아둘 리스트가 필요. -> 이 부분은 deque 필요없음 왜냐면 동시에 발생해야지만 지금 현재
#    인덱스의 값을 이용하지 않고 인접 노드 개수만 이용하기에 그냥 포문 돌리기
# 2. 다음은 번식, 위와 비슷하게 벽, 나무, 제초제가 없는 칸에 번식 진행하고 번식 가능한
#    인접노드를 count하고 가능한 인덱스를 리스트에 담아둔 후 for가 끝나면 가능한 인덱스에
#    자기 값 나누기 count로 더해줌 -> 여기서 deque가 필요.
# 3. 그 다음 제초제 뿌리기. 벽이 있는 경우, 전파되지 않음. 그리고 c년만큼 제초제가 남아있다
#    그러면 c+1년째에 사라짐. 그럼 0에서 사라진다. 이말임. 제초제는 빈칸에 들어가면 거기말고
#    다른 칸으로 전파가 없음. 그래서 나무가 있는 곳만 살펴보면서 대각선으로 k만큼 가보는 거임.
#    그걸 위해서 4칸의 check 리스트를 만들고 벽이나 빈칸을 만나면 해당 방향 체크해서 멈추게
#    만들면 좋을듯
# 4. 내 생각에는 먼저 제초제 없애고 바로 뿌리면 될듯
from collections import deque
def outOfRange(r, c):
    if 0<=r<n and 0<=c<n:
        return True
    else:
        return False
def grow():
    dx = (0, 1, 0, -1) # 우하좌상
    dy = (1, 0, -1, 0)
    for i in range(n):
        for j in range(n):
            if forest[i][j] > 0:
                count = 0
                for l in range(4):
                    adj_r, adj_c = i + dx[l], j + dy[l]
                    if outOfRange(adj_r, adj_c) and forest[adj_r][adj_c] > 0:
                        count += 1
                forest[i][j] += count
def breeding():
    tree = deque()
    dx = (0, 1, 0, -1)  # 우하좌상
    dy = (1, 0, -1, 0)
    for i in range(n):
        for j in range(n):
            if forest[i][j] > 0:
                tree.append((i, j, forest[i][j]))
    plus = [[0]*n for _ in range(n)]
    while tree:
        r, c, num = tree.popleft()
        adj = []; count = 0
        for i in range(4):
            adj_r, adj_c = r + dx[i], c + dy[i]
            if outOfRange(adj_r, adj_c) and forest[adj_r][adj_c] == 0:
                adj.append((adj_r, adj_c))
                count += 1
        for i in adj:
            plus[i[0]][i[1]] += (num//count)
    for i in range(n):
        for j in range(n):
            if plus[i][j] != 0:
                forest[i][j] += plus[i][j]
def findIndex():
    dx = (-1, 1, 1, -1)
    dy = (-1, -1, 1, 1)
    # 최적의 인덱스 찾기
    maxIndex = (-1, -1)
    maxValue = -1
    for i in range(n):
        for j in range(n):
            if forest[i][j] > 0:
                check = [1]*4
                sumValue = forest[i][j]
                for l in range(1, k+1):
                    for y in range(4):
                        if check[y]:
                            adj_r, adj_c = i + (dx[y]*l), j + (dy[y]*l)
                            if outOfRange(adj_r, adj_c) and forest[adj_r][adj_c] > 0:
                                sumValue += forest[adj_r][adj_c]
                            else:
                                check[y] = 0
                    if check[0] == 0 and check[1] == 0 and check[2] == 0 and check[3] == 0:
                        break
                if maxValue < sumValue:
                    maxValue = sumValue
                    maxIndex = (i, j)
                elif maxValue == sumValue:
                    if maxIndex[0] > i:
                        maxValue = sumValue
                        maxIndex = (i, j)
                    elif maxIndex[0] == i:
                        if maxIndex[1] > j:
                            maxValue = sumValue
                            maxIndex = (i, j)
    return maxIndex, maxValue
def killer(loop, index, wall):
    dx = (-1, 1, 1, -1)
    dy = (-1, -1, 1, 1)
    # 먼저 제초제 없애기 시전
    if loop == 0:
        for i in range(n):
            for j in range(n):
                if forest[i][j] == -1:
                    wall.append((i, j))
    else:
        for i in range(n):
            for j in range(n):
                if forest[i][j] < 0 and not (i, j) in wall:
                    forest[i][j] += 1
    # 제초제 뿌리기
    check = [1]*4
    forest[index[0]][index[1]] = -c
    for i in range(1, k+1):
        for j in range(4):
            if check[j]:
                adj_r, adj_c = index[0] + (dx[j] * i), index[1] + (dy[j] * i)
                if outOfRange(adj_r, adj_c) and forest[adj_r][adj_c] > 0:
                    forest[adj_r][adj_c] = -c
                else:
                    if outOfRange(adj_r, adj_c) and not (adj_r, adj_c) in wall:
                        forest[adj_r][adj_c] = -c
                    check[j] = 0
# 나무 : 1이상, 빈칸 : 0, 벽 : -1
def solution():
    result = 0
    wall = []
    for loop in range(m):
        # 1. 성장
        grow()
        # 2. 번식
        breeding()
        # 3. 제초제 위치 선정
        index, value = findIndex()
        if value == -1:
            break
        else:
            result += value
        # 4. 제초제 제거 및 뿌리기
        killer(loop, index, wall)
    return result

if __name__ == "__main__":
    n, m, k, c = map(int, input().split())
    # 격자 크기, 진행 년 수, 제초제 확산 범위, 제초제 존재 년 수
    forest = [list(map(int, input().split())) for _ in range(n)]
    print(solution())