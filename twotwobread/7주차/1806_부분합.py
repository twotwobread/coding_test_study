# 10,000 이하의 자연수로 이루어진 길이 N짜리 수열
# 이 수열에서 연속된 수들의 부분합 중 그 합이 S 이상 되는 것 중 가장 짧은 것의 길이를 구하여라.
# 누적 합을 이용해서 N이 최대 100,000개 , S = 100,000,000까지
# 해당 문제를 완전 탐색을 이용하여 푸는 방법을 생각해보자.
# 첫번째 인덱스부터 값을 더해나가면서 누적 시켜서 합을 구해야한다. 그러면 해당 인덱스의 누적 합을 N의 시간복잡도가 아닌 1로 구할 수 있음.
# 만약 1 - 해당 인덱스까지의 누적합이 s를 넘는다면 그때부터 더 짧은데 s를 넘는 수를 찾아야 한다.
# 이를 위해서 맨처음 값부터 뺴보면서 값이 넘는지를 확인하면서 길이를 더 짧다면 업데이트한다.
def prefix_sum():
    global LENGTH
    total = 0
    left = 0
    for i, number in enumerate(sequence):
        right = i
        total += number
        while total >= S:
            LENGTH = min(LENGTH, right - left + 1)
            total -= sequence[left]
            left += 1

if __name__ == "__main__":
    INF = int(1e9)
    LENGTH = INF
    N, S = map(int, input().split())
    sequence = list(map(int, input().split()))
    prefix_sum()
    print(0 if LENGTH == INF else LENGTH)
