from constructs import Construct
import aws_cdk as cdk
import aws_cdk.aws_s3 as s3
from aws_cdk import (
    Stage 
)

from hello_cdk.hello_cdk_stack import HelloCdkStack

class DeployStage(Stage):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        # The code that defines your stack goes here
        service = HelloCdkStack(self, 'ServiceStack') 
