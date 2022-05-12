# < n_queen >
# 문제유형 : 백트래킹
# 자료구조 : 1차원 리스트 - 퀸이 담기는 좌표를 저장해놓기 위함.
# 1. 먼저 퀸은 무조건 한 행에 하나씩 담긴다. 그래서 행을 인수로써 함수를 구성한다.
# 2. 한 행에서 퀸을 잡고 그 다음 행에서 퀸을 넣는데 자신의 퀸의 범위내에 다른 퀸이 오지
#    않는다면 들어가도 괜찮은 자리가 된다.
# 3. 그렇게 퀸의 좌표를 넣다가 좌표가 n개가 되면 카운트를 증가시킨다.
# 풀이시간 : 1시간 - 시간 초과문제 해결에 시간을 많이 쏟음.
def n_queen(i):
    global count
    if len(result) == n:
        count += 1
        return
    for j in range(n):
        for k in result:
            if (k[0] == i or k[1] == j or (abs(k[0] - i) == abs(k[1] - j))):
                break
        else:
            result.append((i, j))
            n_queen(i + 1)
            result.pop()
    return

if __name__ == "__main__":
    result = []
    count = 0
    n = int(input())
    n_queen(0)
    print(count)
