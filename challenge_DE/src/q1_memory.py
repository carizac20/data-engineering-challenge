import json
from collections import defaultdict
from typing import Generator, Tuple

def q1_memory(file_path: str) -> Generator[Tuple[str, str], None, None]:
    user_counts = defaultdict(lambda: defaultdict(int))

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            tweet = json.loads(line)
            date_str = tweet['date'][:10]
            username = tweet['user']['username']
            user_counts[date_str][username] += 1

    def results_gen():
        for date, users in user_counts.items():
            top_user = max(users, key=users.get)
            yield date, top_user

    # You can adjust the number returned based on your needs
    return sorted(results_gen(), key=lambda x: x[1], reverse=True)[:10]

# Suponiendo que tienes el archivo JSON en el siguiente path

file_path = r"C:\Users\CAMILO\OneDrive\Documents\GitHub\data-engineering-challenge\tweets\farmers-protest-tweets-2021-2-4.json"
# Llamar a la función q1_memory para obtener los resultados
top_results = q1_memory(file_path)

#Imprimir los resultados sin el contador
#print("Top 10 fechas con más tweets y el usuario con más publicaciones:")
#for i, (date, username) in enumerate(top_results, start=1):
#    print(f"{i}. Fecha: {date}, Usuario con más publicaciones: {username}")
