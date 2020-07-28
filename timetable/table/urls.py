from django.urls import path
from .views import index, deleteLecture, register, loginPage, logoutUser

urlpatterns = [
    path('', index, name='index'),
    path('home/', register, name='register'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('delete/<str:id>/', deleteLecture, name='delete')
]
