from django.contrib.auth.decorators import login_required
from django.conf.urls.defaults import *

urlpatterns = patterns('main.views',
	url(r'^profile/(?P<uname>[-\w]+)/edit/$',view="edit_user_profile", name="edit_profile"),
	url(r'^profile/(?P<uname>[-\w]+)/$',view="user_profile", name="profile"),
	url(r'^create/user/su/mama/$',view="create_super_user", name="user"),
	url(r'^contact/$', view="contact_view", name="contact"),
)
