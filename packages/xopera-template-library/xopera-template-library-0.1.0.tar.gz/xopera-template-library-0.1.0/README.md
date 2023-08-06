### Examples:
```
template-library setup
template-library login --username "username1" --password "password1"
template-library template get --version_id 4 --path test-folder --public_access True
template-library template list --name AwsLambda --public_access True
template-library template version list --template_id 4
template save --name AwsLambda --path example/AwsLambdaFunction --public_access False --version 0.0.4
``` 


### Particle to upload structure
 ```        
|-- ParticleFolder
        |-- files
            |-- create.yml
            |-- undeploy.yml
        |-- NodeType.tosca
```