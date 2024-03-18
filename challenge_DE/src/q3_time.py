import json
from collections import Counter
from typing import List, Tuple

def q3_time(file_path: str) -> List[Tuple[str, int]]:

    # Crear un contador para almacenar la cantidad de menciones por usuario
    mention_counter = Counter()

    # Leer el archivo JSON línea por línea
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            tweet = json.loads(line)
            content = tweet['content']
            mentions = [word[1:] for word in content.split() if word.startswith('@')]
            mention_counter.update(mentions)

    # Obtener los top 10 usuarios más mencionados
    top_10_users = mention_counter.most_common(10)

    return top_10_users