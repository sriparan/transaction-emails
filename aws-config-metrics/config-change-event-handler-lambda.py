objMoveFromCompToNonCompEvent = {
    "version": "0",
    "id": "81d83bb1-13dc-cb1e-b370-5c8151b020f7",
    "detail-type": "Config Rules Compliance Change",
    "source": "aws.config",
    "account": "111111111111",
    "time": "2022-03-02T07:03:47Z",
    "region": "us-east-1",
    "resources": [],
    "detail": {
        "resourceId": "vol-0f0b1ec8ced432a26",
        "awsRegion": "us-east-1",
        "awsAccountId": "111111111111",
        "configRuleName": "volumes-prod-tags",
        "recordVersion": "1.0",
        "configRuleARN": "arn:aws:config:us-east-1:111111111111:config-rule/config-rule-dx9jfb",
        "messageType": "ComplianceChangeNotification",
        "newEvaluationResult": {
            "evaluationResultIdentifier": {
                "evaluationResultQualifier": {
                    "configRuleName": "volumes-prod-tags",
                    "resourceType": "AWS::EC2::Volume",
                    "resourceId": "vol-0f0b1ec8ced432a26"
                },
                "orderingTimestamp": "2022-03-02T07:03:08.000Z"
            },
            "complianceType": "NON_COMPLIANT",
            "resultRecordedTime": "2022-03-02T07:03:46.945Z",
            "configRuleInvokedTime": "2022-03-02T07:03:45.230Z",
            "annotation": "\nTag costcenter is not present."
        },
        "oldEvaluationResult": {
            "evaluationResultIdentifier": {
                "evaluationResultQualifier": {
                    "configRuleName": "volumes-prod-tags",
                    "resourceType": "AWS::EC2::Volume",
                    "resourceId": "vol-0f0b1ec8ced432a26"
                },
                "orderingTimestamp": "2022-03-02T00:39:21.000Z"
            },
            "complianceType": "COMPLIANT",
            "resultRecordedTime": "2022-03-02T00:39:56.391Z",
            "configRuleInvokedTime": "2022-03-02T00:39:54.576Z",
            "annotation": "This resource is compliant with the rule."
        },
        "notificationCreationTime": "2022-03-02T07:03:47.488Z",
        "resourceType": "AWS::EC2::Volume"
    }
}


objMoveFromNonCompToCompEvent = {
    "version": "0",
    "id": "f9d5849b-3677-603b-92af-ab18e8877184",
    "detail-type": "Config Rules Compliance Change",
    "source": "aws.config",
    "account": "111111111111",
    "time": "2022-03-02T00:39:56Z",
    "region": "us-east-1",
    "resources": [],
    "detail": {
        "resourceId": "vol-0f0b1ec8ced432a26",
        "awsRegion": "us-east-1",
        "awsAccountId": "111111111111",
        "configRuleName": "volumes-prod-tags",
        "recordVersion": "1.0",
        "configRuleARN": "arn:aws:config:us-east-1:111111111111:config-rule/config-rule-dx9jfb",
        "messageType": "ComplianceChangeNotification",
        "newEvaluationResult": {
            "evaluationResultIdentifier": {
                "evaluationResultQualifier": {
                    "configRuleName": "volumes-prod-tags",
                    "resourceType": "AWS::EC2::Volume",
                    "resourceId": "vol-0f0b1ec8ced432a26"
                },
                "orderingTimestamp": "2022-03-02T00:39:21.000Z"
            },
            "complianceType": "COMPLIANT",
            "resultRecordedTime": "2022-03-02T00:39:56.391Z",
            "configRuleInvokedTime": "2022-03-02T00:39:54.576Z",
            "annotation": "This resource is compliant with the rule."
        },
        "oldEvaluationResult": {
            "evaluationResultIdentifier": {
                "evaluationResultQualifier": {
                    "configRuleName": "volumes-prod-tags",
                    "resourceType": "AWS::EC2::Volume",
                    "resourceId": "vol-0f0b1ec8ced432a26"
                },
                "orderingTimestamp": "2022-03-02T00:08:34.000Z"
            },
            "complianceType": "NON_COMPLIANT",
            "resultRecordedTime": "2022-03-02T00:09:06.189Z",
            "configRuleInvokedTime": "2022-03-02T00:09:05.899Z",
            "annotation": "\nTag costcenter is not present."
        },
        "notificationCreationTime": "2022-03-02T00:39:56.836Z",
        "resourceType": "AWS::EC2::Volume"
    }
}

