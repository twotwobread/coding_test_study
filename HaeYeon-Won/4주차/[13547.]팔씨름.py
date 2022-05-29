def solution(round, data):
    total = 15
    case = [0,0]
    length = len(data)
    for i in data:
        if i=='o': case[0]+=1
        else: case[1]+=1
    if total-length-(case[1]-case[0])>0:
        print("#{} {}".format(round, "YES"))
    else:
        print("#{} {}".format(round, "NO"))

if __name__ == '__main__':
    T = int(input())
    for i in range(1, T+1):
        data = input()
        solution(i, data)

"""

3
oxoxoxoxoxoxoxo
x
xxxxxxxxxxxx
"""