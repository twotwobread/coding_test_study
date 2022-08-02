"""
문제
- 파일 크기가 주어질때, 이 파일들을 하나의 파일로 함치 때 필요한 최소비용 계산
문제 유형
- 자료구조
자료구조
- heap : 항상 최소값을 뽑아올 수 있게 헤줌
사용한 아이디어
- heap que는 항상 정렬된 상태를 보장해줌.
- 파일을 합칠때 가장 비용의 파일끼리 합치는것이 최소 비용
"""
import heapq
from collections import deque
def check(page1, page2, pages):
    LeftPage, RightPage = min(page1, page2), max(page1, page2)
    if LeftPage+1==RightPage:
        return True
    elif pages[LeftPage:RightPage+1].count(1)==2: #두 페이지 사이가 이미 다 연결되어 있는 경우
        return True
    else:
        return False

def solution(n,data):
    result = 0
    pages = [1 for _ in range(n)]
    temp_q = deque()
    while len(data)!=1:
        cost1, idx1 = heapq.heappop(data)
        while data:
            cost2, idx2 = heapq.heappop(data)
            if check(idx1, idx2, pages):
                pages[idx2]=0 #뒤에 뽑아온건 연결된걸로 설정
                total_cost = cost1+cost2
                heapq.heappush(data, (total_cost, idx1))
                result+=total_cost
                break
            else:
                temp_q.append((cost2, idx2))
        while temp_q:
            heapq.heappush(data, temp_q.popleft())
    return result

if __name__ =="__main__":
    T=int(input())
    for _ in range(T):
        n = int(input())
        data = list(map(int, input().split()))
        heap = []
        for i in range(n):
            heapq.heappush(heap,(data[i], i))
        print(solution(n,heap))