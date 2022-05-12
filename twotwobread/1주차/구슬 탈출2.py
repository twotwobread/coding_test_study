# nxm
# 가장 바깥 행과 열은 모두 막힘, 보드엔 구멍 하나
# 빨간 구슬을 구멍을 통해 빼는 것. 파란 구슬 구멍에 들어가면 안됨.
# 왼, 오, 위, 아래 기울이기 가능
# 빨간 구슬이 빠지면 성공, 파란색 빠지면 실패
# 동시에 빠져도 실패
# 두 구슬 같은 칸에 동시에 불가
# 더 이상 구슬이 움직이지 않을 때까지 기울이기
# 최소 몇번만에 빨간색 뺼 수 있을까
# 10번 이하로 뺼 수 없으면 -1 출력
# # = 장애물, O = 구멍, . = 빈칸
# < 구슬 탈출 2 >
# 문제 유형 : DFS/BFS 중 DFS - 한쪽으로 기울이면 쭉 들어가야함.
# 자료구조 : 2차원 배열 - 보드를 나타내기 좋고 pop(index)가 느린데 그걸 하는 부분도 없을
#                      것이라 예상.
#          check 2차원 배열 - 구슬 이동 시에 이동했던 좌표를 알기 위해서 이를 사용
# 1. 상하좌우 벽이 없고 다른 색 구슬이 없는 경우. 즉, 빈칸이 있는 경우나 구슬이 있는 경우 이동
# 2. 한번 이동 시에 쭉 이동하고 거기서 다른 방향으로 확인해야함.( 쭉 이동 시 횟수 하나 증가 )
# 3. 다른 방향이 있다면 그쪽으로 이동. 만약 벽을 만났을때 check 값이 1인 좌표 외에 갈 곳이
#    없다면 return 해야함.
# 4. 만약 빨간 구슬이 이동 가능한 방향이 없다면 파란 구슬이 이동가능한 곳을 확인
# 상하좌우
def wall(r, c):
    if board[r][c] == "#":
        return True
    else:
        return False
dx = (-1, 0, 1, 0) # 북 동 남 서
dy = (0, 1, 0, -1)
count = 0; min_value = 1e9;
def route(rr, rc, br, bc, r_check, b_check, goal, direct):
    global count, min_value
    if (br, bc) == goal or count > 10:
        b_check[br][bc] = 1
        return
    if (rr, rc) == goal:
        row, col = br, bc
        for i in range(10):
            nxt_r, nxt_c = row + dx[direct], col + dy[direct]
            if nxt_r < 0 or nxt_c < 0 or nxt_r > n or nxt_c > m:
                break
            if (nxt_r, nxt_c) == goal:
                return
            row, col = nxt_r, nxt_c

        if min_value > count:
            min_value = count
        return

    r_check[rr][rc] = 1
    b_check[br][bc] = 1
    nrr, nrc = rr + dx[direct], rc + dy[direct]
    nbr, nbc = br + dx[direct], bc + dy[direct]
    if direct == -1 or ((board[nrr][nrc] == '#' or (nrr, nrc) == (br, bc)) and (board[nbr][nbc] == '#' or (nbr, nbc) == (rr, rc))): # 한 방햑에서의 끝까지 간 경우
        count += 1
        temp = direct
        for i in range(4):
            direct = (direct+1) % 4
            nrr, nrc = rr + dx[direct], rc + dy[direct]
            nbr, nbc = br + dx[direct], bc + dy[direct]
            if (board[nrr][nrc] != '#' and (nrr, nrc) != (br, bc) and r_check[nrr][nrc] != 1):
                if wall(nrr, nrc): nrr, nrc = rr, rc
                if wall(nbr, nbc): nbr, nbc = br, bc
                route(nrr, nrc, nbr, nbc, r_check, b_check, goal, direct)
        direct = temp
        for i in range(4):
            direct = (direct + 1) % 4
            nrr, nrc = rr + dx[direct], rc + dy[direct]
            nbr, nbc = br + dx[direct], bc + dy[direct]
            if (board[nbr][nbc] != '#' and (nbr, nbc) != (rr, rc) and b_check[nbr][nbc] != 1):  # 새로운 방향으로 파란색 혹은 빨간색 구슬이 이동가능한 경우
                if wall(nrr, nrc): nrr, nrc = rr, rc
                if wall(nbr, nbc): nbr, nbc = br, bc
                route(nrr, nrc, nbr, nbc, r_check, b_check, goal, direct)
    else: # 한 방향의 끝까지 가지 않은 경우
        if wall(nrr, nrc): nrr, nrc = rr, rc
        if wall(nbr, nbc): nbr, nbc = br, bc
        route(nrr, nrc, nbr, nbc, r_check, b_check, goal, direct)
    count -= 1
    return


def solution(n, m, board):
    # 초기화 부분 ( 빨간 공, 파란 공, 구멍의 위치 확인 )
    r_check = [[0]*m for _ in range(n)]
    b_check = [[0]*m for _ in range(n)]
    route(pos["RED"][0], pos["RED"][1], pos["BLUE"][0], pos["BLUE"][1], r_check, b_check, pos["HOLE"], -1)
    return min_value


if __name__ == "__main__":
    n, m = map(int, input().split(" "))
    board = [list(input()) for _ in range(n)]
    pos = dict()
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                pos["RED"] = (i, j)
            elif board[i][j] == 'B':
                pos["BLUE"] = (i, j)
            elif board[i][j] == 'O':
                pos["HOLE"] = (i, j)
    result = solution(n, m, board)
    if result == 1e9:
        print(-1)
    else:
        print(result)


    # for i in range(4):
    #     new_direct = (direct + i) % 4
    #     nxt_rr, nxt_rc = red_r + dx[new_direct], red_c + dy[new_direct]
    #     nxt_br, nxt_bc = blue_r + dx[new_direct], blue_c + dy[new_direct]
    #     if ((nxt_rr, nxt_rc)!=(blue_r, blue_c) and board[nxt_rr][nxt_rc] != '#' and r_check[nxt_rr][nxt_rc] != 1) or \
    #             ((nxt_br, nxt_bc)!=(red_r, red_c) and board[nxt_br][nxt_bc] != '#' and b_check[nxt_br][nxt_bc] != 1):
    #         if wall(nxt_rr, nxt_rc):
    #             nxt_rr, nxt_rc = red_r, red_c
    #         if wall(nxt_br, nxt_bc):
    #             nxt_br, nxt_bc = blue_r, blue_c
    #         r_check[nxt_rr][nxt_rc] = 1
    #         b_check[nxt_br][nxt_bc] = 1
    #         if direct != new_direct:
    #             count += 1
    #         temp, direct = direct, new_direct
    #         route(nxt_rr, nxt_rc, nxt_br, nxt_bc, r_check, b_check, goal)
    #         if temp != direct:
    #             count -= 1
    #         direct = temp
    #         if not (nxt_rr == red_r and nxt_rc == red_c):
    #             r_check[nxt_rr][nxt_rc] = 0
    #         if not (nxt_br == blue_r and nxt_bc == blue_c):
    #             b_check[nxt_br][nxt_bc] = 0
    # return

# 8 8
# ########
# ########
# #####B##
# ####.R.#
# ######.#
# #####O.#
# ######.#
# ########

# 출력 : -1
# 정답 : 7  - 왼, 아래, 오, 아래, 오, 아래 , 왼
# 다시 처음부터 생각해볼것