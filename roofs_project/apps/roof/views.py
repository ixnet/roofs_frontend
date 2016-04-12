from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404

from roof.models import Roof 

def l404(request):
    return render(request, 
                  "404.html")

def index(request):
    return render(request, 
                  "roof/index.html")

def list(request):
    queryset = Roof.objects.all()
    return render(request,
                  "roof/list.html",
                  {'list': queryset,
                   'title': 'Крыши'}
                  )


def detail(request, id=None):
    instance = get_object_or_404(Roof, id=id)
    return render(request,
                  "roof/detail.html",
                  {'instance': instance,
                   'title': instance.title}
                  )
