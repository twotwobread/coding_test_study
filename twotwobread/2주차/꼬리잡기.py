# < 꼬리 잡기 >
# [문제유형] : DFS/BFS, 시뮬레이션
# [자료구조] : 2차원 리스트 - 맵 상의 기차와 기차 노선을 표현하고 기차의 움직임을 표현하기 위해서
#                          사용, 특정 위치가 pop되는 것이 없고 특정 인덱스를 수정해야해서 이를 사용
#           deque - 기차의 머리와 꼬리를 표현하기 위해서 사용, 기존 방식을 머리 꼬리 둘다 popleft하여
#                   하여 바꿨는데 수정하면서 그냥 서로 swap하는 방식으로 했기에 리스트를 사용해도 무방
# [구현순서]
# 1. 먼저 주어진 map 상에서 머리와 꼬리를 모두 찾음 - 머리를 찾고 dfs를 이용하여 꼬리로 향하는 방법 채택
#                                                   이를 이용 시 주의할 부분은 이전에 들어갔던 칸으로 들어가게 된다면 메모리 초과가 날 수 있음
#                                                   계속 똑같은 정보를 deque안에 넣기때문에 조심해야함.
# 2. 찾은 머리를 이용해서 앞으로 전진 - 4를 찾고 그쪽으로 1을 이동 그 후 이전 인덱스를 2로 수정, 하지만 기차의 길이와 선로의 길이가 같은 경우 3을 찾아야함.
#    꼬리를 이용해서 앞으로 전진 - 2를 찾고 그쪽으로 3을 이동 그후 이전 인덱스를 4로 수정, 하지만 기차의 길이와 선로의 길이가 같은 경우 4로 수정하면 안됨.
# 3. 이동이 끝나고 선물을 던짐 - 선물은 우상좌하 순서로 던지는데 라운드의 순서는 하우상좌 임.
# 4. 선물을 던지다가 기차에 맞으면 그 인덱스부터 기차의 머리를 찾으러 dfs를 무조건 더 작거나 같은 인덱스로 이동하는데 이전 인덱스로 가지 않기 위해서 그 정보까지 포함하여 재귀
#    주의할점은 1. 2에 맞으면 꼬리로 갈 수가 있음. 이를 무마시키기 위해서 return check를 이용하여 1에 도착할 경우만 check를 true로 만듬. 그래서 3까지 갔다가 false로 리턴
#              2. 기차가 가득차있을 경우, 3에서 바로 1로 갈 수 있음. 그래서 이를 방지하기 위해서 조건문을 사용
#    기차에 맞으면 머리로 이동하면서 cnt를 증가시키고 머리에 도달했을 경우 cnt 값을 저장, 그 후 이전 저장했던 정보를 이용하여 머리와 꼬리를 바꿈.
# 5. 이전에 찾은 cnt 값을 이용하여 모든 기차의 점수를 합하기 때문에 sum = (cnt*cnt)를 함.
# 6. 그리고 선물 던지기가 n이 될 경우 우상좌하 이 방향이 바뀌어야하고 라운드 진행될 때는 하우상좌가 바뀌어야함. 이는 우상좌하에서 -1한 방향이 하우상좌이고 이를 이용하여 구현.
# [아이디어]
# - 이전에 문제풀 땐 기차의 모습을 정확히 몸통까지 다 알아야한다고 생각, 그 이유는 기차의 몇번째에 위치하는지 알아야 점수를 계산할 수 있기에
#   dict를 이용하여 몇번째 기차의 몸통인지 아닌지 파악. 하지만 이 경우 {1:[deque(), deque()]} 이런식으로 표현하여 너무 복잡함.
# - 기차의 머리랑 꼬리만 알면된다고 생각. 그 이유는 기차의 움직임은 머리랑 꼬리로만 표현 가능. 그리고 몇번째에 위치하는지는 선물이 닿았을 때
#   dfs/bfs로 파악할 수 있음. 그리고 몇번째 기차인지는 알필요가 없음. sum을 하나로 뭉뚝그려서 표현하기 때문에 그러함.
# - 앞서 말했던 우상좌하, 하우상좌를 이용한 선물의 던지기 방향 설정.
from collections import deque
def search(queue, new):
    while queue:
        r, c, v, direct = queue.popleft()
        if v == 3:
            new.append([r, c])
            break
        for i in range(4):
            if i == direct:
                continue
            adj_r, adj_c = r + dx[i], c + dy[i]
            if 0<=adj_r<n and 0<=adj_c<n and game[adj_r][adj_c] != 4 and v <= game[adj_r][adj_c]:
                queue.append((adj_r, adj_c, game[adj_r][adj_c], (i-2)%4))
    return new
def init():
    queue = deque()
    for i in range(n):
        for j in range(n):
            if game[i][j] == 1:
                queue.append((i, j, game[i][j], -1))
                train.append(search(queue, [[i, j]]))
                queue.clear()
def move():
    for t in range(len(train)):
        head, tail = train[t][0], train[t][1]
        for i in range(4):
            adj_r, adj_c = head[0] + dx[i], head[1] + dy[i]
            if 0<=adj_r<n and 0<=adj_c<n and (game[adj_r][adj_c] == 4 or game[adj_r][adj_c] == 3):
                game[head[0]][head[1]] = 2
                game[adj_r][adj_c] = 1
                train[t][0] = [adj_r, adj_c]
        for i in range(4):
            adj_r, adj_c = tail[0] + dx[i], tail[1] + dy[i]
            if 0<=adj_r<n and 0<=adj_c<n and game[adj_r][adj_c] == 2 and (adj_r != head[0] or adj_c != head[1]):
                if game[tail[0]][tail[1]] != 1:
                    game[tail[0]][tail[1]] = 4
                game[adj_r][adj_c] = 3
                train[t][1] = [adj_r, adj_c]

def findHead(r, c, br, bc, cnt, check):
    global count
    if game[r][c] == 1:
        # 머리랑 꼬리랑 바꾸는 거 추가해야함.
        count = cnt
        check = True
        for i in range(len(train)):
            if [r, c] == train[i][0]:
                game[r][c] = 3
                game[train[i][1][0]][train[i][1][1]] = 1
                train[i][0], train[i][1] = train[i][1], train[i][0]
                break
        return check
    for i in range(4):
        nr, nc = r + dx[i], c + dy[i]
        if 0<=nr<n and 0<=nc<n and game[nr][nc] != 0 and game[r][c] >= game[nr][nc] and (nr!=br or nc != bc):
            if game[r][c] == 3 and game[nr][nc] == 1:
                continue
            check = findHead(nr, nc, r, c, cnt+1, check)
            if check:
                return check
    return False

def throw(d, row, col):
    global sumValue, count
    for i in range(n):
        nr, nc = row + (dx[d]*i), col + (dy[d]*i)
        if 0 < game[nr][nc] < 4:
            count = 1
            if findHead(nr, nc, -1, -1, 1, False):
                sumValue += (count*count)
                break
def solution():
    init()
    row = 0; col = 0; d = 3
    for loop in range(k):
        if (loop % n) == 0:
            d = (d+1) % 4
        else:
            row += dx[(d-1)%4]
            col += dy[(d - 1) % 4]
        move()
        throw(d, row, col)

if __name__ == "__main__":
    dx = (0, -1, 0, 1) # 우상좌하
    dy = (1, 0, -1, 0)
    sumValue = 0
    count = 0
    train = deque()
    n, m, k = map(int, input().split())
    # 격자 크기, 팀 수, 라운드 수
    game = [list(map(int, input().split())) for _ in range(n)]
    solution()
    print(sumValue)
