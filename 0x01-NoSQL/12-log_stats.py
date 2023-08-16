#!/usr/bin/env python3
"""Module for 12-log_stats.py"""
from pymongo import MongoClient
from typing import List


# connect to mongodb server
client: MongoClient = MongoClient(host="localhost", port=27017)
# create database
db = client.logs
# create a collection
collection = db.nginx
# count all document(logs) in the collection
sum_logs: int = collection.count_documents({})
# print out the logs
print("{} logs".format(sum_logs))
# check status
status: int = collection.count_documents({"path": "/status"})
print("methods:")
# Initialise methods to ["GET", "POST", "PUT", "PATCH", "DELETE"]
methods: List[string] = ["GET", "POST", "PUT", "PATCH", "DELETE"]
# loop over the list methods
for method in methods:
    method = collection.document_counts({"methods": method})
    print(f"\tmethod {method}: {method_count}")
    # print out the status
    print(f"{status} status check")
