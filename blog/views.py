from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return HttpResponse("<html><title>Сайт Асана Жумабаева</title><h1>Асан Жумабаев</h1></html>")

