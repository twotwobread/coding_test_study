"""
문제
- 오른쪽에 있으면서 큰수 중 인덱스 번호가 가장 낮은수를 고르는 문제
문제 유형
- 큐
자료구조
- deque : 배열에서 하나씩 뽑아온 원소를 담아줌
사용한 아이디어
- 돌맹이 쌓는 느낌
- 원래 제일 위에 있던것 보다 무거운걸 놓으면 지금 올려놓은거 보다 무거운거 나올때 까지 부수면서 내려감
- 만약 큐에 남은 값이 4,3,2 이고 들어온 값이 2라 했을때 
- 어차피 젤 뒤에거 보다 작으면 앞에것도 못나가니까 break
"""
from collections import deque
def solution(n, data):
    result = [-1 for _ in range(n)]
    extracted = deque([0]) #현재 큐 밖으로 나온 원소
    for i in range(1,n):
        while extracted:
            now = extracted.pop()
            if data[now]<data[i]: 
                # 돌맹이 쌓는 느낌
                # 원래 제일 위에 있던것 보다 무거운걸 놓으면 지금 올려놓은거 보다 무거운거 나올때 까지 부수면서 내려감
                # 만약 큐에 남은 값이 4,3,2 이고 들어온 값이 2라 했을때 
                #어차피 젤 뒤에거 보다 작으면 앞에것도 못나가니까 break
                result[now] = data[i]
            else:
                extracted.append(now)
                break
        extracted.append(i)
    print(" ".join(str(s) for s in result))
         
if __name__ =="__main__":
    n = int(input())
    data = list(map(int, input().split()))
    solution(n,data)