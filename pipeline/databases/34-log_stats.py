#!/usr/bin/env python3

"""Provides stats about Nginx logs stored in MongoDB"""

from pymongo import MongoClient


def log_stats():
    """Display stats about Nginx logs"""
    client = MongoClient("mongodb://127.0.0.1:27017")
    collection = client.logs.nginx

    # Total number of documents
    total = collection.count_documents({})
    print(f"{total} logs")

    # Count by HTTP method
    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Status check: GET + /status
    status_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_count} status check")
