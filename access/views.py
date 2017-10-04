from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
# from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.contrib import auth
from .models import Profile


def index(request):
    # email = EmailMessage('title', 'body', to=['dk291996@gmail.com'])
    # abc = email.send()
    # print (abc)
    return render(request, 'index.html')


def auth_check(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username , password=password)

    if user is not None:
        auth.login(request , user)
        return redirect('home')
    else:
        return HttpResponseRedirect('/invalid/')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST , request.FILES)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load profile instance created by signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.profile.gender = form.cleaned_data.get('gender')
            user.profile.first_name = form.cleaned_data.get('firts_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.address = form.cleaned_data.get('address')
            user.profile.referal_id = form.cleaned_data.get('referal_id')
            user.profile.pan_number = form.cleaned_data.get('pan_number')
            user.profile.city = form.cleaned_data.get('city')
            user.profile.mobile_number = form.cleaned_data.get('mobile_number')
            user.profile.pincode = form.cleaned_data.get('pincode')
            user.profile.email_id = form.cleaned_data.get('email_id')
            user.profile.state = form.cleaned_data.get('state')
            user.profile.profile_pic = form.cleaned_data.get('profile_pic')
            user.save()
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form':form})


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


def invalid(request):
    return render(request, 'invalid.html')


def log_in(request):
    return render(request, 'login.html')


def home(request):
    if request.user.is_authenticated():
        return render(request, 'home.html')
    else:
        return render(request, 'invalid.html')
