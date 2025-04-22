from django.urls import path
from base.views import *
urlpatterns = [
    path('', home, name='home'),
    path('profile/', profile , name='profile'),
    path('details/', details , name='details'),
    path('login/', loginView , name='login'),

   
]
