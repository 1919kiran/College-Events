from django.shortcuts import render

# Create your views here.
def test(request):
    return render(request, 'accounts/index.html')

def signup(request):
    return render(request, 'accounts/index.html')
