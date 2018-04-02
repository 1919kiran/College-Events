from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as login_function
# Create your views here.
def test(request):
    return render(request, 'index.html')

def login(request):

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login_function(request,user)
            return redirect('events')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html',{'form':form})

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login_function(request, user)
            return redirect('events')
        else:
            return redirect('events')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html',{'form':form})
