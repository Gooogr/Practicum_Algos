# https://contest.yandex.ru/contest/24414/problems/A/
# https://contest.yandex.ru/contest/24414/run-report/80109376/
'''
--Описание решения--
Решение основано на принципах поисковой системы описанной в условии задачи.
Для каждого документа вычисляется поисковый индекс, в котором хранится частота 
появления каждого уникального слова в документе.
При поисковом запросе для каждого уникального и входящего в поисковй индекс 
слова эти веса складываются и результат выдачи ранжируется по нему.

--Доказательство корректности--
Каждому документу соответсвует хэш-таблица с частотными значениями слов.
В случае попадания слов из запроса в этот список мы можем проранжировать документы.
В противном случае результат ранжирования будет пустым.

--Временная сложность--
Временная сложность построения поискового индекса:
O(число документов * максимальное число слов в документе)
Временная сложность поиска для каждого запроса:
О(число слов в запросе)

--Пространственная сложность--
Алгоритм требует O(числа слов запросе) дополнительной памяти для каждого запроса

'''

from typing import List, Dict, Tuple
from collections import defaultdict, Counter

def create_search_index(docs: List[str]) -> Dict[str, Dict[int, int]]:
    '''
    Create search index as
    {word1: {doc_1:word_count_in_doc_1}, ...}, ...}
    '''
    index_hash = defaultdict(dict)
    for doc_idx, doc in enumerate(docs):
        for word, count in Counter(doc.split()).items():
            index_hash[word][doc_idx] = count
    return index_hash


def search_query(
    query: str, 
    index_hash: Dict[str, Dict[int, int]], 
    n_docs: int, 
    limit: int=5
) -> List[int]:
    '''
    Find indecies of the most relevant documnets from the search index
    '''
    # initialize weights for earch document from index hash
    docs_weights = [0] * n_docs
    # compute search index weights for query
    for word in set(query.split()):
        if word in index_hash:
            for doc_idx, count in index_hash[word].items():
                docs_weights[doc_idx] += count
    # sort and filter results
    sorted_docs_idx = sorted(range(n_docs), 
                             key=lambda x: docs_weights[x], 
                             reverse=True)
    result = []
    i = 0
    while len(result) < limit and i < n_docs:
        if docs_weights[sorted_docs_idx[i]] != 0:
            result.append(sorted_docs_idx[i] + 1)
            if len(result) == limit:
                break
        i += 1
    return result

def read_input() -> Tuple[int, List[str], List[str]]:
    '''
    Read input data
    '''
    n_docs = int(input().strip())
    docs = []
    for _ in range(n_docs):
        docs.append(input().strip())

    n_queries = int(input().strip())
    queries = []
    for _ in range(n_queries):
        queries.append(input().strip())
    return n_docs, docs, queries

n_docs, docs, queries = read_input()
index_hash = create_search_index(docs)
for query in queries:
    result_order = search_query(query, index_hash, n_docs)
    print(*result_order)
