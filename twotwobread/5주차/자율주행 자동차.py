# < 자율주행 자동차 >
# 문제 유형 : 시뮬레이션
# 자료 구조 : 2차원 리스트 - 자동차가 움직이는 도로의 정보
#           dx, dy (튜플) - 4방향으로 이동을 위함.
# [ 아이디어 ]
# - 방문한 곳과 인도를 똑같이 1로 둬도 괜찮음. -> 똑같이 여기기 때문에
# - 크기가 50x50까지 가능함. -> 최적의 경우를 찾는게 아니라 그냥 시뮬 진행해서 단순 구현으로 시간초과 x
# [ 구현 순서 ]
# 1. 먼저 맵 정보를 받는다.
# 2. 이를 이용해서 현재 방향을 기준으로 왼쪽 방향을 확인.
#    - 즉 시계 반대 방향으로 돌면서 확인해야하고 맨처음부터 방향을 돌리고 나서 확인해야함.
# 3. 이를 다 진행하면서 개수를 세서 방문 면적 구하기.

def move(row, col, direct, num):
    if road[row][col] == 0:
        road[row][col] = 2
    for i in range(1,5):
        next_d = (direct - i) % 4
        adj_r, adj_c = row + dx[next_d], col + dy[next_d]
        if 0<=adj_r<n and 0<=adj_c<m and road[adj_r][adj_c] == 0:
            return move(adj_r, adj_c, next_d, num+1)
    adj_r, adj_c = row + dx[(direct-2)%4], col + dy[(direct-2)%4]
    if 0<=adj_r<n and 0<=adj_c<m and road[adj_r][adj_c] != 1:
        return move(adj_r, adj_c, direct, num)
    return num
def solution():
    return move(x, y, d, 1)

if __name__ == "__main__":
    dx = (-1, 0, 1, 0) # 북, 동, 남 ,서
    dy = (0, 1, 0, -1)
    n, m = map(int, input().split())
    x, y, d = map(int, input().split())
    road = [list(map(int, input().split())) for _ in range(n)]
    print(solution())