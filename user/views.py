from django.contrib.auth import forms
from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegisterForm
from django.contrib import messages

class Register(View):
    def get(self, request):
        form = UserRegisterForm()
        context = {'form': form}
        return render(request, 'user/register.html', context = context)
    
    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            userName = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {userName}. You are now able to log in')
            return redirect('login')
        return render(request, 'user/register.html', {'form': form})
        
