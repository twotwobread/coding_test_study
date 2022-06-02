def solution(round, num):
    print("#{} {}".format(round, num//3))

if __name__=="__main__":
    T = int(input())
    for i in range(1, T+1):
        num = int(input())
        solution(i, num)