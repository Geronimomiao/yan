"""yan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from django.urls import path, re_path

import xadmin

from users.views import UserProfileListView, UserLoginView, UserLoginOutView, UserCheckLoginView, UserRegisterView, UserUpdateView

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    re_path(r'^users/getlist', UserProfileListView.as_view()),
    re_path(r'^users/login', UserLoginView.as_view()),
    re_path(r'^users/logout', UserLoginOutView.as_view()),
    re_path(r'^users/checklogin', UserCheckLoginView.as_view()),
    re_path(r'^users/register', UserRegisterView.as_view()),
    re_path(r'^users/update/(?P<update_filed>.*)/$', UserUpdateView.as_view()),
]
