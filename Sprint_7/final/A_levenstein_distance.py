# https://contest.yandex.ru/contest/25597/problems/A/
# https://contest.yandex.ru/contest/25597/run-report/81926917/

'''
--Описание решения--
Основано на описании алгоритма из википедии: 
https://en.wikipedia.org/wiki/Levenshtein_distance

Суть: 
* Создаем матрицу размером (m + 1) 
Дополнительное простанство нужно для базового случая - пустой строки.
В процессе работы алгоритма будет хранить вторую матрицу такой же длины, кэшируя 
данные по текущему и прошлому элементу изменяемой.
* Сдвигам указатели в строках таким образом, чтобы минимизировать 
суммарное количество изменений.

Движение курсора:
* Элементы равны - current_row[j + 1] = previous_row[j] 
число изменений не поменялось, копируем значение и переходим к слелующей паре элементов.
* Добавление элемента в строку word1 - previous_row[j], 
+1 к числу изменений, сдвиг в первой строке из-за вставки
* Удаление элемента из строки word1 - current_row[j],
+1 к числу изменений, сдвиг во второй строке к следующему элементу
* Замена элемента в строке word1 - previous_row[j + 1],
+1 к числу изменений, замена произошла на место старого элемента,
можем переходить к следующей паре элементов

--Доказательство корректности--

Мы начинаем обход с краев матрицы, используя bottom up подход.
Итоговое значение будет лежать в ячейке  current_row[-1]

--Временная сложность--
Временная сложность алгоритма состовляет O(m*n),
где m и n - число элементов во входных строках

--Пространственная сложность--
Пространственная сложность алгоритма состовляет O(m*n)

'''

from typing import Tuple

def read_input() -> Tuple[int, int]:
    word1 = input().strip()
    word2 = input().strip()
    return word1, word2


### --- Original version with O(m*n) memory complexity ---###
def get_lev_dist(word1: str, word2: str) -> int:
    dp = [[float('inf')] * (len(word2) + 1) for _ in range(len(word1) + 1)]

    # Infill edges. Idea behind it - if one of your strings is empty
    # you need to add/delete all elements in the other one
    for j in range((len(word2) + 1)):
        dp[len(word1)][j] = len(word2) - j
    for i in range((len(word1) + 1)):
        dp[i][len(word2)] = len(word1) - i

    # Bottom up from edges to top left corner
    for i in range(len(word1) - 1, -1, -1):
        for j in range(len(word2) - 1, -1, -1):
            if word1[i] == word2[j]:
                # No changes - write previous step counter value
                dp[i][j] = dp[i + 1][j + 1]
            else:
                # Select optimal aproach based on previous history
                dp[i][j] = 1 + min(
                    dp[i + 1][j],    # insert
                    dp[i][j + 1],    # delete
                    dp[i + 1][j + 1] # replace
                )
    return dp[0][0]

### --- Updated  version with O(min(m, n)) memory complexity ---###

# Also use top down approach to make indicies more readable
def get_lev_dist(word1: str, word2: str) -> int:
    m, n = len(word1), len(word2)
    if m > n:
        word1, word2, m, n = word2, word1, n, m
    
    current_row = [0] * (n + 1)
    for j in range(n + 1):
        current_row[j] = j
    
    for i in range(m):
        previous_row, current_row = current_row, [i + 1] + [0] * n
        for j in range(n):
            if word1[i] == word2[j]:
                current_row[j + 1] = previous_row[j]
            else:
                current_row[j + 1] = 1 + min(previous_row[j], current_row[j], previous_row[j + 1])
    
    return current_row[-1] 


print(get_lev_dist(*read_input()))

