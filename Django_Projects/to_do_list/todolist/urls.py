from django.urls import path
from . import views

app_name = 'todolist'
urlpatterns = [

    path('', views.home, name='主页'),
    path('/todolist/about', views.aboutPage, name='关于本站'),  # name=网址名字
    path('/todolist/edit', views.edit, name='edit')
]