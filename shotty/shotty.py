import boto3

if __name__ == '__main__':
    session2 = boto3.Session(region_name='eu-west-1',profile_name='shotty')
    ec2 = session2.resource('ec2')

    for i in ec2.instances.all():
        print(i)
