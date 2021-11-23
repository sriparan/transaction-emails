package com.myorg;

import software.amazon.awscdk.core.CfnParameter;
import software.amazon.awscdk.core.Construct;
import software.amazon.awscdk.core.Stack;
import software.amazon.awscdk.core.StackProps;

import software.amazon.awscdk.services.dynamodb.*;
import software.amazon.awscdk.services.lambda.Code;
import software.amazon.awscdk.services.lambda.CodeConfig;
import software.amazon.awscdk.services.lambda.Function;
import software.amazon.awscdk.services.lambda.Runtime;
import software.amazon.awscdk.core.RemovalPolicy;

public class ApiStack extends Stack {
    public ApiStack(final Construct scope, final String id) {
        this(scope, id, null);
    }

    public ApiStack(final Construct scope, final String id, final StackProps props) {
        super(scope, id, props);
        CfnParameter tableName = CfnParameter.Builder.create(this, "dynamoDBName").type("String")
                .description("The name of the dynamodb Table").build();

        final Table table = Table.Builder.create(this, "tableId").tableName(tableName.getValueAsString())
                .removalPolicy(RemovalPolicy.DESTROY).billingMode(BillingMode.PROVISIONED)
                .stream(StreamViewType.NEW_IMAGE)
                .partitionKey(Attribute.builder().name("endpoint").type(AttributeType.STRING).build()).build();

        final Code code = Code.fromInline("This is so not the code");
        // CodeConfig.builder().inlineCode("this is code").build();
        final Function function = Function.Builder.create(this, "change_listener").functionName("start_journey")
                .handler("somethign to do").code(code).runtime(Runtime.PYTHON_3_7).build();
        // The code that defines your stack goes here
    }
}
