from elasticsearch import Elasticsearch
from datetime import datetime, timedelta
import json

# Connect to Elasticsearch
es = Elasticsearch("http://localhost:9200")
info = es.info()
print("Connected to:", info['cluster_name'])

# Time range for queries
now = datetime.utcnow()
past = now - timedelta(hours=24)

# 🔐 Failed Login Events Function
def Failed_Logins():
    query = {
        "query": {
            "bool": {
                "must": [
                    {"match": {"event.code": "4625"}},
                    {"range": {
                        "@timestamp": {
                            "gte": past.isoformat(),
                            "lte": now.isoformat()
                        }}
                    }
                ]
            }
        }
    }

    res = es.search(index="winlogbeat-*", body=query)
    count_res = es.count(index="winlogbeat-*", body=query)

    messages = []  # Store messages here
    for hit in res["hits"]["hits"]:
        message = hit["_source"].get("message", "No message")
        print(message)
        messages.append(message)

    print("Failed logins in last 24 Hours:", count_res['count'])

    result = f"Failed logins in last 24 Hours: {count_res['count']}"
    return result, messages

# 🛡️ Security Events Function
def Security():
    query = {
        "query": {
            "bool": {
                "must": [
                    {"match": {"event.module": "security"}},
                    {"range": {
                        "@timestamp": {
                            "gte": past.isoformat(),
                            "lte": now.isoformat()
                        }}
                    }
                ]
            }
        }
    }

    count_res = es.count(index="winlogbeat-*", body=query)
    Search_res = es.search(index="winlogbeat-*", body=query)
    messages = []
    if 'hits' in Search_res and 'hits' in Search_res['hits']:
        for hit in Search_res['hits']['hits']:
            if '_source' in hit and 'message' in hit['_source']:
                messages.append(hit['_source']['message'])
    print("Security events in last 24 Hours:", count_res['count'])
    result = f"Security events in last 24 Hours: {count_res['count']}"
    return result, messages

# Run functions
# Failed_Logins()
# Security()
