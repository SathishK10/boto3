import boto3

Client = boto3.client('ec2',
                      region_name ='ap-southeast-1',
                      aws_access_key_id ='AKIAQGBI5HETXWMGUP5G',
                      aws_secret_access_key ='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', )

listec2 = Client.describe_instances()

##print(listec2['Reservations'])

for output in listec2['Reservations']:
    for output2 in output['Instances']:
        for output3 in output2['Tags']:
            print(output2['InstanceId'],output2['LaunchTime'],'[',output3['Key'],':',output3['Value'],']')
