from typing import Tuple

def get_excessive_letter(shorter: str, longer: str) -> str:
    # Здесь реализация вашего решения
    shorter = sorted(shorter)
    longer = sorted(longer)
    for idx in range(len(shorter)):
        if shorter[idx] != longer[idx]:
            return longer[idx]
    return longer[-1]

def read_input() -> Tuple[str, str]:
    shorter = input().strip()
    longer = input().strip()
    return shorter, longer

shorter, longer = read_input()
print(get_excessive_letter(shorter, longer))