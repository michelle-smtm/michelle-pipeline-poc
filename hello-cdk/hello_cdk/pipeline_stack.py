from constructs import Construct
from aws_cdk import (
    Stack,
    pipelines as pipelines,
    aws_codepipeline_actions,
    aws_codepipeline,
    aws_codebuild as codebuild,
    aws_lambda
)
from hello_cdk.deploy_stage import DeployStage

class PipelineStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        source_artifact = aws_codepipeline.Artifact

        #repository = aws_ecr.Repository.from_repository_name(self, "CdkEcrRepo", "codepipeline-poc-repo")
        #input_ecr = pipelines.CodePipelineSource.ecr(repository)

        input_artifact = pipelines.CodePipelineSource.connection("michelle-smtm/michelle-pipeline-poc", "main", connection_arn="arn:aws:codestar-connections:us-east-1:062621911729:connection/78b6f50a-09b4-470a-81a3-9351f51411fc")
        # Pipeline code will go here
        my_pipeline = pipelines.CodePipeline(
            self,
            "Pipeline",
            synth=pipelines.ShellStep(
                "Synth",
                input=input_artifact,
                commands=[
                    "cd hello-cdk",
                    "npm install -g aws-cdk",  # Installs the cdk cli on Codebuild
                    "pip install -r requirements.txt",  # Instructs Codebuild to install required packages
                    "cdk synth",
                ],
                primary_output_directory= 'hello-cdk/cdk.out',
            )
        )

        #build_action = aws_codepipeline_actions.CodeBuildAction(action_name='DockerBuildImages', input=input_artifact, project=pipeline_project)
        #build_stage = pipeline.add_stage(aws_codepipeline.StageProps( stage_name='Build', actions= build_action))

        deploy = DeployStage(self, "Deploy")
        deploy_stage = my_pipeline.add_stage(deploy)

        lambda_action = aws_codepipeline_actions.LambdaInvokeAction(
            action_name="IntegTests",
            user_parameters_string="hello",
            lambda_=aws_lambda.Function.from_function_arn(
                self,
                id="TestLambda",
                function_arn="arn:aws:lambda:us-east-1:062621911729:function:MyLambdaFunctionForAWSCodePipeline")
        )
        

