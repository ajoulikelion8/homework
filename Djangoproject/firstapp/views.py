from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

    #url 과 html 연결