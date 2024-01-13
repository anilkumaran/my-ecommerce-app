from flask import Flask
import boto3
from botocore.exceptions import ClientError

import os


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/createLaptop')
def hello_world():
    data = {"name": "Macbook prod"}
    # db_details = get_secret()
    db_host = os.environ['host']
    return 'Hello, World!'

def get_secret():

    secret_name = "jenkins_admin_user_creds"
    region_name = "us-east-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )
    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    return get_secret_value_response['SecretString']

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


