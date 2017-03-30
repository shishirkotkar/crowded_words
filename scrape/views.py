from django.shortcuts import render_to_response


def cloud(request):
    return render_to_response('index.html')
