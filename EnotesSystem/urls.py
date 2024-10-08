from django.contrib import admin
from django.urls import path
from Enotes.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('register/', register, name='register'),
    path('user_login/', user_login, name='user_login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('profile/', profile, name='profile'),
    path('addNotes/', addNotes, name='addNotes'),
    path('viewNotes/', viewNotes, name='viewNotes'),
    path('editNotes/<int:pid>/', editNotes, name='editNotes'),
    path('deleteNotes/<int:pid>/', deleteNotes, name='deleteNotes'),
    path('changePassword/', changePassword, name='changePassword'),  # Fixed this line
    path('logout/', Logout, name='logout'),
]
