from datetime import datetime
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.core import serializers

from todolist.models import Task

# Create your views here.

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_todolist = Task.objects.filter(user=request.user)
    context = {
        'nama': request.user.username,
        'list_todolist': data_todolist,
        # 'last_login': request.COOKIES['last_login'],
    }
    return render(request, "todolist-ajax.html", context)

@login_required(login_url='/todolist/login/')
def show_todolist_json(request):
    if request.method == "GET":
        data = Task.objects.filter(user=request.user)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def add_task_ajax(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest' and request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        date = datetime.now()
        new_task = Task.objects.create(user=request.user, date=date, title=title, description=description)
        
        serialize_json = serializers.serialize('json', [new_task])
        print(serialize_json)
        
        return HttpResponse(serialize_json)

    return JsonResponse({"error": "Not an ajax request"}, status=400)

def delete_task_ajax(request, id):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest' and request.method == "DELETE":
        task = Task.objects.get(pk=id)
        task.delete()
        return HttpResponse("Success Deleting Task")
    return JsonResponse({"error": "Not an ajax request"}, status=400)

def done_task_ajax(request, id):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest' and request.method == "POST":
        task = Task.objects.get(pk=id)
        task.is_finished = True
        task.save()
        return HttpResponse("Success updating status task")
    return JsonResponse({"error": "Not an ajax request"}, status=400)

def undone_task_ajax(request, id):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest' and request.method == "POST":
        task = Task.objects.get(pk=id)
        task.is_finished = False
        task.save()
        return HttpResponse("Success updating status task")
    return JsonResponse({"error": "Not an ajax request"}, status=400)



def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)                                                # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist"))  # membuat response
            response.set_cookie('last_login', str(datetime.now()))     # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}

    return render(request, 'login.html', context)

@login_required(login_url='/todolist/login/')
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login/')
def create_task(request):
    if (request.method == "POST"): # Jika request user tambah task
        title = request.POST["title"]
        date = datetime.now()
        description = request.POST["description"]
        
        new_task = Task.objects.create(user=request.user, date=date, title=title, description=description)
        return redirect('todolist:show_todolist')

    return render(request, "create-task.html")

@login_required(login_url='/todolist/login/')
def delete_task(request, id):
    task_to_delete = Task.objects.get(pk=id) # Mengambil index task yang ingin dihapus
    task_to_delete.delete()
    return redirect('todolist:show_todolist')

@login_required(login_url='/todolist/login/')
def done_task(request, id):
    task_to_update = Task.objects.get(pk=id)    # Mengambil index task yang ingin dihapus
    task_to_update.is_finished = True           # set menjadi true
    task_to_update.save()
    return redirect('todolist:show_todolist')

@login_required(login_url='/todolist/login/')
def undone_task(request, id):
    task_to_update = Task.objects.get(pk=id)    # Mengambil index task yang ingin dihapus
    task_to_update.is_finished = False          # set menjadi false
    task_to_update.save()
    return redirect('todolist:show_todolist')