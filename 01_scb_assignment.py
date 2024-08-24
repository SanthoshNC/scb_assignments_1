"""
Author: Santhosh NC
Purpose: Solution for the provided assignment
"""

import json
from pymongo import MongoClient, UpdateOne, errors
import requests
import uuid

# Get the JSON file from GitHub
# Original URL : https://github.com/codingo/Ransomware-Json-Dataset/blob/master/ransomware_overview.json
url = 'https://raw.githubusercontent.com/codingo/Ransomware-Json-Dataset/master/ransomware_overview.json'
response = requests.get(url)
data = response.json()

# To read the file from local file system
# with open('ransomware_overview.json') as f:
#     file_data = json.load(f)

# Connect to the local MongoDB
client = MongoClient('localhost', 27017)
# this will create the database and collection automatically with the given name     
db = client['scb_assignment_security_data']
collection = db['scb_assignment_ransomware_overview']

# To validate the given conditions
"""
This function will receive the data from json file and will perform the validation, Here I considered name as primary_key
"""
def validate_data(item):
    if not item.get('name') or not isinstance(item['name'], list) or not item['name'][0]:
        item['name'] = [str(uuid.uuid4())]  # Generate a unique ID if 'name' is missing or invalid
    return item

# Prepare a list of operations for bulk write
operations = []

for item in data:
    cleaned_data = validate_data(item)
    operations.append(
        UpdateOne(
            {'name': cleaned_data['name']},  # Find documents with the same 'name'
            {'$set': cleaned_data},           # Update the document with cleaned data
            upsert=True                       # Insert if the document does not exist
        )
    )

# Perform the bulk write operation
try:
    if operations:
        result = collection.bulk_write(operations)
        print(f"Bulk write operation completed. {result.matched_count} matched, {result.modified_count} modified, {result.upserted_count} upserted.")
except errors.BulkWriteError as bwe:
    print(f"Bulk write error: {bwe.details}")
except errors.PyMongoError as e:
    print(f"An error occurred: {e}")

# if pymongo < 3.0, use insert()
# collection_currency.insert(file_data)
# if pymongo >= 3.0 use insert_one() for inserting one document
# collection_currency.insert_one(file_data)
# if pymongo >= 3.0 use insert_many() for inserting many documents
# collection_currency.insert_many(file_data)
# unique = { each['Name'] : each for each in te }.values()


# Close the MongoDB connection
client.close()
