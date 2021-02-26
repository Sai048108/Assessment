PROCESS:
in this Automate process it will create the KEY_PAIR, Security group, EC2 instance, and copy the files into ec2 instance attached volumes
installations:

```
install python
install pip
install boto3 using pip
install yaml using pip
install aws cli
```
export aws configurations on terminal
```
'ec2',
aws_access_key_id = 'AKIATA5Hxxxxxxxxxxx3',
aws_secret_access_key = 'Zn2xxxxxxxxxxxH/eRKsxWJ/Y+B6',
region_name = 'us-east-2'
)
```

update the required below` fields in ec2.yaml file like

```
security_group id
image_id
