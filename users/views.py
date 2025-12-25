import uuid
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Profile
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt

@csrf_exempt
def signup_view(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phoneno = request.POST.get('phoneno')
        gender = request.POST.get('gender')

        if User.objects.filter(username=username).exists():
            messages.warning(request, 'Account Already Exists')
            return redirect('signup')

        user_obj = User.objects.create_user(username=username, email=email, password=password)

        profile = Profile.objects.create(
            user=user_obj,
            fullname=fullname,
            phoneno=phoneno,
            gender=gender,
            username=username,
            email=email,
            password=password,

        )

        messages.success(request, 'Account Created. Please log in.')
        return redirect('login')

    return render(request, 'signup.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username)

        if not user.exists():
            messages.warning(request, 'Account Not Found')
            return HttpResponseRedirect(request.path_info)
        user = authenticate(username=username, password=password)
        if user:
            login(request,user)
            messages.success(request, 'Login Successful')
            return redirect("home")
        messages.warning(request, 'Invalid Credentials')
        return HttpResponseRedirect(request.path_info)
    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')