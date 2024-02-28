import boto3
import json
import os

# import requests
dynamodb = boto3.resource('dynamodb')
table_name = os.environ['TABLE_NAME']
table = dynamodb.Table(table_name)  # Replace with your DynamoDB table name

def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    try:
        print('Table name: ' + table_name)
        response = table.update_item(
            Key={'visits': 'counter'},
            UpdateExpression='SET footfall = if_not_exists(footfall, :zero) + :incr',
            ExpressionAttributeValues={':zero': 0, ':incr': 1},
            ReturnValues='UPDATED_NEW',
            ConditionExpression='attribute_not_exists(visits) OR footfall >= :zero'
        )
        count = response['Attributes']['footfall']
        print('Update successful')
        print('Count: ' + str(count))
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',  # or specify your allowed origin
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
            },
            'body': json.dumps({'count': float(count)})
        }
    except Exception as e:
        print('Error:', str(e))
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',  # or specify your allowed origin
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
            },
            'body': json.dumps({'error': 'There is an internal Error'})
        }
