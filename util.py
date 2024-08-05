from apiCaller import api_caller

def get_report_data(access_token, sql):
    print("\nGetting report data...")
    report_payload = api_caller(access_token, {
        "method": "POST",
        "endpoint": "/Report",
        "payload": [{
            "sql": sql,
            "_loadreportonly": True
        }]
    })
    return report_payload['report']['rows']
