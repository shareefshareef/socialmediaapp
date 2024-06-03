from django.shortcuts import render,redirect
from .models import AccountImages

# Create your views here.

def get_image(request):
    user = request.user
    if request.method == "POST":
        description = request.POST.get("description")
        image = request.FILES.get("image")
        obj = AccountImages.objects.create(iuser=user,iimage = image,description=description)
        return redirect("/get-image")

    return render(request,"add_image.html")

def getallpics(request):
    obj = AccountImages.objects.all().order_by("-id")
    
    return render(request,"allpics.html",context={"data":obj})
