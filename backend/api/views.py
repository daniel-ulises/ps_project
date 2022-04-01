from django.core import serializers
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Process
import subprocess, os

# This execute the bash script to fetch and save the 'ps' output into the database.
# If saved successfully, it will return a JSON response saying it was cached successfully.
# The 'os' module was used to get the relative path, in order to make it work on any computer.
def cachePs(request):
    subprocess.run(os.path.abspath('psscript.sh'))
    msg = {
        "body": "PS output cached successfully"
    }
    return JsonResponse(msg)

# Here the saved data is serialized, in order to display it as JSON to the front end. 
# This will make the data readable for the front end, so it can be displayed in the browser.
def getPs(request):
    ps = serializers.serialize("json", Process.objects.all())
    return HttpResponse(ps, content_type='application/json')
