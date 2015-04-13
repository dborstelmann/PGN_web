from django.conf.urls import include, url
from django.contrib import admin
from pgn_web import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'pgn_db.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^auth/linkedin/callback', views.linkedin_callback),
    url(r'^create_user', views.create_user),
    url(r'^login/', views.login_view, name='login'),
    url(r'^register', views.register_view, name='register'),
    url(r'^search/', views.search_view, name='search'),
    url(r'^admin/', include(admin.site.urls)),
]
