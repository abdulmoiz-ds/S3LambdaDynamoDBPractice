# S3LambdaDynamoDBPractice
Hi, I was practicing AWS Lambda, AWS DynamoDB, and AWS S3. A quick overview of these services.

# AWS Lambda
AWS Lambda is a computing service provided by AWS. It is a serverless service. We don't have to worry about any infrastructure and servers.
# AWS DynamoDB
AWS DynamoDB is a database service where we can store NoSQL data.
# AWS S3
AWS S3 is a storage service where we can store raw data in any format.

# Project Overview

In this project, my motive was to perform some tasks on batch data. I used AWS S3 to store data. I manually uploaded data to AWS S3 using AWS Console. It could also be done using AWS CLI. After this, I created an AWS DynamoDB table and set the primary key as "string". Then I created a Lambda function to write code. This code will fetch data from the S3 bucket and then store this data by assuming the data attributes on its own, in the AWS DynamoDB table.

## Step 1:
Create an S3 bucket and then upload any data in the bucket using AWS Console.
![Screenshot (581)](https://github.com/abdulmoiz-ds/S3LambdaDynamoDBPractice/assets/74011754/16336590-4099-4cb4-9cf2-07f81299a40d)

## Step 2:
Now go to AWS DynamoDB and create a table.
![Screenshot (582)](https://github.com/abdulmoiz-ds/S3LambdaDynamoDBPractice/assets/74011754/6047b11a-7ec2-4770-a539-66fe2ee21a8b)

## Step 3:
Now go to AWS IAM and create a role and attach the necessary policies to it. You can see this in the picture.![Screenshot (583)](https://github.com/abdulmoiz-ds/S3LambdaDynamoDBPractice/assets/74011754/808a76c7-618e-4834-8fd3-e2496c7ecb29)

![Screenshot (584)](https://github.com/abdulmoiz-ds/S3LambdaDynamoDBPractice/assets/74011754/0c5ef20c-1e0a-45b3-aba5-11972a727e23)


## Step 4:
It's time to create a Lambda function and assign the IAM role we just created. After that, you can see the Python file I attached to this repository to do the remaining task.
