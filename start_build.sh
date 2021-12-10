git commit -a -m "Demo change adding phone number"
git push
sleep 10
aws codepipeline list-pipeline-executions --pipeline-name transaction-emails --max-items 1 --query "pipelineExecutionSummaries[0].[pipelineExecutionId, status,lastUpdateTime]"
