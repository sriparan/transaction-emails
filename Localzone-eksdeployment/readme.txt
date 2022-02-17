Run the vpc config first . 
Create subnets : 2 in region and 2 local zone subnets.
create the eks cluster with the control  plane interfaces in the subnet in the main region and none in the local zone

Thing to note EKS ownership is to the role that creates the cluster.
So if you want to access the cluster thought the cli...
you need to make sure the role that was provided during EKS cluster create is the same one used to manage the cluster.

If cluster is private and you need to have a host / cloud shell then ensure that the role you would use is mentioned on the cluster owners.


configure command line tools
https://docs.aws.amazon.com/eks/latest/userguide/getting-started-eksctl.html


To configure the clients you need the eksctl and cubectl
these command work with one cluster at a time and the cluster they want to manage have a few parameters that you need to provide.
to simplify this , these clis use config files to manage the target clusters and the corrosponding configuration of the clusters.


aws eks <update config> is a cli that can help you generate the eks config file on your local/ec2/shell node.
once this file is created you get to  the cli tools.


Instructions to deploy the ASG with nodes.
https://docs.aws.amazon.com/eks/latest/userguide/launch-workers.html

infra template for the vpc creation.
eks_nodegroup for the unmanaged nodee group for eks in the localzonethen auth-cm to attach the nodes to the cluster.
