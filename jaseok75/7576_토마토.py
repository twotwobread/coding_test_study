"""
Project: 백준_7576_토마토
Date: 2022.05.03.화
Comment:
- 문제유형: BFS
- 익은 토마토 주변을 탐색하면서 진행
- 토마토 박스 자체를 익는 데에 걸린 시간을 체크하는 용도로 함께 사용함
- 2차원 리스트(미로 배열 tomato_box): 토마토 박스의 값을 확인하고 변경하는 용도.
  pop이나 append 등의 연산을 자주 하지 않고, 값 변경이 가능해야 해서 사용함
- deque(위치 q): 익은 토마토의 위치를 저장하고, 주변을 탐색할 위치 인덱스로 사용
  잦은 pop과 append가 사용되어야 하기 때문에 속도를 위해 사용함
  
1. 먼저 전체 토마토 박스 중 익은 토마토의 위치를 q에 저장
2. q가 비었다면 토마토가 익을 수 없는 상황이므로 -1을 출력하고 종료
3. 저장된 익은 토마토를 하나씩 빼서 주변의 익지 않은 토마토 확인
4. 익지 않은 토마토가 있다면 현재 위치의 값 (현재까지 익은 데에 걸린 날짜) + 1의 값을 삽입
5. 모든 과정을 끝낸 후에 tomato_box에 익지 않은 토마토가 있다면 -1 출력
6. 전체 토마토가 익은 데에 걸린 날짜는 tomato_box의 max 값 - 1이다.
7. 익을 토마토가 없었다면 4번 과정이 없었기 때문에 tomato_box의 최댓값은 1이므로 0을
   출력하게 됨.
"""

from collections import deque


def solution():
    q = deque((i, j) for i in range(n) for j in range(m) if tomato_box[i][j] == 1)  # 익은 토마토의 위치만 저장
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    if not q:
        print("-1")
        return

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and tomato_box[nx][ny] == 0:
                tomato_box[nx][ny] = tomato_box[x][y] + 1
                q.append((nx, ny))

    result = [1 for i in range(n) for j in range(m) if tomato_box[i][j] == 0]
    if result:
        print('-1')
    else:
        print(max(map(max, tomato_box)) - 1)    # 2차원 배열의 max값 확인


if __name__ == "__main__":
    m, n = map(int, input().split())
    tomato_box = [list(map(int, input().split())) for _ in range(n)]

    solution()