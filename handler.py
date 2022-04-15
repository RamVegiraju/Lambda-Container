from cmath import sqrt
import json
import boto3
import numpy as np

def handler(event, context):
    print(type(event))
    print(event)
    inp = event['Input']
    print(type(inp))
    print(inp)
    res = int(np.sqrt(inp))
    print(res)
    print(type(res))

    return {
        'statusCode': 200,
        'body': res
    }