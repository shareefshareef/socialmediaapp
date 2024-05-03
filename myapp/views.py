from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth  import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Tweets
# Create your views here.


@login_required(login_url="login/")
def index_page(request):

    user_data = Tweets.objects.all().order_by("-pub_date")
    return render(request,"index.html",context={"page":"home","data":user_data})

@login_required(login_url="login/")
def add_tweet(request):

    if request.method == "POST":
        data = request.POST

        topic = data.get("topic")
        tweet = data.get("tweet_content")
        pub_date = timezone.now()
        user = User.objects.get(username = request.user.username)

        Tweets.objects.create(
            user = user,
            topic = topic,
            tweet = tweet,
            pub_date = pub_date
        )

        return redirect("/")


    return render(request,"add_tweet.html")

@login_required(login_url="login/")
def logout_page(request):
    logout(request)
    return redirect("/login/")

def login_page(request):

    if request.method == "POST":
        username = request.POST.get("user_name")
        password = request.POST.get("user_password")

        if not User.objects.filter(username=username).exists():
            messages.error(request,"Invalid Username")
            return redirect("/login/")

        user = authenticate(username = username,password = password)

        if user is None:
            messages.info(request,"Invalid Password")
            return redirect("/login/")
        else:
            login(request,user)
            return redirect("/")
    return render(request,"login.html",context={"page":"login"})

def register_page(request):

    if request.method == "POST":
        username = request.POST.get("user_name")
        password = request.POST.get("user_password")
        repassword = request.POST.get("user_repassword")

        user = User.objects.filter(username = username)
        if user.exists():
            messages.info(request,"User Already Exists...")
            return redirect("/register")
        #checking the both passwords in normal texts
        if password != repassword:
            messages.info(request,"password didn't match")
            return redirect("/register/")
        
        #creating a user 
        new_user = User.objects.create(
            username = username,
        )
        #saving the password in encrypted mode
        new_user.set_password(password)
        #saving the user 
        new_user.save()
        #informing user that account is created..
        messages.info(request,"Registration Success...")
        #redirecting to the register page
        return redirect("/register/")

    return render(request,"register.html",context={"page":"register"})

@login_required(login_url="login/")
def delete_tweet(request,tweet_id):
    tweet = Tweets.objects.get(id=tweet_id)
    tweet.delete()

    return redirect("/")

@login_required(login_url="login/")
def update_tweet(request,tweet_id):
    
    queryset = Tweets.objects.get(id=tweet_id)

    if request.method == "POST":
        data = request.POST

        utopic = data.get("topic")
        utweet = data.get("tweet_content")
        upub_date = timezone.now()

        queryset.topic = utopic
        queryset.tweet = utweet
        queryset.pub_date = upub_date

        queryset.save()

        return redirect("/")
    context = {"retrotweet":queryset}



    return render(request,"update_tweet.html",context=context)

@login_required(login_url="login/")
def add_image(request):
    return render(request,"add_image.html")

def show_my_tweets(request,username):

    
    queryset = Tweets.objects.filter(user__username = username)
    context = {"user_tweets":queryset}

    return render(request,"all_tweets.html",context=context)