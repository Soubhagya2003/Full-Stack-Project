from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse("this about")

def contact(request):
    return HttpResponse("Wanna contact me")

def service(request):
    return HttpResponse("there is no service")

