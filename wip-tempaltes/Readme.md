#Deploy the configuration template
export CONFIG_TEMPLATE=cloudformation-ec2-instance-minikube
aws cloudformation create-stack --stack-name ${CONFIG_TEMPLATE}-STACK --template-body file://./${CONFIG_TEMPLATE}.yaml --region us-east-1 --capabilities CAPABILITY_NAMED_IAM
