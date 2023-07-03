import sys, os
import numpy as np
from time import sleep
import requests
import json
import pandas as pd
from datetime import datetime, timedelta

def maple_API(key):
    url = 'https://public.api.nexon.com/openapi/maplestory/v1/cube-use-results'

    start_dates = "2022-11-25"
    last_dates = "2023-07-02"
    a = datetime.strptime(start_dates,"%Y-%m-%d")
    print('a:',a)
    print(type(a))
    b = a.strftime("%Y-%m-%d")
    print('b:',b)
    print(type(b))

    start_date = datetime.strptime("2023-07-01","%Y-%m-%d")
    last_date = datetime.strptime(last_dates,"%Y-%m-%d")

    # 큐브기록 저장
    total_history = []
    while start_date<= last_date:
        dates = start_date.strftime("%Y-%m-%d")
        headers = {
            'authorization' : 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJYLUFwcC1SYXRlLUxpbWl0IjoiNTAwOjEwIiwiYWNjb3VudF9pZCI6IjE3Nzg1MjM0NzMiLCJhdXRoX2lkIjoiMiIsImV4cCI6MTcwMzkwNjI2MSwiaWF0IjoxNjg4MzU0MjYxLCJuYmYiOjE2ODgzNTQyNjEsInNlcnZpY2VfaWQiOiI0MzAwMTEzOTciLCJ0b2tlbl90eXBlIjoiQWNjZXNzVG9rZW4ifQ.rOBbtpfB-Tv5xKIHb6uJ9I1YdMZVG6RMqwhl3ds_31s'
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
    
    # 데이터	                            유형	                             설명
    # id	                                String	                            큐브 사용 내역에 대한 고유 식별자
    # character_name	                    String	                            캐릭터이름 
    # create_date	                        String	                            큐브 사용 날짜
    # cube_type	                            String	                            사용한 큐브
    # item_upgrade_result	                String	                            큐브 사용 결과(등업 결과)
    # miracle_time_flag	                    String	                            미라클 타임 적용 여부
    # item_equip_part	                    String	                            장비 분류
    # item_level	                        integer	                            장비 레벨
    # target_item	                        String	                            큐브를 사용한 장비
    # potential_option_grade	            String	                            잠재능력 등급
    # additional_potential_option_grade	    String	                            에디셔널 잠재능력 등급
    # upgradeguarantee	                    Boolean	                            천장에 도달하여 확정 등급 상승한 여부
    # upgradeguaranteecount	                Integer	                            현재까지 쌓은 스택
    # before_potential_options	            object array(CubeResultOptionDTO)	큐브사용전 잠재능력 옵션
    # before_additional_potential_options	object array(CubeResultOptionDTO)	큐브사용전 에디셔널 잠재능력 옵션
    # after_potential_options	            object array(CubeResultOptionDTO)	큐브 사용 후 잠재능력 옵션
    # after_additional_potential_options	object array(CubeResultOptionDTO)	큐브 사용 후 에디셔널 잠재능력 옵션
    # value                                 string                              옵션이름
    # grade                                 string                              옵션등급

    tf = total_history[0]
    print(tf['character_name'])

maple_API("a")