import uuid
import boto3
import json
import os


# create_by panjingping
# description: create short url token
# create 2020.6.2

def handler(event, context):
    token = hex(uuid.getnode())

    url = event['postData']['url']
    customDomain = event['postData']['customDomain']

    bucket = event['postData']['bucket']

    short_url = customDomain + "/" + token
    s3 = boto3.client('s3')
    # TODO implement
    try:
        s3.put_object(ACL='public-read', Bucket=bucket, Key=token, WebsiteRedirectLocation=url, ContentType='text/html')

        return {'statusCode': 200,
                'body': json.dumps({'short_url': short_url, 'url': url, 'token': token}),
                'headers': {'Content-Type': 'application/json'}}
    except Exception as e:
        print(e)
        raise e
