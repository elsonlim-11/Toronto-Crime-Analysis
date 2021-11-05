import json
import os
from azure.storage.blob import BlobServiceClient

## Get Azure storage key
keyPath = f"{os.getcwd()}\\ACCESS_KEY.JSON"

with open(keyPath,'r') as keyFile:
    keyDict = json.load(keyFile)
    STORAGE_NAME = keyDict['STORAGE_NAME']
    STORAGE_KEY = keyDict['STORAGE_KEY']
    STORAGE_CONNECTION = keyDict['STORAGE_CONNECTION']

