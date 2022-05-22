def check(new, queen):
    #놓을 수 없는 위치에 있다면?
    #같은 행은 애초에 밑에서 걸러짐
    for i in range(new[0]): #지금까지 진행한 행 확인
        if new[1]==queen[i] or abs(new[0]-i)==abs(new[1]-queen[i]):
            return False
    return True


def solution(n, depth, queen):
    global result
    if depth==n:
        result+=1
        return
    for col in range(n):
        if not check((depth,col), queen):
            continue
        queen[depth]=col
        solution(n,depth+1, queen)

if __name__ =="__main__":
    n=int(input())
    queen = [-1 for _ in range(n)]
    result = 0
    solution(n,0, queen)
    print(result)
"""
문제 
- N*N 체스판 위 N개의 퀸이 서로 공격할 수 없게 놓는 문제
문제 유형 
- 백트레킹
자료구조 
- 리스트 : 퀸의 위치 저장
사용한 아이디어
- 0행 0열 부터 N행 N열까지 차례대로 퀸을 놓는다
- 여기서 1차원 리스트의 인덱스는 행, 값은 열을 의미
- 만약 같은 행에 이미 퀸이 있다면 다음 행으로
- 만약 같은 행에 이미 퀸이 있다면 다음 열로
- 만약 대각선 상에 퀸이 있다면 열을 한개씩 더해준다
- 이렇게 진행하다 재귀의 깊이가 체스판과 동일 해지면 result+1
"""
