T = int(input())
for t in range(T):
    game = input()
    if (15 - len(game)) + game.count('o') >= 8:
        print("#{} YES".format(t+1))
    else:
        print("#{} NO".format(t + 1))