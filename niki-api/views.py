from django.http import HttpResponse
import json
from nikiconverter import NikiConverter

nc = NikiConverter()

def apicall(request):
    resource = request.GET['resource']
    result = nc.apiRequest(resource)
    return HttpResponse(json.dumps(result), content_type='application/json')