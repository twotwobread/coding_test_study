'''
Project: 백준_17298
Date: 2022.07.31.
Content: DP
- A 수열의 수를 하나씩 q에 넣는다.
- 넣는 수보다 오른쪽의 수가 더 크면 그건 오큰수이므로 그걸 오큰수로 지정한다.
- q에 넣어진 수를 순서대로 확인하며 찾은 오큰수로 지정할 수 있는 것들을 결정한다.
'''


from collections import deque


def solution():
    NGE = [-1 for _ in range(n)]    # 일단 모든 값은 -1로 초기화
    q = deque()
    for i in range(1, n):
        q.append((map_A[i-1], i-1)) # 이전 값이랑 이전 위치 저장 (오른쪽 값이 더 클 때까지)
        if map_A[i - 1] < map_A[i]: # 오른쪽 값이 더 크면
            num = map_A[i]  # 그게 오큰수
            while q:
                if q[-1][0] < num:  # 찾은 오큰수로 q에서 뺄 수 있는거 다 빼서
                    NGE[q.pop()[1]] = num   # 그걸 오큰수로 채우기
                else:   # 근데 찾은 오큰수보다 q에 들어있는 게 더 크면 그건 오큰수 해당 안되니까
                    break   # 그만하고 나가기
    print(*NGE)


if __name__ == "__main__":
    n = int(input())
    map_A = list(map(int, input().split()))
    solution()
