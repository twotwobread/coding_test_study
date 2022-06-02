def solution(round, number):
    val = int("".join(number))
    maxVal, minVal = val, val
    length = len(number)
    if length==1:
        print("#{} {} {}".format(round, val, val))
        return
    for i in range(length-1):
        for j in range(i+1, length):
            temp = [x for x in number]
            temp[i], temp[j] = temp[j], temp[i]
            if temp[0]=='0':
                continue
            else:
                temp = "".join(temp)
                val = int(temp)
                if val>maxVal: maxVal = val
                if val<minVal: minVal = val
    print("#{} {} {}".format(round, minVal, maxVal))
    return
if __name__ == "__main__":
    T = int(input())
    for i in range(1,T+1):
        number = input()
        solution(i, list(number))

"""
최대 9자리수 ->8+7+6+5+4+3+2+1 => 비교횟수 최대 36
"""