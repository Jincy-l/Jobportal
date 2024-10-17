from django.urls import path
from . import views
from django.conf.urls.static import static


urlpatterns = [
     path("",views.index,name='index'),
     path("mainindex",views.mainindex,name='mainindex'),
     path("userlogin",views.user_login,name='user_login'),
     path("userregister",views.user_register,name='user_register'),
     
]