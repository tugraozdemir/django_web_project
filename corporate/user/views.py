from django.shortcuts import redirect, render
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import login
# Create your views here.

def register(request):
    form = RegisterForm(request.POST or None)
    
    if form.is_valid():
        first_name = form.cleaned_data.get("first_name")
        last_name = form.cleaned_data.get("last_name")
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")
        
        
        # Kullanıcı adı kontrolü
        if User.objects.filter(username=username).exists():
            form.add_error("username", "Bu kullanıcı adı zaten alınmış.")
        else:
            # Kullanıcı adı mevcut değilse yeni kullanıcı oluştur
            newUser = User(first_name = first_name, last_name = last_name,username=username,email = email,)
            newUser.set_password(password)
            

            newUser.save()

            login(request, newUser)
            return redirect("index")
    
    context = {
        "form": form
    }
    
    return render(request, "register.html", context)

    
def loginUser(request):
    return render(request, "login.html")
def logoutUser(request):
    return render(request, "logout.html")