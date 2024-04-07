from django.shortcuts import render, redirect
from userauths import forms
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.conf import settings
from .models import User

# Create your views here.
def register_view(request):
    form = forms.UserRegisterForm()
    if request.method == 'POST':
        form = forms.UserRegisterForm(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Hey {username}, Your account was created successfully!")
            new_user = authenticate(request, username=form.cleaned_data['email'], password=form.cleaned_data['password1'])
            login(request, new_user)
            return redirect("baseapp:index")
    context = {
        'form': form,
    }
    return render(request, "userauths/sign-up.html", context)

def login_view(request):     
    context = {}
    if request.user.is_authenticated:
        messages.warning(request, f"Hey, you are already logged in!")
        return redirect('baseapp:index')
    if request.method == 'POST':
        givenemail = request.POST.get("email")
        givenpassword = request.POST.get("password")
        try:
            user = User.objects.get(email=givenemail, password=givenpassword)
            user = authenticate(request, email=givenemail, password=givenpassword)
            if user is not None:
                login(request, user)
                messages.success(request, f"You have logged in")
                return redirect('baseapp:index')
            else:
                messages.warning(request, "User doesn't exist. Please create an account first")
        except:
            messages.warning(request, f"User with {givenemail} does not exist")
    return render(request, "userauths/sign-in.html", context)

def logout_view(request):
    logout(request)
    messages.success(request, "User has been logged out.")
    return redirect("userauths:sign-in")


