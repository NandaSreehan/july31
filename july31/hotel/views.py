from django.shortcuts import render
from hotel.models import menu


def home(request):
    res=menu.objects.all()
    if request.method=="POST":
        s=int(request.POST.get('dishname'))
        if menu.objects.filter(price=s).exists():
            n=menu.objects.filter(price=s)
        else:
            n=None
        return render(request,'index.html',{"j":res,"s":n})
    return render(request,'index.html',{"j":res})