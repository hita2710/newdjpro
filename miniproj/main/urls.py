from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from django.views.static import serve
from django.conf.urls import url

urlpatterns=[
    path('',views.home,name="home"),
    path('register/',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('display/',views.display,name="display"),
    path('upload/',views.upload,name="upload"),
    path('file_list/',views.file_list,name="file_list"),
    path('logout/',views.logout,name="logout"),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':  settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    