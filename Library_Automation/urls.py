"""Library_Automation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from library.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home, name='home'),
    path('about', about, name='about'),
    path('logout', Logout, name='logout'),
    path('loginadmin/',Adminlogin,name='loginadmin'),
    path('loginstudent/',Student_login,name='loginstudent'),
    path('signupadmin/',Signupadmin,name='signupadmin'),
    path('signupstudent/',Signup_student,name='signupstudent'),
    path('AddBook/',Add_book,name='AddBook'),
    path('searchbook/',search_book,name='searchbook'),
    path('bookview/',View_Book,name='bookview'),
    path('studentbooksearch/',booksearch2,name='studentbooksearch'),
    path('editbook/(?P<pid>[0-9]+)',edit_book,name='editbook'),
    path('orderbook/(?P<pid>[0-9]+)',order_book,name='orderbook'),
    path('returnbook/(?P<pid>[0-9]+)',returnbook,name='returnbook'),
    path('deletebook/(?P<pid>[0-9]+)',bookdelete,name='deletebook'),
    path('fine/(?P<pid>[0-9]+)',f,name='fine'),
    path('order/',order,name='order'),
    path('orderview/',orderview,name='orderview'),
    path('fineview/',Fine,name='fineview'),
    path('vieworder/',ViewOrder,name='vieworder'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
