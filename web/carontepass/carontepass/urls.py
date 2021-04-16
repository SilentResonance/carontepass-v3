"""carontepass URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
#from django.conf.urls import include, url
from django.urls import include, re_path
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from access.viewsets import UserViewSet, DeviceViewSet
from access.views import DeviceIDList, homepage, personal_info, device_info, global_charts, register
#from django.contrib.auth.views import login, logout
from django.contrib.auth import (
    REDIRECT_FIELD_NAME, get_user_model, login as auth_login,
    logout as auth_logout, update_session_auth_hash,
)
from django.contrib import admin
from django.contrib.auth import views as auth_views

router = DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'device', DeviceViewSet)

urlpatterns = [
    re_path(r'^admin', admin.site.urls),
    re_path(r'^api/1/', include(router.urls)),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^api/1/device/(?P<code>.+)$', DeviceIDList.as_view()),
    re_path(r'^commons/', include('commons.urls')),
    re_path(r'^accounts/profile/$', homepage, name='homepage'),
    re_path(r'^accounts/profile/info$', personal_info , name='personal_info'),
    re_path(r'^accounts/profile/device$', device_info , name='device_info'),
    re_path(r'^charts$', global_charts , name='gobal_charts'),
    re_path(r'^registration$', auth_views.LoginView.as_view(template_name="registration/login.html") , name='register'),
    re_path(
        r'^$', 
        auth_views.LoginView.as_view(template_name="registration/login.html"),
        name='login',
    ),
    re_path(r'^logout/$',
        auth_views.LogoutView.as_view(template_name="registration/logout.html"),
        {'next_page': '/'},
        name='logout',
    ),
]

# urlpatterns = [
#     url(r'^admin/', include(admin.site.urls)),
#     url(r'^api/1/', include(router.urls)),
#     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
#     url(r'^api/1/device/(?P<code>.+)$', DeviceIDList.as_view()),
#     url(r'^commons/', include('commons.urls')),
#     url(r'^accounts/profile/$', homepage, name='homepage'),
#     url(r'^accounts/profile/info$', personal_info , name='personal_info'),
#     url(r'^accounts/profile/device$', device_info , name='device_info'),
#     url(r'^charts$', global_charts , name='gobal_charts'),
#     url(r'^registration$', register , name='register'),
#     url(
#         r'^$', login,
#         name='login',
#     ),
#     url(r'^logout/$',
#         logout,
#         name='logout',
#     ),
# ]
