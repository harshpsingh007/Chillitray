from django.contrib.auth import authenticate, login
from django.core import paginator
from django.shortcuts import render
from .forms import UserRegistrationForm
from .models import Task
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.
def Home(request):
    task = Task.objects.all()
    paginator = Paginator(task,5)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    params = {'page_obj': page_obj}
    return render(request,"mainapp/home.html",params)

def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        # print(f"user Form : ==== : {user_form.cleaned_data['username']}")
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data["password"])
            new_user.save()
            return render(request, 'mainapp/register_done.html')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'mainapp/register.html', {'user_form': user_form})