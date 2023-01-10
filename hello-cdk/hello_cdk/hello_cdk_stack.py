from aws_cdk import (
    Stack,
    aws_ec2 as ec2, 
    aws_ecs as ecs,
    aws_ecr as ecr,
)
from constructs import Construct

from aws_cdk.aws_ecr_assets import DockerImageAsset, NetworkMode

class HelloCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc = ec2.Vpc(self, "CodePipelineEcsVpc", max_azs=3)     # default is all AZs in region

        cluster = ecs.Cluster(self, "CodePipelineEcsCluster", vpc=vpc, cluster_name="BetaCluster")
        asset = DockerImageAsset(self, "MyBuildImage",
            directory= "../home-outer",
            file="Dockerfile",
            network_mode=NetworkMode.HOST
        )

        task_definition = ecs.FargateTaskDefinition( self, "cdk-task-def", cpu=512, memory_limit_mib=2048)
        repository = ecr.Repository.from_repository_name(self, "CdkEcrRepo", "codepipeline-poc-repo")

        image = ecs.ContainerImage.from_docker_image_asset(asset)
        container = task_definition.add_container( "cdk-container", image=image, container_name="BetaContainer")

        fargate = ecs.FargateService(self, "CdkCodePipelineEcsService",
            service_name="BetaService",
            cluster=cluster,            
            task_definition=task_definition,
            desired_count=1,      
            assign_public_ip=True)  
