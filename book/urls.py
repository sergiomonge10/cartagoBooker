from django.contrib.auth.decorators import login_required
from django.conf.urls.defaults import *

urlpatterns = patterns('book.views',

	url(r'^$',view="my_books_view",name="my_books"),
	url(r'^add/$',view="add_book_view",name="add_book"),

)