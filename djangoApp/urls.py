"""djangoApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import include, path
from rest_framework_simplejwt import views
from register.views import UserCreate, UserDetail

urlpatterns = [
    path('', include('members.urls')),
    path('', include('apis.urls')),
    path('admin/', admin.site.urls),
    path("api/auth/register/", UserCreate.as_view(), name="register"),
    path("api/auth/me/", UserDetail.as_view(), name="me"),
    path(
        "api/auth/obtain/token/",
        views.TokenObtainPairView.as_view(),
        name="obtain-token",
    ),
    path(
        "api/auth/obtain/refreh/",
        views.TokenRefreshView.as_view(),
        name="refresh-token",
    )    
]