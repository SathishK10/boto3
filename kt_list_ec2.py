import boto3
import sys


region = sys.argv[1]
accesskey = sys.argv[2]
secretkey = sys.argv[3]


Client = boto3.client('ec2',
                      region_name =region,
                      aws_access_key_id =accesskey,
                      aws_secret_access_key =secretkey)

listec2 = Client.describe_instances()

##print(listec2['Reservations'])

for output in listec2['Reservations']:
    for output2 in output['Instances']:
        for output3 in output2['Tags']:
            print(output2['InstanceId'],output2['LaunchTime'],'[',output3['Key'],':',output3['Value'],']')
