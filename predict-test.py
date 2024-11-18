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

probability = response['attended_probability']
attended = response['attended']

if attended:
    print(f"Keep space for member {member_id}. Likelihood of attendance: {probability:.2f}.")
else:
    print(f"Make space for another member. Likelihood of attendance for {member_id}: {probability:.2f}.")