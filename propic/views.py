from django.shortcuts import render,redirect
from .models import AccountImages

# Create your views here.

def get_image(request):
    user = request.user
    if request.method == "POST":
        image = request.FILES.get("image")
        obj = AccountImages.objects.create(iuser=user,iimage = image)
        return redirect("/get-image")

    return render(request,"add_image.html")

def getallpics(request):
    obj = AccountImages.objects.all()
    
    return render(request,"allpics.html",context={"data":obj})
