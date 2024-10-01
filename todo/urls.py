from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add/", views.add, name="add"),
    path("view/", views.view, name="view"),
    path("delete/<str:pk>", views.delete, name="delete"),
    path("update/<str:pk>", views.update, name="update"),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
   
]