newObjectCreatedInNonCompStateevent= {
    "version": "0",
    "id": "776c8973-7430-cb53-887c-fbe30d0919a1",
    "detail-type": "Config Rules Compliance Change",
    "source": "aws.config",
    "account": "111111111111",
    "time": "2022-03-02T00: 09: 06Z",
    "region": "us-east-1",
    "resources": [],
    "detail": {
        "resourceId": "vol-0f0b1ec8ced432a26",
        "awsRegion": "us-east-1",
        "awsAccountId": "111111111111",
        "configRuleName": "volumes-prod-tags",
        "recordVersion": "1.0",
        "configRuleARN": "arn:aws:config:us-east-1: 111111111111:config-rule/config-rule-dx9jfb",
        "messageType": "ComplianceChangeNotification",
        "newEvaluationResult": {
            "evaluationResultIdentifier": {
                "evaluationResultQualifier": {
                    "configRuleName": "volumes-prod-tags",
                    "resourceType": "AWS: :EC2: :Volume",
                    "resourceId": "vol-0f0b1ec8ced432a26"
                },
                "orderingTimestamp": "2022-03-02T00:08:34.000Z"
            },
            "complianceType": "NON_COMPLIANT",
            "resultRecordedTime": "2022-03-02T00:09:06.189Z",
            "configRuleInvokedTime": "2022-03-02T00:09:05.899Z",
            "annotation": "\nTag costcenter is not present."
        },
        "notificationCreationTime": "2022-03-02T00:09:06.393Z",
        "resourceType": "AWS: :EC2: :Volume"
    }
}
import json
import boto3
import logging

LOGGER = logging.getLogger()
logging.basicConfig(level=logging.ERROR)
LOGGER.setLevel(logging.INFO)


def send_metrics(event, complianceType, measure):
    NAMESPACE = "config_mterics_agg"
    metric_name = complianceType
    
    dimensionList = [
                    # {
                    # 'Name': 'awsRegion',    
                    # 'Value': event["detail"]["awsRegion"]
                    # },
                    # {
                    # 'Name': 'awsAccountId',    
                    # 'Value': event["detail"]["awsAccountId"]
                    # },
                    # {
                    # 'Name': 'resourceType',    
                    # 'Value': event["detail"]["resourceType"]
                    # },
                    # {
                    # 'Name': 'resourceId',    
                    # 'Value': event["detail"]["resourceId"]
                    # },
                    {
                    'Name': 'configRuleName',    
                    'Value': event["detail"]["configRuleName"]
                    },
    ]

    LOGGER.info(json.dumps(dimensionList))
    cw_client = boto3.client("cloudwatch")
    response = cw_client.put_metric_data(
        Namespace=NAMESPACE,
        MetricData=[
            {
                'MetricName': metric_name,
                'Dimensions': dimensionList,
                'Timestamp': event["detail"]["notificationCreationTime"],
                'Value': measure,
                'Unit': 'Count',
                'StorageResolution': 60
            },
        ]
    )

    LOGGER.info(response)

def lambda_handler(event, context):
    
    LOGGER.debug(event["detail"]["awsRegion"])
    LOGGER.debug(event["detail"]["awsAccountId"])
    LOGGER.debug(event["detail"]["resourceType"])
    LOGGER.debug(event["detail"]["resourceId"])
    LOGGER.debug(event["detail"]["messageType"])
    LOGGER.debug(event["detail"]["configRuleName"])
    LOGGER.debug(event["detail"]["notificationCreationTime"])

    newStatus = event["detail"]["newEvaluationResult"]
    curComplianceType = newStatus["complianceType"]
    send_metrics(event, curComplianceType, 1.0)
    
    prevComplianceType = "UNKNOWN" 
    if "oldEvaluationResult" in event["detail"] :
        LOGGER.debug("There was an old state lets see what we have here")
        oldStatus = event["detail"]["oldEvaluationResult"]
        prevComplianceType = oldStatus["complianceType"]
        send_metrics(event, prevComplianceType, -1.0)
        



if __name__ == "__main__":
    lambda_handler(objMoveFromNonCompToCompEvent, "this is where it starts")
    
    lambda_handler(newObjectCreatedInNonCompStateevent, "this is where it starts")

    lambda_handler(objMoveFromCompToNonCompEvent, "this is where it starts")


    # dimensionList = [{
    #                 'Name': 'configRuleName',    
    #                 'Value': event["detail"]["configRuleName"]
                        
    #                 },
    #                 {
    #                 'Name': 'awsRegion',    
    #                 'Value': event["detail"]["awsRegion"]
    #                 },
    #                 {
    #                 'Name': 'awsAccountId',    
    #                 'Value': event["detail"]["awsAccountId"]
    #                 },
    #                 {
    #                 'Name': 'resourceType',    
    #                 'Value': event["detail"]["resourceType"]
    #                 },
    #                 {
    #                 'Name': 'resourceId',    
    #                 'Value': event["detail"]["resourceId"]
    #                 },
    #                 {
    #                 'Name': 'messageType',    
    #                 'Value': event["detail"]["messageType"]
    #                 },
    #                 {
    #                 'Name': 'complianceType',    
    #                 'Value': curComplianceType
    #                 },
    #                 {
    #                 'Name': 'prevComplianceType',    
    #                 'Value': prevComplianceType
    #                 },
    # ]
