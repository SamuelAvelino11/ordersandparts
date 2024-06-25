from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def view_login(request):
    return render(request, 'Login.html')

def submitLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request,'usuario ou senha invalida!')
    return redirect('/')
def logout_user(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/login/')
def menu(request):
    return render(request, 'Menu.html')

@login_required(login_url='/login/')
def pedidos(request):
    return render(request, "Pedidos.html")

@login_required(login_url='/login/')
def produtos(request):
    return render(request, "Produtos.html")
