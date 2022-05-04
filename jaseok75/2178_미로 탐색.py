"""
Project: 백준_2178_미로 탐색
Date: 2022.05.03.화
Comment:
- 문제유형: BFS
- 미로를 따라 한 칸씩 진행하면서 주변을 확인하며 진행
- 2차원 리스트(미로 배열 miro): 미로 배열 자체에서 거리값을 누적해서 변경하고
  따로 pop이나 append 등의 연산을 필요로 하지 않음
- deque(위치 q): 미로를 따라가면서 현재 위치에 대한 정보를 저장하고, 꺼내면서
  사용하기 때문에 반복되는 pop과 append 연산의 시간을 단축하기 위해 list 대신 deque 사용
  
1. 첫 번째 위치 q에 담고 BFS 시작
2. 인접한 4방향에서 미로의 길이 있다면 (1) 현재 위치의 정보(누적 거리)에서 1 더한 값으로 변경
   후 현재 위치 정보 q에 담기
3. 마지막 위치에 대한 값은 출발점부터 목적지까지의 거리
"""

from collections import deque


def solution():
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]  # 북 동 남 서
    q = deque()
    q.append((0, 0))    # 시작점은 무조건 (0, 0)

    # 4방향 확인하면서 갈 수 있는 길이라면(1 이라면) 거리 계산하고 위치 추가하기
    while q:
        x, y = q.popleft()  # 현재 위치
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]  # 4방향으로 길이 있는지 확인하기 위해 새로운 위치
            if 0 <= nx < n and 0 <= ny < m and miro[nx][ny] == 1:   # 갈 수 있는 길이라면
                miro[nx][ny] = miro[x][y] + 1   # 누적 거리 계산하기
                q.append((nx, ny))  # 위치 추가하기
    return miro[n - 1][m - 1]   # 목적지의 누적 거리 반환


if __name__ == "__main__":
    n, m = map(int, input().split())
    miro = [list(map(int, input())) for _ in range(n)]
    print(solution())