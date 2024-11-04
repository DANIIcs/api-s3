import boto3

def lambda_handler(event, context):
    bucket_name = event["body"]["bucket_name"]
    directorio = event["body"]["directorio"]
    archivo = event["body"]["archivo"]
    nombre_objeto = event["body"].get("nombre_objeto", archivo)

    ruta_objeto = f"{directorio}/{nombre_objeto}"

    try:
        s3 = boto3.client("s3")
        s3.upload_file(archivo, bucket_name, ruta_objeto)
        return {
            "statusCode": 201,
            "message": f"Archivo '{archivo}' subido exitosamente a '{ruta_objeto}' en el bucket '{bucket_name}'."
        }

    except Exception as e:
        print(e)
        return {
            "statusCode": 400,
            "message": "No se pudo subir el archivo"
        }
