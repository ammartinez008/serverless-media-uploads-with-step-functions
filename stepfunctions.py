import os
import json
import boto3
stepfunctions = boto3.client('stepfunctions')
STATE_ARN = os.environ['statemachine_arn']

def execute(event, context):
    stepfunctions.start_execution(stateMachineArn=STATE_ARN)
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
