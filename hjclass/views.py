from django.shortcuts import render
from django.template.response import TemplateResponse
from django.http.response import HttpResponse
from .models import HJClass

# Create your views here.
def getclass(request, class_name):
    try:
        short_url = HJClass.objects.get(class_name=class_name).short_url
    except Exception:
        return HttpResponse("课程不存在")

    context = dict(
        class_name=class_name,
        short_url=short_url
    )
    return TemplateResponse(request, 'class.html', context)