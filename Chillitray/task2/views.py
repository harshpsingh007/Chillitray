from django.core import paginator
from django.shortcuts import render
from .models import Task2Model
from django.shortcuts import get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
def Task2(request):
    obj = Task2Model.objects.all()
    paginator = Paginator(obj,5)
    page_number = request.GET.get("page")
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return render(request,"task2/task2home.html",{'page_obj':page_obj})