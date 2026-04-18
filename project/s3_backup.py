"""
This script will create daily backups, S3 bucket, and then add daily backups from local device to AWS S3 and display all the 
existing buckets in AWS S3.
boto3 -> used to do AWS tasks using Python 
"""

import boto3
import os
import datetime
import shutil

s3 = boto3.resource('s3')

def show_bucket(s3):
    print("List of existing S3 Buckets: ")
    for bucket in s3.buckets.all():
        print(bucket.name)
        
        
def create_buckets(s3):
    s3.create_bucket(Bucket='backup-from-python801080', CreateBucketConfiguration={'LocationConstraint': 'us-east-2'},)
    print("Bucket from terminal created successfully...!!!")
    print(" ")
    
# variables for creating backup
source = "/mnt/d/DevOps/Python/practice"
destination = "/mnt/d/DevOps/Python/project/backups"
    
today = datetime.date.today()
backup_file = os.path.join(destination, f"backup_{today}.tar.gz")

def create_backup(source, destination):
    # global today
    # global backup_file 
    shutil.make_archive(backup_file.replace(".tar.gz", ""), 'gztar', source )
    print("Backup Created Successfully...!!!")
    print(" ")

    
def upload_backup(s3, backup_file, bucket_name, key_name):
    data = open(backup_file, 'rb') #this will read the given files in binary format
    s3.Bucket(bucket_name).put_object(Key=key_name, Body=data)
    print("Backup Uploaded Successfully to AWS S3...!!!")
    print(" ")
    
    
# variables for uploading backups 
bucket_name = 'backup-from-python801080'
region = 'us-east-2'
# file_name = 'project/backups/backup_2026-04-17.tar.gz'
    
create_buckets(s3)
create_backup(source, destination)
upload_backup(s3, backup_file, bucket_name, "my_backup.tar.gz")
show_bucket(s3)