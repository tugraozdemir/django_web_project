from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    """context = {
        "numbers":[1,2,3,4,5,6,7]
    }"""
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def detail(request,id):
    return HttpResponse("Detail: "+ str(id))

def contact(request):
    return render(request, "contact.html")
    