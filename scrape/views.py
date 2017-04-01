import json
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from scrape.data_processor import DataProcessor

def cloud(request):
    return render_to_response('index.html')


@csrf_exempt
def analyze(request):
    dp = DataProcessor(input_data=dict(request.POST)['data'])
    filtered_wrods =  dp.run()
    return HttpResponse(json.dumps({'x': 1}))

