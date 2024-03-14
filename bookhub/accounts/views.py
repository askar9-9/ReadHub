from django.shortcuts import render, redirect

# Create your views here.
def login(request):
    return redirect('catalog')

def logout(request):
    return redirect('catalog')

def register(request):
    return redirect('index')