from django.core import serializers
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Process, Users
import subprocess, os, json


# This execute the bash script to fetch and save the 'ps' output into the database.
# If saved successfully, it will return a JSON response saying it was cached successfully.
# The settings from django.conf were imported, to use the BASE_DIR in order to join the script
# location, to ensure portability to any system. 
def cachePs(request):
    subprocess.run(os.path.join(settings.BASE_DIR, "psscript.sh"))
    msg = {
        "body": "PS output cached successfully"
    }
    return JsonResponse(msg)

# Here the saved data is serialized, in order to display it as JSON to the front end. 
# This will make the data readable for the front end, so it can be displayed in the browser.
def getPs(request):
    ps = serializers.serialize("json", Process.objects.all())
    output = [d['fields'] for d in json.loads(ps)]
    return JsonResponse(output, safe=False)

def getById(request, uid):
    psByUid = serializers.serialize("json", Process.objects.filter(uid=uid))
    output = [d['fields'] for d in json.loads(psByUid)]
    return JsonResponse(output, safe=False)

def getUsers(request):
    subquery = Process.objects.values_list("uid", flat=True).distinct()
    users = serializers.serialize("json", Users.objects.filter(uid__in=subquery))
    output = [d['fields'] for d in json.loads(users)]
    return JsonResponse(output, safe=False)