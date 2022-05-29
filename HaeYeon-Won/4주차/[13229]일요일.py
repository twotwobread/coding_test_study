weekDays = {'SUN' : 7, 'SAT' : 1, 'FRI' : 2, 'THU' : 3, 'WED' : 4, 'TUE' : 5, 'MON' : 6}
if __name__ == '__main__':
    T = int(input())
    for i in range(1, T+1):
        data = input()
        print("#{} {}".format(i, weekDays[data]))


"""

3
SUN
SAT
MON
"""