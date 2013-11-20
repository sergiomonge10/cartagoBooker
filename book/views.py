# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from book.models import Book
from book.forms import addBookForm
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseBadRequest

def pdf_view(request,title):
	book = Book.objects.filter(user=request.user).get(title=title)
	with open(book.book.path, 'r') as pdf:
		response = HttpResponse(pdf.read(), mimetype='application/pdf')
        response['Content-Disposition'] = 'inline;filename=some_file.pdf'
        return response
        pdf.closed

@login_required
def add_book_view(request):
	info = ""
	info_send = True

	if request.method == 'POST':
		book = ""
		user = ""
		year = ""
		gender = ""
		title = ""
		
		form = addBookForm(request.POST, request.FILES)

		if form.is_valid():
			book = form.cleaned_data['book']
			user = request.user
			year = form.cleaned_data['year']
			gender = form.cleaned_data['gender']
			title = form.cleaned_data['title']

			book = Book.objects.create(
				book=book, user=user, year=year, gender=gender, title=title)

			info = "Guardado exitosamente, puedes agregar otro "
			info_send = True

		else:
			info = "No se ha guardado"

		#form = addBookForm()
		ctx = {'form':form,'info':info,'info_send':info_send}
		return render_to_response('book/add_book.html',ctx,context_instance=RequestContext(request))

	else:
		form = addBookForm()
		ctx = {'form':form,'info':info,'info_send':info_send}
		return render_to_response('book/add_book.html',ctx,context_instance=RequestContext(request))

@login_required
def my_books_view(request):
	my_books = Book.objects.filter(user=request.user)
	ctx = {'my_books':my_books}
	return render_to_response('book/my_books.html',ctx,context_instance=RequestContext(request))




