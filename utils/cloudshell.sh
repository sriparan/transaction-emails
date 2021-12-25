#!/usr/bin/bash

set -x
CONFIG=.aws/config
rm ${CONFIG}
> {CONFIG}

aws organizations list-accounts --query Accounts[*].[Id,Name] --output text | while read x y
do
        echo "[profile ${y}]" >> ${CONFIG}
        echo "role_arn=arn:aws:iam::${x}:role/OrganizationAccountAccessRole" >> ${CONFIG}
        echo "credential_source=EcsContainer" >> ${CONFIG}
        echo "" >> ${CONFIG}
done
