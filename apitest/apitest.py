import sys, os
import numpy as np
from time import sleep
import requests
import json
import pandas as pd
from datetime import datetime, timedelta

def maple_API(key,start_date,last_date):
    url = 'https://public.api.nexon.com/openapi/maplestory/v1/cube-use-results'

    start_date = datetime.strptime(start_date,"%Y-%m-%d")
    last_date = datetime.strptime(last_date,"%Y-%m-%d")

    # 큐브기록 저장
    total_history = []
    while start_date <= last_date:
        dates = start_date.strftime("%Y-%m-%d")
        headers = {
            'authorization' : key
        }
        params = {
            'count' : 1000,
            'date' : dates,
            'cursor' : ''
        }
        res = requests.get(url,headers=headers,params=params)
        data = res.json()
        if data['cube_histories']:
            for h in data['cube_histories']:
                total_history.append(h)
        start_date += timedelta(days=1)
    
    return total_history