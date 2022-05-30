def solution():
    X, Y = 0, 0
    value = 0
    if light[1] <= light[2] or light[3] <= light[0]:
        return 0
    else:
        start = light[0] if light[0] >= light[2] else light[2]
        end = light[1] if light[1] <= light[3] else light[3]
        return end - start
if __name__ == "__main__":
    T = int(input())
    result = ""
    for t in range(T):
        light = list(map(int, input().split()))
        result += "#"+str(t+1)+" "+str(solution())+"\n"
    print(result)