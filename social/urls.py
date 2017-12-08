"""social URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from posts import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.posts_list, name='posts-list'),
    url(r'^detail/(?P<post_id>\d+)/$', views.post_detail, name='post-detail'),
    url(r'^like/(?P<post_id>\d+)/$', views.like, name='like'),
    url(r'^sign-up', views.sign_up, name='sign-up'),
    url(r'^add/$', views.post_add, name='post-add'),
    url(r'^edit/(?P<post_id>\d+)/$', views.post_edit, name='post-edit'),
    url(r'^post/(?P<post_id>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^sign-in/$', auth_views.login, {'template_name': 'posts/sign_in.html'}, name='sign-in'),
    url(r'^sign-out', auth_views.logout, {'next_page': '/'}, name='sign-out'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
