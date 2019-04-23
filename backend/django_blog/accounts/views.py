from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

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