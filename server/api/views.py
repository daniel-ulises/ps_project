from django.core.serializers import serialize
from django.conf import settings
from django.http import JsonResponse
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
    return JsonResponse(msg, safe=False)

# Here the saved data is serialized, in order to display it as JSON to the front end. 
# This will make the data readable for the front end, so it can be displayed in the browser.
def getPs(request):
    ps = json.loads(serialize("json", Process.objects.all()))
    return JsonResponse(ps, safe=False)

# This will get the running processes for a specific user that will be selected
# on the front end. 
def getById(request, uid):
    psByUid = json.loads(serialize("json", Process.objects.filter(uid=uid)))
    return JsonResponse(psByUid, safe=False)

# This query will return a list of users to display them in the 'select' element
# on the front end. In order to avoid displaying users from the system that
# are not running a process, the query filters the users to show only
# the ones that also have a running process attatched to them.
def getUsers(request):
    subquery = Process.objects.values_list("uid", flat=True).distinct()
    users = json.loads(serialize("json", Users.objects.filter(uid__in=subquery)))
    return JsonResponse(users, safe=False)