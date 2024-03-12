import boto3

def check_imdsv2_support(instance_id):
    ec2_client = boto3.client('ec2')
    response = ec2_client.describe_instance_attribute(
        InstanceId=instance_id,
        Attribute='instanceMetadataOptions'
    )
    imdsv2_support = response['InstanceMetadataOptions']['HttpTokens']
    return imdsv2_support == 'required'

def update_instance_metadata(instance_id):
    ec2_client = boto3.client('ec2')
    response = ec2_client.modify_instance_metadata_options(
        InstanceId=instance_id,
        HttpTokens='required',
        HttpPutResponseHopLimit=1
    )
    print(f"Instance {instance_id} updated to use IMDSv2.")

def main():
    instance_id = 'your_instance_id_here'  # Replace with your EC2 instance ID
    
    if check_imdsv2_support(instance_id):
        print(f"Instance {instance_id} is already updated to use IMDSv2.")
    else:
        update_instance_metadata(instance_id)

if __name__ == "__main__":
    main()
