# n x m
# 주사위 각 면 0이 쓰여져 있음.
# 칸에 쓰여진 수 = 0 -> 주사위 바닥 면 쓰여진 수 칸에 복사
# 주사위 수는 변하지 않음
# 칸에 쓰여진 수 != 0 -> 칸에 쓰여진 수 주사위 바닥에 복사. 해당 칸의 수 = 0
# 주사위 격자판 밖으로 이동 x.
# 주사위 초기 위치와 굴리는 방향이 주어질 때, 이동 시 정육면체의 상단 면에 쓰여진 숫자 출력
# < 정육면체 굴리기 >
# 문제유형 : 시뮬레이션
# 자료구조 : 2차원 리스트 - 맵의 정보를 얻고 이를 이용해 주사위를 굴리면서 주사위에 값을 복사
#                       혹의 주사위 값을 칸에 복사할 예정
#          2차원 리스트 - 주사위의 현재 각 면마다의 숫자 정보를 넣어놓을 예정.
# < 동작 순서 >
# 1. 맨 처음 주사위의 정보를 초기화 해놓는다. 처음은 0으로 다 초기화 된다.
# 2. 그 후 roll에 들어간 정보를 토대로 주사위를 굴리고 칸의 값이 0이면 주사위의 바닥면에
#    쓰여진 수가 칸에 복사된다.
# 3. 칸의 값이 0이 아니면 칸에 쓰여진 수가 정육면체 바닥면으로 복사되며, 해당 칸의 수는 0이
#    된다.
# 4. 전부 다 돌리고 나서 상단면에 존재하는 값을 출력하면 된다.
# < 아이디어 >
# -1 0 -1 -1
#  0 0  0  0
# -1 0 -1 -1
# 동서로 구를 땐 2행의 값들만 옆으로 밀고 당기고 구름에 따라 어떻게 값이 바뀌는지 정의
# 북남으로 이동할때도 dice 값들이 어떻게 바뀌는지 정의
def move(direct):
    if direct == 0: # 우
        dice[1][1], dice[1][0] = dice[1][0], dice[1][1]
        dice[1][1], dice[1][3] = dice[1][3], dice[1][1]
        dice[1][1], dice[1][2] = dice[1][2], dice[1][1]
    elif direct == 1: # 좌
        dice[1][1], dice[1][2] = dice[1][2], dice[1][1]
        dice[1][1], dice[1][3] = dice[1][3], dice[1][1]
        dice[1][1], dice[1][0] = dice[1][0], dice[1][1]
    elif direct == 2: # 위
        dice[0][1], dice[1][3] = dice[1][3], dice[0][1]
        dice[1][3], dice[1][1] = dice[1][1], dice[1][3]
        dice[1][3], dice[2][1] = dice[2][1], dice[1][3]
    elif direct == 3: # 아래
        dice[2][1], dice[1][3] = dice[1][3], dice[2][1]
        dice[1][3], dice[1][1] = dice[1][1], dice[1][3]
        dice[1][3], dice[0][1] = dice[0][1], dice[1][3]
def solution(x, y):
    for r in range(k):
        direct = roll[r] - 1
        nx, ny = x + dx[direct], y + dy[direct]
        if 0<=nx<n and 0<=ny<m:
            move(direct)
            if graph[nx][ny] == 0:
                graph[nx][ny] = dice[1][1]
            else:
                dice[1][1] = graph[nx][ny]
                graph[nx][ny] = 0
            print(dice[1][3])
            x, y = nx, ny

if __name__ == "__main__":
    dx = (0, 0, -1, 1) # 동서북남 0 ~ 3
    dy = (1, -1, 0, 0)
    dice = [[-1, 0, -1, -1], [0, 0, 0, 0], [-1, 0, -1, -1]]
    n, m, x, y, k = map(int, input().split())
    # 세로 x 가로, 주사위 초기 위치, 굴리기 횟수
    graph = [list(map(int, input().split())) for _ in range(n)]
    roll = list(map(int, input().split()))
    solution(x, y)
