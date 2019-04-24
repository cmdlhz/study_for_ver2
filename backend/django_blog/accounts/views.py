from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.
def signup_view(request):
  if request.method == 'POST':
    userForm = UserCreationForm(request.POST)
    if userForm.is_valid():
      userForm.save()
      # log the user in
      return redirect('articles:list')
  else:
    userForm = UserCreationForm()
  return render(request, 'accounts/signup.html', { 'form': userForm })

def login_view(request):
  if request.method == 'POST':
    authForm = AuthenticationForm(data=request.POST)
    if authForm.is_valid():
      # log in the user
      return redirect('articles:list')
  else:
    authForm = AuthenticationForm()
  return render(request, 'accounts/login.html', { 'form': authForm })
