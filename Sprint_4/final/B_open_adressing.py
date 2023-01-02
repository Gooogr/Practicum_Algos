# https://contest.yandex.ru/contest/24414/problems/B/
# https://contest.yandex.ru/contest/24414/run-report/80230936/

'''
--Описание решения--
Хеш таблица, способ разрешения коллизий - метод открытой адресации.
Представляет собой два листа, один для хранения ключей, другой - для хранения 
значений. Выбор индекса определяется через линейное пробирование.
При удалении перезаписанные ячейки помечаются как DELETED.
Размер таблицы равен 130003. По условию число операций над таблцей не превышет 1e5,
таким образом при коэффициенте заполненности в 1.3 минимальное простое число 
превышающее 1.3*e5 будет 130003.
Список простых чисел: http://compoasso.free.fr/primelistweb/page/prime/liste_online_en.php


--Доказательство корректности--
Поскольку размер таблицы всегда больше максимального числа операций над ней,
то в таблице всегда будет свободное место и цикл разрешения коллизии отработает
корректно.

--Временная сложность--
Средняя сложность операций над хеш-таблицами составляет O(1+alpha), 
где alpha — текущий коэффициент заполнения хеш-таблицы.

--Пространственная сложность--
Алгоритм потребует O(N) дополнительной памяти
'''

from typing import List, Optional
TABLE_CAPACITY = 130003 # minimum prime number > 1e5 * 1.3

class Hash_table:
    def __init__(self, capacity):
        self.capacity = capacity
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity

    def _get_bucket(self, key: int) -> int:
        '''
        Compute hash backet for int value
        '''
        return key % self.capacity
    
    def _reget_bucket(self, old_bucket: int) -> int:
        '''
        Linear probing
        '''
        return (old_bucket + 1) % self.capacity
    
    def put(self, key: int, value: int) -> None:
        '''
        Add key-value pair in hash table
        '''
        bucket_idx = self._get_bucket(key)
        # Simple case - put new key-value in empty space
        if self.values[bucket_idx] is None:
            self.keys[bucket_idx] = key
            self.values[bucket_idx] = value
        # Update case - keep key and change value
        elif self.keys[bucket_idx] == key:
            self.values[bucket_idx] = value
        # Collision case. Try to find empty space or target key
        else:
            next_bucket_idx = self._reget_bucket(bucket_idx)
            while (self.values[next_bucket_idx] is not None  
                   and self.keys[next_bucket_idx] not in (key, 'DELETED')):
                next_bucket_idx = self._reget_bucket(next_bucket_idx)
            # If we find empty space
            if (self.values[next_bucket_idx] is None 
                or self.values[bucket_idx] == 'DELETED'):
                self.keys[next_bucket_idx] = key
                self.values[next_bucket_idx] = value
            # Else - update value
            else:
                self.values[next_bucket_idx] = value

    def get(self, key: int) -> Optional[int]:
        bucket_idx = self._get_bucket(key)
        while (self.values[bucket_idx] is not None 
                and self.keys[bucket_idx] != key):
            bucket_idx = self._reget_bucket(bucket_idx)
        if self.keys[bucket_idx] == key:
            value = self.values[bucket_idx] 
            return value if value != 'DELETED' else None
        return None

    def delete(self, key: int) -> Optional[int]:
        value = self.get(key)
        if value is not None and value != 'DELETED':
            self.put(key, 'DELETED')
            return value
        else:
            return None

###----------------------------- Helper functions --------------------------###
def read_input() -> List[str]:
    n = int(input())
    commands = []
    for _ in range(n):
        commands.append(str(input()))
    return commands

def apply_commands(hash_table: Hash_table, commands: List[str]):
    for step in commands:
        *step,  = step.split() # flexible unpacking
        if step[0] == 'put':
            hash_table.put(int(step[1]), int(step[2]))
        elif step[0] == 'get':
            result = hash_table.get(int(step[1]))
            if result is None:
                print('None')
            else:
                print(result)
        elif step[0] == 'delete':
            result = hash_table.delete(int(step[1]))
            if result is None:
                print('None')
            else:
                print(result)
        else:
            raise ValueError('Incorrect command')

###--------------------------------- Main run ------------------------------###

hash_table = Hash_table(TABLE_CAPACITY)
commands = read_input()
apply_commands(hash_table, commands)