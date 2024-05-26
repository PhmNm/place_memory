from django.urls import path
from .views import login_page, dashboard, logout_handle, new_memory

urlpatterns = [
    path('', login_page, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', logout_handle, name='logout'),
    path('new-memory/', new_memory, name='new-memory'),
]
