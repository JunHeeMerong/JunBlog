from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json
from django.db.models import Q
# from .models import modelname
from django.http import Http404, JsonResponse, HttpResponse
from rest_framework import status
from rest_framework.serializers import Serializer
from apitest.apitest import maple_API
from apitest.models import Cube
from datetime import datetime,timedelta

from blog.models import Post
from blog.serializers import PostSerializer
# Create your views here.

@api_view(['GET'])
def apitest(request):
    if request.method == 'GET':
        datas = Post.objects.all()
        serializer = PostSerializer(datas,many=True)
        return Response(serializer.data)

@api_view(['GET'])
def mapleapitest(request):
    if request.method == 'GET':
        key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJYLUFwcC1SYXRlLUxpbWl0IjoiNTAwOjEwIiwiYWNjb3VudF9pZCI6IjE3Nzg1MjM0NzMiLCJhdXRoX2lkIjoiMiIsImV4cCI6MTcwMzkwNjI2MSwiaWF0IjoxNjg4MzU0MjYxLCJuYmYiOjE2ODgzNTQyNjEsInNlcnZpY2VfaWQiOiI0MzAwMTEzOTciLCJ0b2tlbl90eXBlIjoiQWNjZXNzVG9rZW4ifQ.rOBbtpfB-Tv5xKIHb6uJ9I1YdMZVG6RMqwhl3ds_31s'
        start_date = '2023-07-01'
        last_date = '2023-07-02'
        datas = maple_API(key,start_date,last_date)
        return Response(datas)
    
def cubeapi(request):
    return render(request,'apitest/main.html')

def cubesave(cubedata,key):
    if cubedata:
        for c in cubedata:
            if len(c['before_potential_options'])==3:
                Cube.objects.create(
                    key = key,
                    character_name = c['character_name'],
                    create_date = c['create_date'],
                    cube_type = c['cube_type'],
                    item_upgrade_result = c['item_upgrade_result'],
                    item_level = c['item_level'],
                    target_item = c['target_item'],
                    potential_option_grade = c['potential_option_grade'],
                    before_options_value1 = c['before_potential_options'][0]['value'],
                    before_options_grade1 = c['before_potential_options'][0]['grade'],
                    before_options_value2 = c['before_potential_options'][1]['value'],
                    before_options_grade2 = c['before_potential_options'][1]['grade'],
                    before_options_value3 = c['before_potential_options'][2]['value'],
                    before_options_grade3 = c['before_potential_options'][2]['grade'],
                    after_options_value1 = c['after_potential_options'][0]['value'],
                    after_options_grade1 = c['after_potential_options'][0]['grade'],
                    after_options_value2 = c['after_potential_options'][1]['value'],
                    after_options_grade2 = c['after_potential_options'][1]['grade'],
                    after_options_value3 = c['after_potential_options'][2]['value'],
                    after_options_grade3 = c['after_potential_options'][2]['grade']
                )
            elif len(c['before_potential_options'])==2:
                Cube.objects.create(
                    key = key,
                    character_name = c['character_name'],
                    create_date = c['create_date'],
                    cube_type = c['cube_type'],
                    item_upgrade_result = c['item_upgrade_result'],
                    item_level = c['item_level'],
                    target_item = c['target_item'],
                    potential_option_grade = c['potential_option_grade'],
                    before_options_value1 = c['before_potential_options'][0]['value'],
                    before_options_grade1 = c['before_potential_options'][0]['grade'],
                    before_options_value2 = c['before_potential_options'][1]['value'],
                    before_options_grade2 = c['before_potential_options'][1]['grade'],
                    after_options_value1 = c['after_potential_options'][0]['value'],
                    after_options_grade1 = c['after_potential_options'][0]['grade'],
                    after_options_value2 = c['after_potential_options'][1]['value'],
                    after_options_grade2 = c['after_potential_options'][1]['grade']
                )
            elif len(c['before_additional_potential_options'])==3:
                Cube.objects.create(
                    key = key,
                    character_name = c['character_name'],
                    create_date = c['create_date'],
                    cube_type = c['cube_type'],
                    item_upgrade_result = c['item_upgrade_result'],
                    item_level = c['item_level'],
                    target_item = c['target_item'],
                    potential_option_grade = c['additional_potential_option_grade'],
                    before_options_value1 = c['before_additional_potential_options'][0]['value'],
                    before_options_grade1 = c['before_additional_potential_options'][0]['grade'],
                    before_options_value2 = c['before_additional_potential_options'][1]['value'],
                    before_options_grade2 = c['before_additional_potential_options'][1]['grade'],
                    before_options_value3 = c['before_additional_potential_options'][2]['value'],
                    before_options_grade3 = c['before_additional_potential_options'][2]['grade'],
                    after_options_value1 = c['after_additional_potential_options'][0]['value'],
                    after_options_grade1 = c['after_additional_potential_options'][0]['grade'],
                    after_options_value2 = c['after_additional_potential_options'][1]['value'],
                    after_options_grade2 = c['after_additional_potential_options'][1]['grade'],
                    after_options_value3 = c['after_additional_potential_options'][2]['value'],
                    after_options_grade3 = c['after_additional_potential_options'][2]['grade']
                )
            elif len(c['before_additional_potential_options'])==2:
                Cube.objects.create(
                    key = key,
                    character_name = c['character_name'],
                    create_date = c['create_date'],
                    cube_type = c['cube_type'],
                    item_upgrade_result = c['item_upgrade_result'],
                    item_level = c['item_level'],
                    target_item = c['target_item'],
                    potential_option_grade = c['additional_potential_option_grade'],
                    before_options_value1 = c['before_additional_potential_options'][0]['value'],
                    before_options_grade1 = c['before_additional_potential_options'][0]['grade'],
                    before_options_value2 = c['before_additional_potential_options'][1]['value'],
                    before_options_grade2 = c['before_additional_potential_options'][1]['grade'],
                    after_options_value1 = c['after_additional_potential_options'][0]['value'],
                    after_options_grade1 = c['after_additional_potential_options'][0]['grade'],
                    after_options_value2 = c['after_additional_potential_options'][1]['value'],
                    after_options_grade2 = c['after_additional_potential_options'][1]['grade']
                )

