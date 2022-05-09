# n+1일 쨰 퇴사
# 하루에 하나씩 서로 다른 사람의 상담을 잡아놓음.
# 상담 완료 기간 = T, 완료시 받는 금액 = P
# N의 크기가 작기 때문에 백트래킹도 가능

# < 퇴사 >
# 문제 유형 : DP, 백트래킹
# 자료 구조 : 2차원 리스트 - 1일부터 7일의 정보를 담기 위해 사용
#           총 합을 담기 위한 변수 - 이를 이용해서 최대 총합을 구할 예정
# 1. 백트래킹을 이용해서 자기 일수에 T를 더했을 때 N을 넘지 않는 경우 값을 담음.
# 2. 재귀를 돌릴때 시작하는 index를 T를 더한 곳부터 시작하게 함.
# 3. 시작 index가 7을 넘으면 총합을 구하고 최대를 구함.

# - 재귀 이용 : 풀이시간 ( 15분 )
def sumConsult(start, n, consult):
    global max, result
    for i in range(start, n):
        if (i + consult[i][0] - 1) < n:
            result += consult[i][1]
            sumConsult(i+consult[i][0], n, consult)
            result -= consult[i][1]
    if max < result:
        max = result
    return
def solution(n, consult):
    index = 0
    sumConsult(index, n, consult)
    return max
##########################################################

# - DP 이용



if __name__ == "__main__":
    max = -1; result = 0
    n = int(input())
    consult = [list(map(int, input().split(" "))) for _ in range(n)]
    print(solution(n, consult))