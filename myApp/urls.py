from django.urls import path
from .views import home, dashboard, logoutHandle

urlpatterns = [
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', logoutHandle, name='logout'),
]
