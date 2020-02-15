#!/usr/bin/python
from google.cloud import storage
import os

def upload_to_bucket(blob_name, path_to_file, bucket_name):
    """ Upload data to a bucket"""

    # Explicitly use service account credentials by specifying the private key
    # file.
    CRED_PATH = os.environ['CRED_PATH']
    storage_client = storage.Client.from_service_account_json(
        CRED_PATH)

    #print(buckets = list(storage_client.list_buckets())

    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.upload_from_filename(path_to_file)
    blob.make_public()

    #returns a public url
    #return blob.public_url

#upload_to_bucket("headlines.txt", "./headlines.txt", "max123")
