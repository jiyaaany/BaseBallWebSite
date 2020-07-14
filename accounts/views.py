from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
                username = request.POST["username"], password = request.POST["password1"])
            auth.login(request,user)
            return redirect('index')
        return render(request, 'signup.html')
    return render(request, 'signup.html')

def login(request):
    # COOKIES에 값이 없다면
    if request.COOKIES.get('username') is not None:
        username = request.COOKIES.get('username')
        password = request.COOKIES.get('password')
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("cafe:index")
        else:
            return render(request, 'accounts.login.html')
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            if request.POST.get("keep_login")=="TRUE":
                response = render(request, 'accounts/home.html')
                response.set_cookie('username', username)
                response.set_cookie('password', password)
                return response
            return redirect('index')
        else:
            return render(request, 'login.html', {'error' : 'username or password is incorrect'})
    else:
        return render(request, 'login.html')
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def mypage(request):
    return render(request, 'mypage.html')