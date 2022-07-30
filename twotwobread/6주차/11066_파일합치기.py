# 각 챕터 -> 각각 다른 파일에 저장 -> 파일 합쳐서 최종적 완성본 한 개 파일
# 두 개 파일 -> 하나의 임시 파일, 임시 파일 혹은 원래 파일을 두개씩 합침.
# 두 개 파일을 합치는데 필요한 비용 -> 두 파일의 크기 합
# 최종적 한 개 파일을 환성하는데 필요한 비용의 총합 계산. -> 최소비용

# 챕터 갯수 K 는 최대 500, 파일 크기 10,000 이하
# O(N^2)의 연산 수행이 필요하다고 생각 -> 500 * 500 = 250,000
# 문제에서 요구하는 것은 챕터들을 두개씩 합쳐서 하나의 파일로 합칠때 필요한 최소비용을 계산하는 것이다.
# 이것은 최적화 문제이다. 브루트 포스로 단순히 생각하면 N개 중 2개를 뽑고 다음은 N-1개 중 2개를 뽑는 형식으로
# 진행되고 nC2 => n^2 이다. 이것이 N동안 반복되니까 대략 O(n^3) 정도의 시간 복잡도가 요구되고 N의 최대 값은 500이다. -> 대략 1억이 넘기 때문에 줄일 필요가 있다.
# 그렇다면 어떤 식으로 접근하는게 좋을까? 40, 30, 30, 60 이 예시로 만들 수 있는 경우는 어떤 것들이 있을까?
    # 1. (((40 + 30) + 30) + 60)
    # 2. ((40+30) + (30+ 60))
    # 3. ((40 + (30 + 30)) + 60)
    # 4. (40 + (30 + (30 + 60)))
# 위는 일부의 경우만 적었지만 저것 이외에도 다른 경우들이 존재하고 숫자의 갯수들이 많아지면 셀 수 없이 많아질 것을 예상할 수 있다.
# 그리고 위의 부분에서 (40 + 30) 을 더하는 과정은 1, 2 경우에서 겹치고 (30 + 60)을 더하는 과정은 2, 4번에서 겹치는 것을 확인할 수 있다.
# 중복되는 연산을 줄이는 방법으로 시간적인 효율성을 높이기 위해서 DP를 이용하는 방법을 생각해보자.
# 먼저 중복되는 연산을 생각해보자. A B C D 가 있다고 하면 여기에서 A와 마지막 D를 합치는 경우는 무엇이 있을까?
    # 1. A부터 C까지 더하고 D를 더하는 방법
    # 2. A+B랑 C+D를 더하는 방법
    # 3. B부터 D까지 더하고 A를 더하는 방법
# 크게 이렇게 생각해볼 수 있다. A부터 C까지 더하거나 B부터 D까지 더하는 것은 알아서 최적의 경우로 더한다고 생각하고 4개의 길이의 관점에선 이렇게 생각해 볼 수 있다.
# 이것을 식으로 표현하면 merge(start, end) = min( merge(start, start+1) + merge(start+1, end), merge(start, start+2) + merge(start+2, end), ...... )
# 이렇게 생각할 수 있고 내부의 작은 부분 문제들의 합이 memorization되어 있다면 중복연산을 줄일 수 있다고 생각한다.
# 이런 방법으로 탑다운을 할 수 있고 바텀업을 생각해보자.

# 바텀업은 작은 부분문제에서 큰 문제로 올라가야한다. 그렇다면 여기서 가장 작은 문제는 무엇일까?
# 파일개수가 하나라서 하나의 파일만 존재하는 경우이다. 그 경우엔 뭔가 연산을 할 필요가 없다.
# 그럼 조금 더 큰 경우를 생각해보자. 파일개수가 2개인 경우는 어떻게 하면 좋을까? 두 파일을 더하면 된다.
# 이를 이용해서 먼저 table을 작성해보자. 두 파일을 더하는 것을 표현하기 위해서 2차원 배열로 생성하겠다.
#   A B     C       D               => 같은 파일을 더하는 경우는 하나의 파일이 있는 경우를 의미하기 위해서 비용을 0으로 설정한다.
# A 0 AB    AB+ABC  (AB+CD)+ABCD    => 먼저 AB를 살펴보자. 얼마일까? 아까 2개의 파일을 더할 땐 AB를 더하면 된다고 했다. 좀 더 풀어보면 AA + AB인 것이다.
                                        # => 다음 AC는 얼마일까? 이 경우를 생각하면 A, B, C를 더하는 것과 같다. A+B와 B+C 중에 최소값과 A+B + ABC를 하면 된다.
                                            # => 그 다음 AD는 얼마일까? A B C D 를 구하면 된다. 크게 생각해서 A+B+C, (A+B)+(C+D), (B+C+D)의 최소값을 생각하면 된다.
# B   0     BC      BC+BCD      => 다음 BC는 얼마일까? 인접하기 때문에 역시 BC라고 넣으면 될 것같다.
                                    # => BD는 얼마일까? B C D를 합치는 것으로 B+C , C+D 중의 최소값을 생각하면 될 것 같다.
# C         0       CD          => CD도 마찬가지 이다.
# D                 0

# 위를 생각해서 탑다운과 바텀업 방식을 구현해보자.
# 먼저 탑다운 방식부터 구현해보겠다.
def fileMerge(start, end):
    if start == end:
        return 0
    if memo.get((start, end), 0):
        return memo[(start, end)]
    else:
        memo[(start, end)] = INF
        for i in range(end - start):
            left = fileMerge(start, start+i)
            right = fileMerge(start + i + 1, end)
            memo[(start, end)] = min(memo[(start, end)], left+right + sum(file[start:end+1])) # 누적합을 더해야함.
        return memo[(start, end)]

if __name__ == "__main__":
    INF = int(1e9)
    T = int(input())
    for t in range(T):
        memo = dict()
        K = int(input())
        file = list(map(int, input().split()))
        print(fileMerge(0, len(file) - 1))


# 바텀업 방식 구현
def tabulation():
    #dp = [ [file[i] if i == j else 0 for i in range(K)] for j in range(K)]
    dp = [[0]*K for _ in range(K)]
    print(dp)
    for j in range(1, K): # 열이 바뀜 -> 마지막에 [start][end]가 나와야함.
        for i in range(j-1, -1, -1): # 행은 큰 값부터 들어가야함.
            cost = INF
            for k in range(j-i):
                cost = min(cost, dp[i][i+k] + dp[i+k+1][j])
            dp[i][j] = cost + sum(file[i:j+1])
    print(dp)
    return dp[0][K-1]

if __name__ == "__main__":
    INF = int(1e9)
    T = int(input())
    for t in range(T):
        K = int(input())
        file = list(map(int, input().split()))
        print(tabulation())



