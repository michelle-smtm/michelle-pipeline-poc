from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_ec2 as ec2, 
    aws_ecs as ecs,
    aws_ecr_assets,
    aws_ecs_patterns as ecs_pattern,
    aws_ecr as ecr,
)
from constructs import Construct
import aws_cdk as cdk
import aws_cdk.aws_s3 as s3

from aws_cdk.aws_ecr_assets import DockerImageAsset, NetworkMode

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
        asset = DockerImageAsset(self, "MyBuildImage",
            directory= "../home-outer",
            file="Dockerfile",
            network_mode=NetworkMode.HOST
        )

    #     image = DockerImageAsset(this, "BackendImage", {
    #   directory: join(__dirname, "..", "service"),
    # });

        task_definition = ecs.FargateTaskDefinition( self, "cdk-task-def", cpu=512, memory_limit_mib=2048)
        repository = ecr.Repository.from_repository_name(self, "CdkEcrRepo", "codepipeline-poc-repo")

        image = ecs.ContainerImage.from_docker_image_asset(asset)
        container = task_definition.add_container( "cdk-container", image=image)

        fargate = ecs.FargateService(self, "CdkCodePipelineEcsService",
            cluster=cluster,            # Required
            task_definition=task_definition,
            desired_count=1,      # Default is 512
            assign_public_ip=True)  
