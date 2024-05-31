import boto3
import json


def lambda_handler(event,context):
    response=client.get_object(Bucket='',key='')
    data_byte=response['Body'].read()
    data_string=data_byte.decode('UTF-8')
    data_dict=json.loads(data_string)

    return {
        'StatusCode':200,
        'body':json.dumps(data_dict),
        'headers':{'Content-Type':'application/json'}
    }