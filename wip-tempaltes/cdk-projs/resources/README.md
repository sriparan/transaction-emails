# Welcome to your CDK TypeScript project

Basic code to test s3 triggers
Created a bucket
Enabled inventory -> Not needed.
Added 2 triggers
-> object create to call lambda
--object delete to add the event to a queue

Lambda function when invoked on create events..deletes the object that triggered the event.

Test to add objects to bucket and read the items off of the queue.

If every thing worked..the s3 bucket will have no objects at the end of the tests.
Focus was the trigerring mechanism and Typescript/CDK learning.

## Useful commands

- `npm run build` compile typescript to js
- `npm run watch` watch for changes and compile
- `npm run test` perform the jest unit tests
- `cdk deploy` deploy this stack to your default AWS account/region
- `cdk diff` compare deployed stack with current state
- `cdk synth` emits the synthesized CloudFormation template
