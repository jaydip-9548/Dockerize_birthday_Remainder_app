from django.urls import path
from . import views



urlpatterns = [
    path('remainderDataApi/',views.remainder_details,name='remainder_details')
]
