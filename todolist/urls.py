# TODO: Implement Routings Here
from django.urls import path
from todolist.views import show_todolist
from todolist.views import register, login_user, logout_user, create_task #sesuaikan dengan nama fungsi yang dibuat




app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'), #sesuaikan dengan nama fungsi yang dibuat
    path('login/', login_user, name='login'), #sesuaikan dengan nama fungsi yang dibuat
    path('logout/', logout_user, name='logout'), #sesuaikan dengan nama fungsi yang dibuat
    path('create-task/', create_task, name="create_task"),
]