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

from django.urls import path, re_path, include
from rest_framework.documentation import include_docs_urls
import xadmin
from rest_framework.routers import DefaultRouter

from users.views import UserProfileListView, UserLoginView, UserLoginOutView, UserCheckLoginView, UserRegisterView, UserUpdateView
from source.views import SourceRecommendBookView, SourceRecommendVideoView, PlanTableView, PlanTableViewset, UserRecordView, UserRecordViewset, UserExperienceView, UserExperienceViewset
from chat.views import UserChatRecordView, UserChatRecordViewset

router = DefaultRouter()
router.register(r'plans', PlanTableViewset, base_name="plans")
router.register(r'records', UserRecordViewset, base_name="records")
router.register(r'experiences', UserExperienceViewset, base_name="experiences")
router.register(r'chats', UserChatRecordViewset, base_name="chats")

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    re_path(r'docs/', include_docs_urls(title='一路考研', authentication_classes=[], permission_classes=[])),
    re_path(r'^', include(router.urls)),

    re_path(r'^users/getlist', UserProfileListView.as_view()),
    re_path(r'^users/login', UserLoginView.as_view()),
    re_path(r'^users/logout', UserLoginOutView.as_view()),
    re_path(r'^users/checklogin', UserCheckLoginView.as_view()),
    re_path(r'^users/register', UserRegisterView.as_view()),
    re_path(r'^users/update/(?P<update_filed>.*)/$', UserUpdateView.as_view()),

    re_path(r'^source/book', SourceRecommendBookView.as_view()),
    re_path(r'^source/video', SourceRecommendVideoView.as_view()),
    re_path(r'^source/aims_plan', PlanTableView.as_view()),
    re_path(r'^source/aims_record', UserRecordView.as_view()),
    re_path(r'^source/aims_experience', UserExperienceView.as_view()),

    re_path(r'^source/chats', UserChatRecordView.as_view()),

    # re_path(r'^source/plan/(?P<pk>.*)/$', PlanTableViewset.as_view({"get":"list", "post":"create", "put":"update", "delete":"destroy"})),
]
