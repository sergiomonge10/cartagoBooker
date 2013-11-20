# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from main.forms import ContactForm, ProfileForm
from django.core.mail import EmailMultiAlternatives
from django.views.generic.create_update import create_object, delete_object,update_object
from main.models import userProfile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import sys

def contact_view(request):
	info_send = False #define si se envia la informacion
	email = ""
	title = ""
	comment = ""
	if request.method == 'POST':
		formulario = ContactForm(request.POST)
		if formulario.is_valid():
			info_send = True
			email = formulario.cleaned_data['Email']
			title = formulario.cleaned_data['Title']
			comment = formulario.cleaned_data['Comment']

			#Configuracion enviando mensaje via GMAIL
			to_admin = 'bookereditorial@gmail.com'
			html_content = "Informacion Recibida de [%s] <br><br><br>***Mensaje***<br><br>%s"%(email,comment)
			msg = EmailMultiAlternatives('Correo de Contacto',html_content,'from@server.com',[to_admin])
			msg.attach_alternative(html_content,'text/html')
			msg.send()
	else:
		formulario = ContactForm()

	ctx = {'form':formulario,'email':email,'title':title,'comment':comment,'info_send':info_send}
	return render_to_response('contact.html',ctx,context_instance=RequestContext(request))

def create_super_user(request):
	# TODO: Don't actually use this bogus admin account.
    default_username = 'admin'
    default_pass = '1234'
    default_email = 'bookereditorial@gmail.com'
    if authenticate(username=default_username, password=default_pass) is not None:
        return HttpResponse("User already created.")
    try:
        user = User.objects.create_user(default_username, default_email, default_pass)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return HttpResponse("User created!")
    except:
        print sys.exc_info()[0]
        return HttpResponse("Couldnt create user.")


def user_profile(request,uname):
	user = request.user
	ctx = {'user':user}
	return render_to_response('main/profile.html',ctx)


#def edit_user_profile(request):
def edit_user_profile(request,uname):
	#profile, created = User.objects.get_or_create(username=request.user.username)
	profile, created = userProfile.objects.get_or_create(user=request.user)
	return update_object(request,
        form_class=ProfileForm,
        object_id = profile.id,
        template_name = 'main/editProfile.html',
        extra_context = locals(),
        post_save_redirect = "/profile/"+request.user.username+"/",
    )
