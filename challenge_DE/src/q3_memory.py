import pandas as pd
from typing import List, Tuple

def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    mention_counts = pd.Series(dtype='int')
    
    # Leer los datos en bloques para ser más eficiente en memoria
    for df_chunk in pd.read_json(file_path, lines=True, chunksize=10000):
        # Asegurarse de que 'mentionedUsers' exista y no esté completamente vacío
        if 'mentionedUsers' in df_chunk and not df_chunk['mentionedUsers'].isnull().all():
            # Extraer y contar las menciones por usuario
            chunk_mentions = df_chunk['mentionedUsers'].explode().dropna()
            chunk_mentions_counts = chunk_mentions.apply(lambda x: x['username']).value_counts()
            mention_counts = mention_counts.add(chunk_mentions_counts, fill_value=0)
    
    # Obtener los 10 usuarios más mencionados
    top_10_mentions = mention_counts.nlargest(10).items()
    return list(top_10_mentions)

# Ruta al archivo JSON, ajusta según sea necesario
file_path = r"C:\Users\CAMILO\OneDrive\Documents\GitHub\data-engineering-challenge\tweets\farmers-protest-tweets-2021-2-4.json"

# Llamar a la función y obtener los resultados
top_users_by_mentions = q3_memory(file_path)
#print(top_users_by_mentions)