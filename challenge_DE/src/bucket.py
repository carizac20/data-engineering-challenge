import pandas as pd
from google.cloud import storage
from google.oauth2 import service_account

def dataframe_to_gcs_json(df, bucket_name, destination_blob_name):
    # Convertir DataFrame a JSON
    json_str = df.to_json(orient='records', lines=True)
    key_path = "credentials.json"

# Carga las credenciales de la cuenta de servicio desde un archivo JSON
    credentials = service_account.Credentials.from_service_account_file(    
        key_path,
    )
    print('creds', credentials)

    # Inicializa el cliente de GCS
    storage_client = storage.Client(credentials=credentials)

    # Obtiene el bucket
    bucket = storage_client.bucket(bucket_name)

    # Crea un nuevo blob y sube el JSON
    blob = bucket.blob(destination_blob_name)
    
    # Sube el JSON al blob
    blob.upload_from_string(json_str, content_type='application/json')

    print(f"DataFrame uploaded to {destination_blob_name} in bucket {bucket_name}.")