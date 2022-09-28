# TODO: Implement Routings Here
from django.urls import path
from todolist.views import delete_task, show_todolist
from todolist.views import register, login_user, logout_user, create_task, delete_task, done_task, undone_task #sesuaikan dengan nama fungsi yang dibuat


app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'), #sesuaikan dengan nama fungsi yang dibuat
    path('login/', login_user, name='login'), #sesuaikan dengan nama fungsi yang dibuat
    path('logout/', logout_user, name='logout'), #sesuaikan dengan nama fungsi yang dibuat
    path('create-task/', create_task, name="create_task"),
    path('delete_task/<int:id>', delete_task, name="delete_task"),
    path('done_task/<int:id>', done_task, name="done_task"),
    path('undone_task/<int:id>', undone_task, name="undone_task"),
]