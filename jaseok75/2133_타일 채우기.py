'''
Project: 백준_2133
Date: 2022.07.31.
Content: DP
- 짝수만 가능 (홀수일 때는 0으로 반환)
- 현재값 = 이전값 * 3 + (이전값 - 이전이전값)
'''


def solution():
    if n % 2 != 0:
        print("0")
        return
    result_1, result_2 = 1, 0 # 최초의 값은 1로 설정
    diff = 0    # 이전값 - 이전이전값
    for i in range(n // 2):
        result_2 = result_1 * 3 # 현재값 = 이전값 * 3
        result_2 += diff        # 현재값 += (이전값 - 이전이전값)
        diff = result_2 - result_1  # 차이값 바꿔주기
        result_1 = result_2 # 이전값 바꿔주기
    print(result_2)


if __name__ == "__main__":
    n = int(input())
    solution()
