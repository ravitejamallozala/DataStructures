import math
from decimal import Decimal


def avgRotorSpeed(statusQuery, parentId):
    import requests
    base_uri = 'https://jsonmock.hackerrank.com/api/iot_devices/search'
    params = dict(
        status=None,
        page=None)
    resp = requests.get(base_uri, params=params)
    resp_data = resp.json()
    total_pages = resp_data.get('total_pages', None)
    total_devices = 0
    sum_of_speeds = 0
    for page in range(2, total_pages + 1):
        params['page'] = page

        resp = requests.get(base_uri, params=params)
        resp_data = resp.json()
        for record in resp_data['data']:
            # print(record)
            if ('status' in record and record['status'] == statusQuery) and (
                    'parent' in record and record['parent'] and 'id' in record['parent'] and record['parent'][
                'id'] == parentId):
                total_devices += 1
                sum_of_speeds += record['operatingParams']['rotorSpeed']
    final_result = 0
    if total_devices:
        final_result = math.floor(sum_of_speeds / total_devices)

    return final_result


avgRotorSpeed("RUNNING", 7)
