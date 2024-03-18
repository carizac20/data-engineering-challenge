from typing import List, Tuple
from datetime import datetime
from collections import Counter
import json

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    # Inicializa un contador para todas las combinaciones de fecha y usuario.
    date_user_counter = Counter()
    
    # Abre el archivo y procesa cada línea individualmente.
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            tweet = json.loads(line)
            # Extrae la fecha y el nombre de usuario, y actualiza el contador.
            date_str = tweet['date'].split('T')[0]
            date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
            username = tweet['user']['username']
            date_user_counter[(date_obj, username)] += 1

    # Encuentra las 10 fechas más comunes y el usuario más activo en esas fechas.
    most_common = date_user_counter.most_common(10)

    # Devuelve los resultados como una lista de tuplas.
    return [(date, user) for (date, user), count in most_common]
