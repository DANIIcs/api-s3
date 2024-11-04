import boto3

def lambda_handler(event, context):
    bucket_name = event["body"]["bucket_name"]
    directorio = event["body"]["directorio"]

    try:
        s3 = boto3.client("s3")
        # Crear un objeto vacío para representar el directorio
        s3.put_object(Bucket=bucket_name, Key=(directorio + '/'))
        return {
            "statusCode": 201,
            "message": f"Directorio '{directorio}' creado exitosamente en el bucket '{bucket_name}'."
        }

    except Exception as e:
        print(e)
        return {
            "statusCode": 400,
            "message": "No se pudo crear el directorio"
        }
