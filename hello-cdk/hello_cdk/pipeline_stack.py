from constructs import Construct
from aws_cdk import (
    Stack,
    pipelines as pipelines,
    aws_codebuild as codebuild
)

class PipelineStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Pipeline code will go here
        pipeline = pipelines.CodePipeline(
            self,
            "Pipeline",
            synth=pipelines.ShellStep(
                "Synth",
                input=pipelines.CodePipelineSource.connection("michelle-smtm/michelle-pipeline-poc", "cdk-pipeline", connection_arn="arn:aws:codestar-connections:us-east-1:062621911729:connection/78b6f50a-09b4-470a-81a3-9351f51411fc"
           ),
                commands=[
                    "npm install -g aws-cdk",  # Installs the cdk cli on Codebuild
                    "pip install -r hello-cdk/requirements.txt",  # Instructs Codebuild to install required packages
                    "cdk synth",
                ],
                primary_output_directory= 'hello-cdk/cdk.out',
            ),
        )