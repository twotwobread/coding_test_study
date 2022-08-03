def check(now, data):
    count = 0
    for i in range(now[1], n):
        if data[now[0]][i]!='#':
            break
        count+=1

    for i in range(now[0],now[0]+count):
        for j in range(now[1], now[1]+count):
            if data[i][j]=='#':
                data[i][j]='.'
            else:
                return False
    return True

def solution(round,n,data):
    flag = False
    for i in range(n):
        for j in range(n):
            if data[i][j]=="#":
                if flag:
                    print("#{} no".format(round))
                    return
                else:
                    if not check((i,j), data):
                        print("#{} no".format(round))
                        return
                    flag = True

    print("#{} yes".format(round))

if __name__ == '__main__':
    numCase = int(input())
    for i in range(1,numCase+1):
        n = int(input())
        data = [list(input()) for _ in range(n)]
        solution(i, n,data)
