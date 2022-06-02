def solution(n,d):
    d = d*2+1
    result = n//d
    if n%d!=0:
        result+=1
    return result

if __name__ == '__main__':
    numCase = int(input())
    for i in range(1,numCase+1):
        n, d = map(int, input().split())
        val = solution(n,d)
        print("#{} {}".format(i, val))