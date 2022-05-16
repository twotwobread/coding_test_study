# 이전에 k광년 이동시 k-1, k, k+1 이동 가능
# 처음엔 -1, 0, 1 이지만 0, -1은 의미가 없어 1로만 이동가능
# x, y 까지 최소 작동 횟수로 이동하려 함.
# y 도착하기 바로 직전의 이동거리는 반드시 1 광년 이동.
# < Fly me to the Alpha Centauri >
# 문제 유형 : DP -> 아닌거 같음.
# 계속 생각을 해봤는데 아닌 이유는 최대 거리가 2^31-1까지가 나올 수 있는데
# 이 크기의 리스트를 만든다고 가정하면 2^31 * 4 바이트 크기임
# 이는 8,589,934,592 바이트 이고 이는 대략 8600MB -> 무조건 터짐.
# 그래서 이 문제에서 중요한 건 거리라고 생각함.
# 마지막에 반드시 1 광년 이동하는데 이를 위해선 이전에 2, 1, 0 광년의 이동을 해야함.
# 생각해서 규칙을 찾아보자.
# def solution():
#     for t in range(T):
#         start, end = info[t]
#         dist = end - start
#         if dist == 1 or dist == 2:
#             print(dist)
#             continue
#         else:
#             dst = 3
#             lng = 2
#             cnt = 0
#             for i in range(3, dist+1):
#                 if i == (lng+1)**2 - lng:
#                     lng += 1
#                 cnt += 1
#                 if dist == i:
#                     print(dst)
#                     break
#                 if cnt == lng:
#                     dst += 1
#                     cnt = 0
# 2^31 만큼 반복문을 돌리니까 당연히 시간초과가 나지
def solution():
    for t in range(T):
        start, end = info[t]
        dist = end - start
        if dist == 1 or dist == 2:
            print(dist)
            continue
        before = 1gi
        for i in range(2, 47000): # 2^31의 루트 값이 46340 좀 넘으니까
            if (i*i) >= dist:
                if (i*i) - before <= dist:
                    print(i+before)
                else:
                    print(i+before-1)
                break
            before = i

if __name__ == "__main__":
    T = int(input())
    info = [list(map(int, input().split())) for _ in range(T)]
    solution()