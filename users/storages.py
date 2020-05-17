# custom settings class in yourapp/storages.py
from storages.backends.s3boto3 import S3Boto3Storage
class PublicStorage(S3Boto3Storage):
    default_acl = "public-read"
