from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.views.generic import View
from .models import Event
from .forms import UserForm

class UserFormView(View):
    form_class = UserForm
    template_name = 'home/register.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home:index')
        return render(request, self.template_name, {'form':form})

def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                event = Event.objects.filter(user=request.user)
                return render(request, 'home/index.html', {'event': event})
    context = {
        "form": form,
    }
    return render(request, 'home/register.html', context)

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                event = Event.objects.get(pk = request.user.pk)
                return render(request, 'home/index.html', {'event': event})
            else:
                return render(request, 'home/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'home/login.html', {'error_message': 'Invalid login'})
    return render(request, 'home/login.html')

def index(request):
    event_list = Event.objects.all()
    return render(request, 'home/index.html', {'event_list': event_list})

def about(request):
    return render(request, 'home/about.html')

def detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'home/detail.html', {'event': event})

def forum(request):
    return render(request, 'home/forum.html')
