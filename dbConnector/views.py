from django.shortcuts import render
import json
from django.core import serializers

from rest_framework.views import APIView
from rest_framework.response import Response
from dbConnector.models import *
from dbConnector.service import Services


class FetchRecords(APIView):

    def get(self, request, *args, **kwargs):
        print("args - ",args)
        print("kwargs - ",kwargs)
        records = []
        c_type = kwargs['classType']
        class_type = Services.get_class(c_type)
        records = class_type.objects.all()
        records_json = json.loads(serializers.serialize('json', records))
        print("records json -",records_json)
        records_list = []
        i = 0
        for r in records_json:
            # if type(r['fields']) == type(class_type):
            #     records_list.append(json.loads(serializers.serialize('json',r['fields'])))
            records_list.append(r['fields'])
            records_list[i]['id'] = r['pk']
            i += 1
            # print(r['fields'].id)

        
        return Response(records_list)


class UpdateRecord(APIView):

    def post(self, request):
        
        c_type = request.data.get("classType")
        new_record = request.data.get("newRecord")
        id = request.data.get("id")

        class_type = Services.get_class(c_type)
        record = class_type.objects.get(id=id)

        for f in new_record:
            if f == "skill":
                skill = Skill.objects.get(id=record['skill'])
                setattr(skill, 'title', new_record['skill']['title'])
                setattr(skill, 'description', new_record['skill']['description'])
                setattr(record, f, skill)

            else:
                setattr(record, f, new_record[f])

        record.save()
        
        return Response("Update successful")

class DeleteRecord(APIView):

    def post(self, request):
        c_type = request.data.get("classType")
        id = request.data.get("id")
        class_type = Services.get_class(c_type)
        class_type.objects.filter(id=id).delete()
        return Response("Delete successful")


class AddRecord(APIView):

    def post(self, request):
        
        c_type = request.data.get("classType")
        new_record = request.data.get("newRecord")

        class_type = Services.get_class(c_type)
        record = class_type.objects.create()

        for f in new_record:
            print(f)
            

            if f == "skill":
                setattr(record, f, Skill.objects.create(title=new_record['skill']['title'], description = new_record['skill']['description']))

            else:
                setattr(record, f, new_record[f])

        record.save()
        
        return Response("Record successfully added")

class FetchSingleRecord(APIView):

    def get(self, request, *args, **kwargs):
        print("args - ",args)
        print("kwargs - ",kwargs)
        c_type = kwargs['classType']
        id = kwargs['id']
        class_type = Services.get_class(c_type)
        record = class_type.objects.get(id=id)


        record_json = json.loads(serializers.serialize('json', [record]))

        record_ret = record_json[0]['fields']
        record_ret['id'] = record_json[0]['pk']

        return Response(record_ret)

        