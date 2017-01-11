from django.conf.urls import url

from . import views

app_name = "gamification"
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name = "index"),
    url(r'^register/', views.RegisterView.as_view(), name = "register"),
    url(r'^login/', views.SignInView.as_view(), name = "login"),
    url(r'^logout/', views.LogOutView.as_view(), name = "logout"),
    url(r'^trial/', views.TrialView.as_view(), name = "trial")
]