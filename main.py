from dotenv import load_dotenv
from auth import get_access_token
from util import get_report_data
from apiCaller import api_caller

load_dotenv()

if __name__ == "__main__":
    access_token = get_access_token()

    sql = """
        SELECT
            FIELDINFO.fiid
        FROM
            FIELDINFO
        WHERE
            FIELDINFO.FICustom = 1
            AND FIELDINFO.FIusage = 1
            AND FIELDINFO.finame NOT IN ('CFKBCATS')
            AND FIELDINFO.fihidefromfilters IS NULL
    """

    # Load the data from the SQL query
    report_data = get_report_data(access_token, sql)

    for row_number in range(len(report_data)):
        print(f"\nRow number: {row_number + 1} ({row_number + 1}/{len(report_data)}) ({round(((row_number + 1) / len(report_data)) * 100)}%)")

        api_caller(access_token, {
            "method": "POST",
            "endpoint": "/FieldInfo",
            "payload": [
                {
                    "hide_from_filters": True,
                    "id": report_data[row_number]["fiid"]
                }
            ]
        })
