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