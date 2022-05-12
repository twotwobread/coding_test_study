# < 단지번호붙이기 >
# 문제유형 : DFS/BFS
# 자료구조 : 2차원 리스트 - 단지의 정보가 2차원 배열로 주어지고 이를 이용하기 위해 또 원소가 빠지는 부분이
#						없기 때문에 시간 복잡도가 느려질 일도 없음.
# 1. 1이 단지에 속하는 칸이라는 의미기에 1을 찾는다.
# 2. 그후에 bfs를 이용하여 단지의 범위를 찾고 1을 2로 바꾸고 수를 카운트.
# 3. 이를 리스트에 담고 정렬.

from collections import deque

dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)
def outOfRange(r,c):
	if 0<=r<n and 0<=c<n:
		return True
	else:
		return False
def bfs(queue):
	count = 0
	while queue:
		r, c = queue.popleft()
		count += 1
		for i in range(4):
			adj_r, adj_c = r + dx[i], c + dy[i]
			if outOfRange(adj_r, adj_c) and map[adj_r][adj_c] == 1:
				map[adj_r][adj_c] = 2
				queue.append((adj_r, adj_c))
	return count
def solution():
	queue = deque()
	value = []
	for i in range(n):
		for j in range(n):
			if map[i][j] == 1:
				map[i][j] = 2
				queue.append((i,j))
				value.append(bfs(queue))
	return sorted(value)

if __name__ == "__main__":
	n = int(input())
	map = [list(map(int, input())) for _ in range(n)]
	result = solution()
	print(len(result))
	for i in range(len(result)):
		print(result[i])