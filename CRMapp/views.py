from django.shortcuts import render,redirect

def home(request):
    return render(request,'landing_page.html')
def dashboard(request):
    return render(request, 'dashboard.html')
