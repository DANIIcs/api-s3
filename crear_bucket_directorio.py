import boto3
import json

def lambda_handler(event, context):
    try:
        # Decodificar el cuerpo si es necesario
        body = json.loads(event["body"])

        bucket_name = body["bucket_name"]
        directorio = body["directorio"]

        s3 = boto3.client("s3")
        # Crear un objeto vacío para representar el directorio
        s3.put_object(Bucket=bucket_name, Key=(directorio + '/'))
        
        return {
            "statusCode": 201,
            "message": f"Directorio '{directorio}' creado exitosamente en el bucket '{bucket_name}'."
        }

    except KeyError as e:
        return {
            "statusCode": 400,
            "message": f"Falta un parámetro en la solicitud: {str(e)}"
        }

    except Exception as e:
        print(e)
        return {
            "statusCode": 400,
            "message": "No se pudo crear el directorio"
        }
