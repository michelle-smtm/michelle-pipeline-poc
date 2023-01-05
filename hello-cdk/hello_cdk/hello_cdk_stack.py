from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_ec2 as ec2, 
    aws_ecs as ecs,
    aws_ecs_patterns as ecs_pattern,
    aws_ecr as ecr,
)
from constructs import Construct
import aws_cdk as cdk
import aws_cdk.aws_s3 as s3

class HelloCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "HelloCdkQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
        vpc = ec2.Vpc(self, "CodePipelineEcsVpc", max_azs=3)     # default is all AZs in region

        cluster = ecs.Cluster(self, "CodePipelineEcsCluster", vpc=vpc)

        repository = ecr.Repository.from_repository_name(self, "CdkEcrRepo", "codepipeline-poc-repo")

        ecs_pattern.ApplicationLoadBalancedFargateService(self, "CdkCodePipelineEcsService",
            cluster=cluster,            # Required
            cpu=256,                    # Default is 256
            desired_count=1,            # Default is 1
            task_image_options=ecs_pattern.ApplicationLoadBalancedTaskImageOptions(
                image=ecs.ContainerImage.from_ecr_repository(repository)),
            memory_limit_mib=512,      # Default is 512
            public_load_balancer=True)  # Default is True
