if __name__=="__main__":
    T = int(input())
    for i in range(1, T+1):
        data = list(map(int, input().split()))
        result = min(data[1], data[3])-max(data[0], data[2])
        if result:
            print("#{} {}".format(i, result))
        else:
            print("#{} {}".format(i, 0))