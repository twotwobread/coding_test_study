# <교환학생>
# 수업 어떤 요일도 열리지 않는 경우 x
# n일 동안 수업 -> 목표를 이루기 위한 최소 일수 출력
# 최소 1 ~ 100000
# 문제유형 : 구현
#
def solution():
    minValue = 1e9
    for w in range(7):
        if week[w] == 1:
            sumValue = 1
            start = 1
            i = (w+1) % 7
            while True:
                if sumValue == n:
                    break
                if week[i] == 1:
                    sumValue += 1
                start += 1
                i = (i + 1) % 7
            if minValue > start:
                minValue = start
    return minValue

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        n = int(input())
        week = list(map(int, input().split()))
        print("#{} {}".format(t+1, solution()))