# < 2048 게임 >
# 문제유형 : 시뮬레이션, DFS/BFS, 백트래킹
# 자료구조 : 2차원 리스트 - 기울일 값들을 저장하기 위함.
#          1차원 리스트 - 5개의 방향을 담기 위함.
#          MAX 변수 - 최대 값을 저장하기 위함.
#          dx, dy - 상하좌우 방향으로 이동하기 위함.
# < 아이디어 >
# - 매 방향을 찾을때마다 기울이면 copy하고 이러는 횟수가 너무 많아져서 5개의 방향을 다 찾으면 한번에 5번의 기울이기를 실시
# - (상, 좌) 와 (하, 우)를 묶어서 해결 - 그이유는 상좌는 위쪽 혹은 왼쪽 인덱스를 먼저 봐야하고, 하우는 밑쪽 혹은 오른쪽 인덱스를 먼저 봐야함.
#   상좌는 1 ~ n으로 for문 진행, 하우는 n ~ 1로 for문 진행.
# < 구체적인 동작 구현 >
# 1. 5개의 방향을 찾음.
# 2. 기울이기를 실시.
# 3. 최대값을 찾음.

# 이런 문제 나왔을 때, 틀리게 된다면 모든 방향의 기울이기 같은 함수가 제대로 실행되는지 확인.
# dx, dy 오른쪽 방향이 (0,0)으로 적혀있어서 1시간 썼음,,,

def push(new, direct, pos, check):
    adj_r, adj_c = pos[0] + dx[direct], pos[1] + dy[direct]
    if 0<=adj_r<n and 0<=adj_c<n: # 격자 안에 존재하면
        if new[adj_r][adj_c] == 0: # 다음 칸이 빈칸인 경우 그냥 값을 옮김.
            new[adj_r][adj_c] = new[pos[0]][pos[1]]
            new[pos[0]][pos[1]] = 0
            push(new, direct, [adj_r, adj_c], check)
        elif new[pos[0]][pos[1]] == new[adj_r][adj_c]: # 다음 같이 빈칸이 아닌데 현재 값과 같은경우
            if check[adj_r][adj_c] == 0: # check 값이 0이면 더해줌.
                new[adj_r][adj_c] += new[pos[0]][pos[1]]
                new[pos[0]][pos[1]] = 0
                check[adj_r][adj_c] = 1
def pushAll(result):
    global MAX
    new = [grid[i].copy() for i in range(n)]
    for direct in result:
        check = [[0]*n for _ in range(n)]
        if (direct % 2) == 0: # 상, 좌
            for i in range(n):
                for j in range(n):
                    if new[i][j] >= 2:
                        push(new, direct, [i, j], check)
        else: # 하, 우
            for i in range(n-1, -1, -1):
                for j in range(n - 1, -1, -1):
                    if new[i][j] >= 2:
                        push(new, direct, [i, j], check)
    maxValue = max(max(n) for n in new)
    if MAX < maxValue:
        MAX = maxValue
def solution(): # 5개의 방향을 뽑는 부분
    if len(result) >= 5:
        pushAll(result)
        return
    for i in range(4):
        result.append(i)
        solution()
        result.pop()

if __name__ == "__main__":
    dx = (-1, 1, 0, 0) # 상하좌우
    dy = (0, 0, -1, 1)
    MAX = -1
    result = []
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    solution()
    print(MAX)