from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.contrib import admin
from django.conf import settings
from book.views import pdf_view

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^', include('main.urls')),
    url(r'^mybooks/', include('book.urls')),

    url(r'^accounts/', include('registration.backends.default.urls')),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

    url(r'^$', direct_to_template, {'template': 'index.html'}),
    url(r'^about/$', direct_to_template, {'template': 'about.html'}),
    url(r'^terms/$', direct_to_template, {'template': 'terms.html'}),

    url(r'^(?P<title>[-\w]+)', pdf_view, name="book"),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    

)
