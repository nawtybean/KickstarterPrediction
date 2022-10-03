from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth import logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

User = get_user_model()

def home(request):
    try:
        messages.success(request, "Login Successful")
        url = '../kickstarter/landing'
        return redirect(url)
    except:
        logout(request)
        messages.error(request, "An error occurred")
        url = '/'
        return redirect(url)