from django.shortcuts import render
from django.http import HttpResponse

# --- ESTA É A FUNÇÃO QUE ESTAVA FALTANDO ---
def home(request):
    return HttpResponse("<h1>Página Inicial</h1>")

def login(request):
    return HttpResponse("<h1>Página de Login</h1>")

def cadastro(request):
    return HttpResponse("<h1>Página de Cadastro</h1>")
