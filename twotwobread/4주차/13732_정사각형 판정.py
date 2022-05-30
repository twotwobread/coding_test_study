def dfs(x, y, value, func):
    check[x][y] = 1
    if func == 'w':
        adj_r, adj_c = x, y + 1
        if 0<=adj_r<N and 0<=adj_c<N and grid[adj_r][adj_c] == '#':
            return dfs(adj_r, adj_c, value+1, func)
    else:
        adj_r, adj_c = x + 1, y
        if 0 <= adj_r < N and 0 <= adj_c < N and grid[adj_r][adj_c] == '#':
            return dfs(adj_r, adj_c, value + 1, func)
    return value
def checkAll(x, y, width, height):
    for h in range(height):
        for w in range(width):
            nx, ny = x + h, y + w
            check[nx][ny] = 1
            if grid[nx][ny] == '.':
                return False
    return True
def solution():
    global cnt
    for i in range(N):
        for j in range(N):
            if grid[i][j] == '#' and check[i][j] == 0:
                width = dfs(i, j, 1, 'w')
                height = dfs(i, j, 1, 'h')
                if not(width == 1 and height == 1) and (width == height):
                    if checkAll(i, j, width, height):
                        cnt += 1
                        if cnt > 1:
                            return False
                    else:
                        return False
                else:
                    return False
    return True
if __name__ == "__main__": # 여기서 짤려니까 개 ㅈ 같네
    T = int(input())
    for t in range(T):
        N = int(input())
        grid = [list(input()) for _ in range(N)]
        check = [[0]*N for _ in range(N)]
        cnt = 0
        if solution():
            print("#{} yes".format(t + 1))
        else:
            print("#{} no".format(t + 1))