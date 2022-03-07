#Deploy the configuration template
export CONFIG_TEMPLATE=config-create-template
export EVENT_TEMPLATE=events-create-config
aws cloudformation create-stack --stack-name ${CONFIG_TEMPLATE}-STACK --template-body file://./${CONFIG_TEMPLATE}.yaml --region us-east-1 --capabilities CAPABILITY_NAMED_IAM
aws cloudformation create-stack --stack-name ${EVENT_TEMPLATE}-STACK --template-body file://./${EVENT_TEMPLATE}.yaml --region us-east-1 --capabilities CAPABILITY_NAMED_IAM
