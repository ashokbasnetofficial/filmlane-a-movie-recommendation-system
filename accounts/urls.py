
from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login_User,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout_user,name='logout')
    # path('')
    # path('register',views.register,name='register')
    
]
