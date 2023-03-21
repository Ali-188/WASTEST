from django.shortcuts import render
from django.http import HttpResponse

from newsapp.models import News
# Create your views here.

def index(request):
    context_dict = {}
    context_dict['newslist'] = News.objects.order_by('-date')
    return render(request, 'newsapptemplates/index.html', context=context_dict)


