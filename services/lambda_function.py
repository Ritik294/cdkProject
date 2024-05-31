import boto3
import json
client=boto3.client("s3")

def lambda_handler(event,context):
    response=client.get_object(Bucket='banking-app-bucket',
                               Key='emp.json')
    data_byte=response['Body'].read()
    data_string=data_byte.decode('UTF-8')
    data_dict=json.loads(data_string)

    return {
        'statusCode':200,
        'body':json.dumps(data_dict),
        'headers':{'Content-Type':'application/json'}
    }