def cubeinfo(request):
    if request.method == "POST":
        userkey = request.POST['Key']
        comment = ''
        if 'update' in request.POST:
            lasthistory = Cube.objects.filter(key=userkey).order_by('-create_date')[0]
            lastdate = datetime.now().date()-timedelta(days=1)
            if lasthistory:
                startdate = lasthistory.create_date.date()+timedelta(days=1)
                if startdate<=lastdate:
                    cube = maple_API(userkey,startdate.strftime('%Y-%m-%d'),lastdate.strftime('%Y-%m-%d'))
                    cubesave(cube,userkey)
            else:
                cube = maple_API(userkey,'2022-11-25',lastdate.strftime('%Y-%m-%d'))
                cubesave(cube,userkey)
        elif 'filtering' in request.POST:
            charactor_check_list = request.POST.getlist('charactor_filter',None)
            cube_check_list = request.POST.getlist('cube_filter',None)
            qcharacter=Q()
            qcube=Q()
            for c in charactor_check_list:
                qcharacter |= Q(character_name = c)
            for c in cube_check_list:
                qcube |= Q(cube_type = c)
            cubehistory = Cube.objects.filter(qcharacter & qcube).all().order_by('-create_date')
            if not cubehistory:
                cubehistory = Cube.objects.filter(key=userkey).order_by('-create_date')
                comment = '체크한 조건으로 조회된 내용이 없습니다.'
        else:
            cubehistory = Cube.objects.filter(key=userkey).order_by('-create_date')
            
        if cubehistory:
            lastcube = cubehistory[0]
            cubehistory2 = Cube.objects.filter(key=userkey).order_by('create_date')[0]
            userkey = lastcube.key
            userchracter = lastcube.character_name
            startdate = cubehistory2.create_date
            lastdate = lastcube.create_date
            
            charactorlist =  Cube.objects.filter(key=userkey).distinct().values_list('character_name',flat=True)
            cubelist =  Cube.objects.filter(key=userkey).distinct().values_list('cube_type',flat=True)
            cc = cubehistory.filter(cube_type='수상한 큐브').all().count()
            jc = cubehistory.filter(cube_type='장인의 큐브').all().count()
            mc = cubehistory.filter(cube_type='명장의 큐브').all().count()
            rc = cubehistory.filter(cube_type='레드 큐브').all().count()
            bc = cubehistory.filter(cube_type='블랙 큐브').all().count()
            emc = cubehistory.filter(cube_type='이벤트 링 전용 명장의 큐브').all().count()
            cac = cubehistory.filter(cube_type='수상한 에디셔널 큐브').all().count()
            ac = cubehistory.filter(cube_type='에디셔널 큐브').all().count()
            wac = cubehistory.filter(cube_type='화이트 에디셔널 큐브').all().count()
            context = {
                'userkey':userkey,
                'character_name': userchracter,
                'character_list': charactorlist,
                'cube_list': cubelist,
                'cubehistory':cubehistory,
                'startdate': startdate,
                'lastdate': lastdate,
                'cc':cc,
                'jc':jc,
                'mc':mc,
                'rc':rc,
                'bc':bc,
                'emc':emc,
                'cac':cac,
                'ac':ac,
                'wac':wac,
                'comment':comment
            }
        else:
            lastdate = datetime.now().date()-timedelta(days=1)
            cube = maple_API(userkey,'2022-11-25',lastdate.strftime('%Y-%m-%d'))
            cubesave(cube,userkey)
            cubehistory = Cube.objects.filter(key=userkey).order_by('-create_date')
            lastcube = cubehistory[0]
            cubehistory2 = Cube.objects.filter(key=userkey).order_by('create_date')[0]
            userkey = lastcube.key
            userchracter = lastcube.character_name
            startdate = cubehistory2.create_date
            lastdate = lastcube.create_date

            charactorlist =  Cube.objects.filter(key=userkey).distinct().values_list('character_name',flat=True)
            cubelist =  Cube.objects.filter(key=userkey).distinct().values_list('cube_type',flat=True)
            cc = cubehistory.filter(cube_type='수상한 큐브').all().count()
            jc = cubehistory.filter(cube_type='장인의 큐브').all().count()
            mc = cubehistory.filter(cube_type='명장의 큐브').all().count()
            rc = cubehistory.filter(cube_type='레드 큐브').all().count()
            bc = cubehistory.filter(cube_type='블랙 큐브').all().count()
            emc = cubehistory.filter(cube_type='이벤트 링 전용 명장의 큐브').all().count()
            cac = cubehistory.filter(cube_type='수상한 에디셔널 큐브').all().count()
            ac = cubehistory.filter(cube_type='에디셔널 큐브').all().count()
            wac = cubehistory.filter(cube_type='화이트 에디셔널 큐브').all().count()
            context = {
                'userkey':userkey,
                'character_name': userchracter,
                'character_list': charactorlist,
                'cube_list': cubelist,
                'cubehistory':cubehistory,
                'startdate': startdate,
                'lastdate': lastdate,
                'cc':cc,
                'jc':jc,
                'mc':mc,
                'rc':rc,
                'bc':bc,
                'emc':emc,
                'cac':cac,
                'ac':ac,
                'wac':wac,
                'comment':comment
            }
    else:
        context = {}
    return render(request,'apitest/cubeinfo.html',context)