"""
URL configuration for b9_library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *
from user_app import views as user_view
from app import views
from app.views import *
from user_app.views import user_login, user_signup, user_logout
import app

from user_app.views import user_signup, user_login, user_logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.welcome_page, name='home_page'),
    path('show-books/', views.show_all_books, name='show_books'),
    path('show-single-book/<int:bid>', views.show_single_book, name ='show_single_book'),
    path('add-book/',views.add_single_book, name ='add_single_book'),
    path('edit-book/<int:bid>/',views.edit_single_book, name ='edit_single_book'),
    path('delete-book/<int:bid>/',views.delete_single_book, name ='delete_single_book'),
    path('soft-delete-book/<int:bid>/',views.soft_delete_single_book, name ='soft-delete_single_book'),
    path('form-view/', views.form_view, name ='form_view'),
    path('form-views/', views.form_views, name ='form_views'),
    path('form-view_book/', views.form_view_book, name ='form_view_book'),
    path('book-form_views/', views.book_form_views, name='book_form_views'),
    path('show-inactive/', views.show_inactive_book, name='show_inactive_book'),

# user app urls

    path('user-register/', user_signup, name ='user_signup'),
    path('login/', user_login, name ='user_login'),
    path('logout/', user_logout, name ='user_logout'),

]



# show_inactive_book