"""myproject URL Configuration

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
from django.contrib import admin
from django.conf.urls import url
from django.views.generic import TemplateView
from myapp.register import signup
from django.contrib.auth import views as auth_views

from django.conf.urls.static import static
from django.conf import settings

from myapp.views import ViewAnimePost, CreateAnimePost, UpdateAnimePost, DeleteAnimePost
from myapp.views import ViewCartoonPost, UpdateCartoonPost, CreateCartoonPost,DeleteCartoonPost
from myapp.views import ViewSingerPost, ViewSingerdetailPost, UpdateSingerPost, CreateSingerPost,DeleteSingerPost
from myapp.views import ViewBlogPost,  CreateBlogPost,DeleteBlogPost

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', ViewAnimePost.as_view(), name='anime'),
    
    url(r'^home/$', ViewAnimePost.as_view(), name='home'),
    url(r'^anime_create/$', CreateAnimePost.as_view(), name='anime_create'),
    url(r'^anime_update/(?P<id>\d+)/$', UpdateAnimePost.as_view(), name='anime_update'),
    url(r'^anime_delete/(?P<pk>\d+)/$', DeleteAnimePost.as_view(), name='anime_delete'),

    url(r'^anime/onePiece/$', TemplateView.as_view( template_name='anime/onePiece.html'), name='onePiece'),
    url(r'^anime/soloLeveling/$', TemplateView.as_view( template_name='anime/soloLeveling.html'), name='soloLeveling'),
    url(r'^anime/naruto/$', TemplateView.as_view( template_name='anime/naruto.html'), name='naruto'),
    url(r'^anime/demonSlayer/$', TemplateView.as_view( template_name='anime/demonSlayer.html'), name='demonSlayer'),
    url(r'^anime/onePunchMan/$', TemplateView.as_view( template_name='anime/onePunchMan.html'), name='onePunchMan'),
    url(r'^anime/puipui/$', TemplateView.as_view( template_name='anime/puipui.html'), name='puipui'),

    url(r'^cartoon/$', ViewCartoonPost.as_view(), name='cartoon'),
    url(r'^cartoon_create/$', CreateCartoonPost.as_view(), name='cartoon_create'),
    url(r'^cartoon_update/(?P<id>\d+)/$', UpdateCartoonPost.as_view(), name='cartoon_update'),
    url(r'^cartoon_delete/(?P<pk>\d+)/$', DeleteCartoonPost.as_view(), name='cartoon_delete'),

    url(r'^singer/$', ViewSingerPost.as_view(), name='singer'),
    url(r'^singer_about/$', ViewSingerdetailPost.as_view(), name='about'),
    url(r'^singer_create/$', CreateSingerPost.as_view(), name='singer_create'),
    url(r'^singer_update/(?P<id>\d+)/$', UpdateSingerPost.as_view(), name='singer_update'),
    url(r'^singer_delete/(?P<pk>\d+)/$', DeleteSingerPost.as_view(), name='singer_delete'),

    url(r'^blog/$', ViewBlogPost.as_view(), name='blog'),
    url(r'^blog_create/$', CreateBlogPost.as_view(), name='blog_create'),
    url(r'^blog_delete/(?P<pk>\d+)/$', DeleteBlogPost.as_view(), name='blog_delete'),

    url(r'^signup/?$', signup, name='signup'),
    url(r'^login/?$', auth_views.LoginView.as_view( template_name='login.html'), name='login'),
    url(r'^logout/?$', auth_views.LogoutView.as_view( template_name='anime.html'), name='logout')
]


urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)















