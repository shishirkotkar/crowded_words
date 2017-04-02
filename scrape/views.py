from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from scrape.data_processor import DataProcessor, DataAdapter


def cloud(request):
    return render_to_response('index.html')


@csrf_exempt
def analyze(request):
    data_processor = DataProcessor(input_data=dict(request.POST)['data'])
    data_adapter = DataAdapter(data_processor=data_processor)
    return HttpResponse(data_adapter.get_json())
