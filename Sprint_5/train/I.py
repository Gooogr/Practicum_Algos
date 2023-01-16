# https://contest.yandex.ru/contest/24809/problems/I/

# Числа Каталана
def numTrees_catalan(n: int) -> int:
	sol = 1
	for i in range (0, n):
		sol = sol * 2 * (2 * i + 1) / (i + 2)
	return int(sol)

print(numTrees_catalan(int(input())))