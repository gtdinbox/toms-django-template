from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
import MYAPPNAME.urls
import media.urls

admin.autodiscover()
urlpatterns = patterns('',
    url(r'^',include(MYAPPNAME.urls)),

    # For social auth (facebook, twitter etc) uncomment this line
    #url(r'', include('social_auth.urls')),

    # Overwise use these lines for username/password auth
    url(r'^login/$', 'django.contrib.auth.views.login',name="login"),
    url(r'^logout/$', 'django.contrib.auth.views.logout',name="logout"),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
