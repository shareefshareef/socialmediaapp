from django.urls import path
from .views import index_page,login_page,register_page,logout_page
from .views import add_tweet,delete_tweet,update_tweet,add_image
from .views import show_my_tweets,show_profile

app_name = 'myapp'

urlpatterns = [
    path("",index_page,name="index_page"),
    path("login/",login_page,name="login_page"),
    path("register/",register_page,name="register_page"),
    path("logout/",logout_page,name="logout_page"),
    path("add-tweet/",add_tweet,name="add_tweet_page"),
    path("delete-tweet/<tweet_id>/",delete_tweet,name="delete_tweet"),
    path("update-tweet/<tweet_id>/",update_tweet,name="update_tweet"),
    path("add-image/",add_image,name="add_image"),
    path("user/<username>/tweets/", show_my_tweets, name="all_tweets"),
    path("profile/<username>/",show_profile,name="show_profile")


]