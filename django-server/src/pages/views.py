from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'home.html', {})

def models_view(request):
    return render(request, 'models.html', {})

def about_view(request):
    return render(request, 'about.html', {})

def social_view(request):
    return render(request, 'social.html', {})
    