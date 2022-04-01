import boto3
from colorama import Fore, Style
from functions import region_parser

def create_client(botoconfig, session, region):
    client = session.client('rds', config=botoconfig, region_name=region)
    return client

def help():
    print(Fore.YELLOW + "\n================================================================================================" + Style.RESET_ALL)
    print("[+] Module Description:\n")
    print("\tThis module will enumerate available RDS Instances")
    print("\tpresent on the account.")

    print("\n[+] Module Functionality:\n")
    print("\tThe module will call 'describe_db_instances' and ")
    print("\tprint the db names as they are returned.")

    print(Fore.YELLOW + "================================================================================================" + Style.RESET_ALL)

def get_optional_regions():
    region = region_parser.Region()
    optional_region = region.region_select()

    return optional_region

def get_rds_instance_list(botosession, session, region):
    rds_client = create_client(botosession, session, region)
    response = rds_client.describe_db_instances()

    return response

def main(botoconfig, session, selected_session):
    print(Fore.YELLOW + "\n================================================================================================" + Style.RESET_ALL)
    print("[+] Starting RDS Enumeration module...")
    print("[+] Select region to retrieve instances...")
    
    rds_instance_list = []

    region_option = get_optional_regions()

    if region_option:
        for region in region_option:
            print("[+] Enumerating RDS instances for "+Fore.YELLOW+"{}".format(region)+"...."+Style.RESET_ALL)
            try:
                rds_instances = get_rds_instance_list(botoconfig, session, region)
                if rds_instances['DBInstances'] == []:
                    pass
                else:
                    for instance in rds_instances['DBInstances']:
                        print("[+] Instance: "+Fore.GREEN+"{}".format(instance['DBInstanceIdentifier'])+Style.RESET_ALL)
                        rds_instance_list.append(instance)
            except:
                pass
    
    return rds_instance_list 