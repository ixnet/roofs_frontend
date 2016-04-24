from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from roof.models import Roof


def index(request):
    return render(request,
                  "roof/index.html")

def banner(request):
    return render(request,
                  "roof/banner.html")

def list(request):
    queryset_list = Roof.objects.all()
    # FIXME: 10 roofs per page
    paginator = Paginator(queryset_list, 2)
    page = request.GET.get('page')

    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    return render(request,
                  "roof/list.html",
                  {'list': queryset,
                   'title': 'Список крыш'}
                  )


def detail(request, slug=None):
    roof = get_object_or_404(Roof, slug=slug)
    return render(request,
                  "roof/detail.html",
                  {'roof': roof}
                  )
