from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login

# Create your views here.
def signup_view(request):
  if request.method == 'POST':
    signupForm = UserCreationForm(request.POST)
    if signupForm.is_valid():
      user = signupForm.save()
      # log in the user
      login(request, user)
      return redirect('articles:list')
  else:
    signupForm = UserCreationForm()
  return render(request, 'accounts/signup.html', { 'form': signupForm })

def login_view(request):
  if request.method == 'POST':
    loginForm = AuthenticationForm(data=request.POST)
    if loginForm.is_valid():
      # log in the user
      user = loginForm.get_user()
      login(request, user)
      return redirect('articles:list')
  else:
    loginForm = AuthenticationForm()
  return render(request, 'accounts/login.html', { 'form': loginForm })
