from datetime import datetime
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

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
    return render(request, "todolist.html", context)


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