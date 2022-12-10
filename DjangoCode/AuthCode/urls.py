from django.urls import path
from AuthCode import views

    # Telling where to do if we get the urls
urlpatterns = [
    path('', views.Login, name='Login'),
    path('signup/', views.Signup, name='Signup'),
    path('profile/', views.Profile, name='Profile'),
    path('logout/', views.Logout, name='Logout'),
]
