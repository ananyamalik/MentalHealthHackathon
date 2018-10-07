from django.conf.urls import url, include
from django.contrib import admin
from Login import views as login_views

urlpatterns = [
    url(r'^signup/$', login_views.signup_view, name='signup'),
    url(r'^login/$', login_views.login_view, name='login'),
    url(r'^admin/', admin.site.urls),
    url(r'^blogs/', include('Blog.urls')),
]
