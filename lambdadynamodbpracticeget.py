import boto3
import csv
import json

def lambda_handler(event, context):
    # Define your S3 bucket name and CSV file name
    s3_bucket = "source-demo-json-bucket"
    csv_file = "data.csv"
    table_name = "user"  # Your DynamoDB table name

    # Create clients for S3 and DynamoDB
    s3_client = boto3.client('s3')
    dynamodb_client = boto3.client('dynamodb')

    try:
        # Read the CSV file from S3
        response = s3_client.get_object(Bucket=s3_bucket, Key=csv_file)
        csv_data = response['Body'].read().decode('utf-8')

        # Parse CSV data
        csv_reader = csv.DictReader(csv_data.splitlines())

        # Store each record in DynamoDB
        for item in csv_reader:
            # Create the DynamoDB item with dynamic attributes and values
            dynamodb_item = {}

            # Iterate through each key-value pair in the CSV record
            for key, value in item.items():
                # Create the appropriate attribute based on the data type of the value
                if value.isdigit():  # Assuming numerical values are integers (change as needed)
                    dynamodb_item[key] = {'N': value}
                else:
                    dynamodb_item[key] = {'S': value}

            # Add the 'id' attribute to the DynamoDB item
            dynamodb_item['id'] = {'S': item['Invoice ID']}  # Assuming 'Invoice ID' is the unique identifier

            # Perform the DynamoDB put_item operation with the constructed item
            response = dynamodb_client.put_item(
                TableName=table_name,
                Item=dynamodb_item
            )

            print(f"Inserted item with id: {item['Invoice ID']}")

        return {
            'statusCode': 200,
            'body': json.dumps('Data fetched and stored in DynamoDB successfully.')
        }
    except Exception as e:
        print("Error:", e)
        return {
            'statusCode': 500,
            'body': json.dumps('Error occurred while processing data.')
        }
