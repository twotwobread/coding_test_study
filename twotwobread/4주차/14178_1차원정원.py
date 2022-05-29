

T = int(input())
for t in range(T):
    N, D = map(int, input().split())
    x = (N // (D*2+1))
    if (x*(D*2+1)) < N:
        x += 1
    print("#{} {}".format(t+1, x))
