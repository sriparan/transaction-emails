Run the vpc config first . 2 in region and 2 local zone subnets.
then create the eks cluster in the regional subnets. exclude the localzone
Then configure the instances and loadlancer to deploy in the local zone subnets.
Thenuse the cli to register the nodes into the cluster.

https://docs.aws.amazon.com/eks/latest/userguide/launch-workers.html
infra template for the vpc creation.
eks_nodegroup for the unmanaged nodee group for eks in the localzonethen auth-cm to attach the nodes to the cluster.
