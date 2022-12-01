from typing import List

def get_weather_randomness(temperatures: List[int]) -> int:
    # Здесь реализация вашего решения
    n = len(temperatures)
    if n == 1:
        return 1
    counter = 0
    for idx, t in enumerate(temperatures):
        # Edge cases
        if idx == 0 and t > temperatures[1]:
            counter += 1
        elif idx == n - 1 and t > temperatures[idx-1]:
            counter += 1
        # General case
        elif temperatures[idx - 1] < t > temperatures[idx + 1]:
            counter += 1
    return counter


def read_input() -> List[int]:
    n = int(input())
    temperatures = list(map(int, input().strip().split()))
    return temperatures

temperatures = read_input()
print(get_weather_randomness(temperatures))