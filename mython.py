import json
import time 
import os 

def lambda_handler(event, context):
    #TODO Implement 
    print("cennoecting to db")
    print("running the functioncode")
    return {
        'statusCode': 200, 
        'body': json.dumps('Hello from M<ABL:A')
    }