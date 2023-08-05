from localstack.utils.aws import aws_models
BmQFH=super
BmQFD=None
BmQFn=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  BmQFH(LambdaLayer,self).__init__(arn)
  self.cwd=BmQFD
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class RDSDatabase(aws_models.Component):
 def __init__(self,BmQFn,env=BmQFD):
  BmQFH(RDSDatabase,self).__init__(BmQFn,env=env)
 def name(self):
  return self.BmQFn.split(':')[-1]
# Created by pyminifier (https://github.com/liftoff/pyminifier)
