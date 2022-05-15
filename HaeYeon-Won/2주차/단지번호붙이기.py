import heapq
def init(n,data):
    result = []
    for i in data:
        temp = []
        for j in i:
            temp.append(int(j))
        result.append(temp)
    return result

def solution(size,mtrx, r,c,count):
    global result
    if (0<=r<size and 0<=c<size): 
        if mtrx[r][c]==1:
            result+=1
            mtrx[r][c]=count
            solution(size, mtrx, r+1, c, count)
            solution(size, mtrx, r-1, c, count)
            solution(size, mtrx, r, c+1, count)
            solution(size, mtrx, r, c-1, count)
        else:
            return
    else:
        return

if __name__ =="__main__":
    n = int(input())
    data = [input() for _ in range(n)]
    mtrx = init(n ,data)
    count = 2
    ans = []
    for r in range(n):
        for c in range(n):
            if mtrx[r][c]==1:
                result = 0
                solution(n,mtrx,r,c, count)
                heapq.heappush(ans, result)
                count+=1
    print(count-2) #중복 방지를 위해 처음 단지 번호의 시작을 2로 설정했기때문, 마지막에 들어가고나서 +1 더해서
    if len(ans)!=0:
        while ans:
            print(heapq.heappop(ans))
"""
문제 
- 1은단지, 0은 구분, 총 단지번호, 단지수 오름차순 출력
- https://www.acmicpc.net/problem/2667
- 실버 1
문제 유형 
- DFS / BFS : 깊이를 더해가며 진행하는 방식, 갈수 있는 방향으로 쭉가면 되서 위와같이 선정
자료구조 
- 2차원 리스트 : map 정보를 담기위해 사용
- heapq : 출력 시 단지수를 오름차순 정렬순으로 출력해야하기때문에 사용
 
사용한 아이디어
- mtrx값이 1인 경우 단지이므로 방문
- 처음 시작 단지번호를 1로 설정하면 무한으로 돌기때문에 단지번호는 2번 부터 시작
- DFS 진행 시 조건에 부합한다면 단지수 + 1
- 함수 탈출 후 산출된 단지수를 heapq에 push
"""
