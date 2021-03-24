from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.http import JsonResponse


# Create your views here.
def save_data(request):
    if request.method == 'POST':
        nm=request.POST["name"]
        em=request.POST["email"]
        pw=request.POST["password"]
        user=User.objects.create_user(username=nm, password=pw, email=em)
        user.save()
        return JsonResponse({'status':'save'})
    else:
        return render(request,'register.html')
