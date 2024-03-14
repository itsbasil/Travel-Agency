from django.shortcuts import render

# Create your views here.

def main(request):
    return render (request, 'main.html')
def package(request):
    return render (request, 'package.html')
def destination(request):
    return render (request, 'destination.html')
def contact(request):
    return render (request, 'contact.html')
def about(request):
    return render (request, 'about.html')