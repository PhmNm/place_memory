from django.urls import path
from .views import login_page, dashboard, logoutHandle

urlpatterns = [
    path('', login_page, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', logoutHandle, name='logout'),
]
