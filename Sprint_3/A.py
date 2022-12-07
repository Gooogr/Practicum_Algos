# https://contest.yandex.ru/contest/23638/problems/A/

results = []

def generate_valid_brackets_line(n:int, line:str, n_open: int, n_closed: int):
    if n_open == n_closed == n:
        results.append(line)
        return
    # Number of ( should be less than n
    if n_open < n: 
        generate_valid_brackets_line(n, line + '(', n_open + 1, n_closed)
    # Number of ) can't be more than number of (
    if n_open > n_closed:
        generate_valid_brackets_line(n, line + ')', n_open, n_closed + 1)
    else:
        return None

generate_valid_brackets_line(int(input()), '', 0, 0)
for item in results:
    print(item)


        