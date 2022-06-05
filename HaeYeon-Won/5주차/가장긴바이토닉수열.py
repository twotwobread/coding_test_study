"""
문제
- 수열 S가 어떤 수 Sk를 기준으로 S1 < S2 < ... Sk-1 < Sk > Sk+1 > ... SN-1 > SN을 만족 => 바이토닉 수열
- 예를 들어, {10, 20, 30, 25, 20}과 {10, 20, 30, 40}, {50, 40, 25, 10} 은 바이토닉 수열
- 가장 큰 바이토닉 수열은?
문제 유형
- 백트래킹
자료구조
- 2차원 리스트 : 기존값 저장, 갱신값 저장에 사용
- deque : 해당 round에서 밀 수 있는 숫자의 위치를 담아옴
사용한 아이디어
- 모든 수에서 시작해 봐야함
- 일정 기점에서 오름차순을 내림차순으로 변경해 줘야함
- 시작점이 마지막에 왔다면 그거까지 처리하고 재귀 탈출하면 됨
"""
def binary_search(n, arr, target, INCR):
    start, end = 0, n-1
    while start<end:
        mid = (start+end)//2
        if INCR:
            if arr[mid]<target:
                start=mid+1
            else:
                end=mid #mid 포함 왼쪽 (target과 같은게 없을 때 큰수중 가장 작은값을 위해)
        else:
            if arr[mid]>target:
                start=mid+1
            else:
                end=mid #mid 포함 왼쪽 (target과 같은게 없을 때 큰수중 가장 작은값을 위해)
    return end

def getLongest(n, data):
    result = []
    result.append(data[0])
    for i in range(1, n):
        if result[-1] < data[i]:
            result.append(data[i])
        else:
            idx = binary_search(len(result), result, data[i], True)  # 이분탐색하여 해당 숫자가 어디에 들어갈지 결정
            result[idx] = data[i]
    return result

def getShortest(n, data):
    result = []
    result.append(data[0])
    for i in range(1, n):
        if result[-1] > data[i]:
            result.append(data[i])
        else:
            idx = binary_search(len(result), result, data[i], False)  # 이분탐색하여 해당 숫자가 어디에 들어갈지 결정
            result[idx] = data[i]
    return result

def solution(n, data):
    longest = getLongest(n,data)
    shortest = getShortest(n ,data)
    print(longest)
    print(shortest)



if __name__=="__main__":
    n=int(input())
    data = list(map(int,input().split()))
    print(solution(n, data))
