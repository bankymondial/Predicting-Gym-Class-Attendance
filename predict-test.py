#!/usr/bin/env python
# coding: utf-8

import requests


url = 'http://localhost:5454/predict'

member_id = 'abc-456'
member = {
    "category": "HIIT",
    "day_of_week": "Sat",
    "days_before": 13,
    "months_as_member": 36,
    "time": "AM",
    "weight": 85
}


response = requests.post(url, json=member).json()
print(response)

if response['attended'] == True:
    print('keep space for member %s' % member_id)
else:
    print('make space for another member')