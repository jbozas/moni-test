import requests
import json

# This method make the request to the API
def ItsApproved(dni):
    url = f'https://api.moni.com.ar/api/v4/scoring/pre-score/{dni}'
    headers = {'credential': 'ZGpzOTAzaWZuc2Zpb25kZnNubm5u'}
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        json_format = json.loads(res.text)
        if json_format['status'] == 'approve' and not(json_format['has_error']):
            return True
    return False

