# infra_stack.py
from aws_cdk import App, Stack
import aws_cdk.aws_s3 as s3
import aws_cdk.aws_iam as iam
import aws_cdk.aws_lambda as lb
import aws_cdk.aws_apigateway as apig
from constructs import Construct


class InfraStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        #S3 Bucket
        s3bucket=s3.Bucket(self, "bankingapps3logicid", 
                              bucket_name="banking-app-bucket"
                              )
        #IAM Role
        iamrole=iam.Role(self,'bankingappiamrole',role_name='bankingapps3iamrole',description='Iam role for the lambda to access s3 bucket',assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"))
        iamrole.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name('AmazonS3FullAccess'))

        #Lambda
        awslambda=lb.Function(self,'bankingapplambdafunction',role=iamrole,runtime=lb.Runtime.PYTHON_3_9,code=lb.Code.from_asset('../services/'),handler='lambda_function.lambda_handler')
        # Your stack definition here

        #apigateway
        bankingrestapi=apig.LambdaRestApi(self,"bankingrestapi",handler=awslambda,rest_api_name='bankingrestapi',deploy=True,proxy=False)
        banhstatus=bankingrestapi.root.add_resource('banhstatus')
        banhstatus.add_method('GET')
app =App()
InfraStack(app, "Bankingappstack")