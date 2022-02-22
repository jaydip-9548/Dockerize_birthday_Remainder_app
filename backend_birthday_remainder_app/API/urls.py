from django.urls import path
# from .views import remainderDataOperation
from . import views




urlpatterns = [
    # path('remainderDataApi/',remainderDataOperation.as_view(),),
    path('remainderDataApi/',views.DemoView),
     path('userRegisterApi/',views.user_register,name='user_register'),
    path('userLoginApi/',views.user_login,name='user_login'),
    path('userLogoutApi/',views.logout,name='logout'),
    ]
