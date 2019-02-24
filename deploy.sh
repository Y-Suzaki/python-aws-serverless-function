#!/bin/bash -e

s3_bucket="ys-dev-web-iot-rule-test"

echo "** Start to deploy and build. **"
mkdir -p deploy
pip3 install -r requirements.txt -t deploy
cp -r src/* deploy
cd deploy
zip -r ../serverless-function.zip *
cd ..

#echo "Upload applicaiton zip and swagger spec to s3 bucket..."
#aws s3 cp serverless-function.zip s3://${s3_bucket}/ \
#  --region us-west-2 \
#  --profile default

echo "Build serverless function..."
aws cloudformation package \
  --template-file aws-sam.yaml \
  --output-template-file aws-sam-deploy.yaml \
  --s3-bucket ${s3_bucket} \
  --s3-prefix serverless-function \
  --region us-west-2 \
  --profile default

echo "Deploy serverless function..."
aws cloudformation deploy \
  --template-file aws-sam-deploy.yaml \
  --stack-name serverless-function \
  --capabilities CAPABILITY_IAM \
  --parameter-overrides ArtifactBucket=${s3_bucket} \
  --region us-west-2 \
  --profile default

echo "** All complete! **"
aws s3 rm s3://${s3_bucket}/serverless-function/ \
  --region us-west-2 \
  --profile default \
  --recursive

rm -rf deploy
rm -f aws-sam-deploy.yaml serverless-function.zip
