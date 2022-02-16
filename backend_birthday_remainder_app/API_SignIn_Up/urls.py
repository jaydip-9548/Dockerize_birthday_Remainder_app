from django.urls import path
from . import views



urlpatterns = [
    path('userDataApi/',views.user_register,name='user_register'),
    path('userLoginApi/',views.user_login,name='user_login'),
    path('userStatus/',views.userRegister,name='userRegister'),
]
