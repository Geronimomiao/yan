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
from django.views.decorators.csrf import csrf_exempt
from rest_framework.documentation import include_docs_urls
import xadmin

from users.views import UserProfileListView, UserLoginView, UserLoginOutView, UserCheckLoginView, UserRegisterView, UserUpdateView
from source.views import SourceRecommendBookView, SourceRecommendVideoView, PlanTableView, PlanTableViewset

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    re_path(r'docs/', include_docs_urls(title='一路考研',authentication_classes=[],
                                    permission_classes=[])),

    re_path(r'^users/getlist', UserProfileListView.as_view()),
    re_path(r'^users/login', UserLoginView.as_view()),
    re_path(r'^users/logout', UserLoginOutView.as_view()),
    re_path(r'^users/checklogin', UserCheckLoginView.as_view()),
    re_path(r'^users/register', UserRegisterView.as_view()),
    re_path(r'^users/update/(?P<update_filed>.*)/$', UserUpdateView.as_view()),

    re_path(r'^source/book', SourceRecommendBookView.as_view()),
    re_path(r'^source/video', SourceRecommendVideoView.as_view()),

    # re_path(r'^source/plan', PlanTableView.as_view()),
    re_path(r'^source/plan/', csrf_exempt(PlanTableViewset.as_view({
                                                    "get":"list",
                                                    "post":"create",
                                                    "put":"update",
                                                    "delete":"destroy"}))),
]
