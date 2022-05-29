if __name__ == "__main__":
    T = int(input())
    week = {"SUN":0, "MON":1, "TUE":2, "WED":3,
            "THU":4, "FRI":5, "SAT":6}
    for t in range(T):
        day = input()
        print("#{} {}".format(t+1, 7-week[day]))
