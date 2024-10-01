from django.shortcuts import render,redirect
from .forms import ItemForm,UserForm,LoginForm
from .models import Item
from django.contrib.auth.models import User
from django.contrib.auth.models import auth 
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# Create your views here.
def home (request):
    return render(request, "home.html")

def register(request):
    form = UserForm()
    context = {"form": form}
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    return render(request, "register.html", context=context)
def login(request):
    form = LoginForm()
    context = {"form": form}
    if request.method == "POST":
        form = LoginForm(request,data = request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request,username=username, password=password)
            if user is not None:
                auth.login(request,user)
                return redirect("dashboard")
    return render(request, "login.html", context=context)

def logout(request):
    auth.logout(request)
    return redirect("home")
@login_required(login_url="login")
def dashboard(request):
    return render(request, "dashboard.html")

def add(request):
    form = ItemForm()
    context = {"form": form}
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    return render(request, "add.html",context= context)

def view(request):
    items = Item.objects.all()
    context = {"items": items}
    return render(request, "view.html", context=context)

def delete(request,pk):
    item = Item.objects.get(id=pk)
    context = {"item": item}
    if request.method == "POST":
        item.delete()
        return redirect("view")
    return render(request, "delete.html", context=context)

def update(request,pk):
    item = Item.objects.get(id=pk)
    form = ItemForm(instance=item)
    context = {"form": form}
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("view")
    return render(request, "update.html", context=context)




