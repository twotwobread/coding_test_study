# < 가장 긴 바이토닉 부분 수열 >
# 문제 유형 : DP
# 자료 구조 : 1차원 리스트 - 수열 저장을 위함.
#           1차원 리스트 - LIS, LDS 결과 값들을 저장하기 위함.
#
# [ 아이디어 ]
# - 수열의 크기가 1000까지 가능하기 때문에 백트래킹으론 풀 수 없음.
# - DP를 이용해서 풀어야하는 것을 확인.
# - 또 바이토닉 수열이 되어야함.
# - LIS(Longest Increasing Subsequence)를 이용해서 LIS를 구하고 그 젤 큰놈부터
#   LDS를 구하면 바이토닉이 되지 않을까? 생각함.
# - 그래서 처음엔 증가하는 부분 수열을 구하고 거기에서 연결되는 감소하는 부분 수열을 구한 길이를
#   더하고 수열을 거꾸로 뒤집고 증가하는 부분 수열을 구하고 거기에 똑같이 감소하는 부분수열을 구한
#   길이를 더한 값 중 더 큰 값을 출력했는데 이것은 정답이 아니었음.
# - 그래서 그럼 이 문제는 무조건 DP로 풀어야할 것 같다는 생각이 들었음.
# - 모든 자리에서 증가하는 부분수열이 몇인지를 알고 있으면 됨.
# - 생각해보면 기존에 lis을 구하는 방식이 매자리 지나가면서 더 크면 값을 추가해주고 lis를 늘리고
#   그게 아니면 자기의 위치를 찾을 때 이분 탐색을 이용함. 더 작으면 이분탐색을 통해서 같은 값이거나
#   가장 근접한 큰 수를 찾아서 그 값을 넣어줌 그렇게 하는 이유는 해당 숫자로부터 다시 증가하는
#   부분 수열이 이어질 수 있기 때문에 그럼. LCS 푸는 것과 유사함. 떨어져도 그 값을 계속 끌고 가는
#   의미임.
# - 그래서 매 자리 부분 수열을 구할 때, 그 값을 DP로 저장을 해줬음.
# - 그리고 어짜피 거꾸로 돌려서 증가하는 부분수열을 찾으면 감소하는 부분수열이 됨.
# - 이를이용해서 모든자리 감소하는 부분수열을 찾고 그 값을 더해줬음. 그 경우 최대 높은 값이
#   가장 긴 바이토닉 수열이 됨.

def binarySearch(data, left, right, goal): # 같거나 가장 근접한 큰 수를 찾기 위함.
    while left < right:
        mid = (left + right) // 2
        if data[mid] < goal:
            left = mid + 1
        else:
            right = mid
    return right
def solution():
    lis = [sequence[0]]
    DP = [1]*n
    for i in range(1, n):
        if lis[len(lis)-1] < sequence[i]:
            lis.append(sequence[i])
            DP[i] = len(lis)
        else:
            lis[binarySearch(lis, 0, len(lis)-1, sequence[i])] = sequence[i]
            DP[i] = len(lis)
    lis = [sequence[-1]]
    for i in range(n-2, -1, -1):
        if lis[len(lis)-1] < sequence[i]:
            lis.append(sequence[i])
            DP[i] += (len(lis) - 1)
        else:
            lis[binarySearch(lis, 0, len(lis)-1, sequence[i])] = sequence[i]
            DP[i] += (len(lis) - 1)
    print(max(DP))

if __name__ == "__main__":
    n = int(input())
    sequence = list(map(int, input().split()))
    solution()