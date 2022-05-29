
def solution(num, length):
    max_value = 0
    for i in range(length): max_value += num[i] * (10 ** ((length-1) - i))
    min_value = max_value
    copy_num = num.copy()
    for i in range(0, length-1):
        for j in range(i+1,length):
            if (i==0 and num[j]==0):
                continue
            if num[i] != num[j]:
                num[i], num[j] = num[j], num[i]
                compare = 0
                for k in range(length): compare += num[k] * (10 ** ((length - 1) - k))
                if max_value < compare:
                    max_value = compare
                if min_value > compare:
                    min_value = compare
                num = copy_num.copy()
    return min_value, max_value

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        num = list(map(int, input()))
        MIN, MAX = solution(num, len(num))
        print("#{} {} {}".format(t+1, MIN, MAX))