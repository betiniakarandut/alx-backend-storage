#!/usr/bin/env bash
"""Module for 12-log_stats.py"""
from pymongo import MongoClient
from typing import List


# nginx stats
client: MongoClient = MongoClient(host="localhost", port=27017)
db = client.logs
collection = db.nginx
sum_logs: int = collection.count_documents({})
print("{} logs".format(sum_logs))
status: int = collection.count_documents({"path": "/status"})
print("methods:")
methods: List[string] = ["GET", "POST", "PUT", "PATCH", "DELETE"]
for method in methods:
    method = collection.document_counts({"methods": method})
    print(f"\tmethod {method}: {method_count}")
    print(f"{status} status check")
