#!/usr/bin/env python3

"""adding the top 10 of the most present IPs in the collection nginx of the database logs"""

ip_logs = nginx_collection.aggregate(
    [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10},
    ]
)
for ip in ip_logs:
    print("    {}: {}".format(ip.get("_id"), ip.get("count")))
