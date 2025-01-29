from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Count    


from .models import Task, User, Client
from .forms import TaskForm, ClientForm, CustomerForm, WorkTypeForm

PAGINATION = 10

class TaskCreateView(CreateView):
    form_class = TaskForm
    template_name = 'task/new_task.html'
    success_url = reverse_lazy('task:index')


@login_required
def task_create(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        task = form.save(commit=False)
        task.author = request.user
        task.save()
        return redirect("task:index")
        # return redirect("task:profile", request.user.username)
    form = TaskForm()
    context = {"form": form}
    return render(request, "task/new_task.html", context)


@login_required
def client_create(request):
    form = ClientForm(request.POST or None)
    if form.is_valid():
        client = form.save(commit=False)
        client.save()
        return redirect("task:new_task")
    form = ClientForm()
    context = {"form": form}
    return render(request, "task/new_client.html", context)


@login_required
def customer_create(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        customer = form.save(commit=False)
        customer.save()
        return redirect("task:new_task")
    form = CustomerForm()
    context = {"form": form}
    return render(request, "task/new_customer.html", context)


@login_required
def work_type_create(request):
    form = WorkTypeForm(request.POST or None)
    if form.is_valid():
        customer = form.save(commit=False)
        customer.save()
        return redirect("task:new_task")
    form = WorkTypeForm()
    context = {"form": form}
    return render(request, "task/new_work_type.html", context)


def index(request):
    print(type(request.user))
    if request.user.is_superuser:
        task_list = Task.objects.all().order_by('-adding_date')
    else:
        task_list = Task.objects.all().filter(executor = request.user).order_by('-adding_date')
    paginator = Paginator(task_list, PAGINATION) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'task/index.html', context)  


def task_list(request):
    return HttpResponse('Tasl List')


def task_detail(request, pk):
    task = Task.objects.get(id=pk)
    context = {
        'task': task,
    }
    return render(request, 'task/task_detail.html', context)


def user_profile(request, user_id):
    user = User.objects.get(id=user_id)
    user_tasks = Task.objects.all().filter(executor = user_id)
    paginator = Paginator(user_tasks, PAGINATION) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'user': user,
    }
    return render(request, 'task/user_profile.html', context)  


def client_profile(request, client_id):
    client = Client.objects.get(id=client_id)
    client_tasks = Task.objects.all().filter(client = client_id)
    paginator = Paginator(client_tasks, PAGINATION) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'client': client,
    }
    return render(request, 'task/client_profile.html', context)  
