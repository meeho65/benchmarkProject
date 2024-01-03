"""
URL configuration for SE_project project.

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
from kleemoapp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.SignUp,name='signup'),
    path('login/', views.LogIn,name='login'),
    path('home/', views.HomePage,name='home'),
    path('compare/', views.CompPage,name='compare'),
    path('profile/', views.Profile,name='profile'),
    path('profile_update/', views.ProfileUpdate,name='profile_update'),
    path('profile_update2/', views.ProfileUpdate2,name='profile_update2'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('product/<str:type>/<str:product_name>/', views.one_prod_Page,name='oneProd'),
    path('bookmark/', views.BookMark,name='bookmark'),
    path('reviews/', views.Reviews,name='review'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)