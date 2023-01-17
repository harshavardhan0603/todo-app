from tasks import views
from django.urls import path

urlpatterns  = [

path('', views.index, name='home'),
path("update/<str:n>", views.update, name = "update"),
path("delete/<str:n>", views.deleteTask, name = "delete"),

path("login/", views.log_in, name = "login"),
path("logout", views.log_out, name = "logout"),

path("register/", views.registerpage, name='register')

]