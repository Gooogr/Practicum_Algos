def is_power_of_four(number: int) -> bool:
    # Здесь реализация вашего решения
    n = 0
    while 4 ** n <= number:
        if 4 ** n == number:
            return True
        else:
            n += 1
    return False

print(is_power_of_four(int(input())))