
from multiprocessing import AuthenticationError
from multiprocessing.context import ForkContext
from django.shortcuts import redirect, render
from django.views import generic
from django.urls  import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, AuthenticationForm
from django.contrib.auth import logout
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q 
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

# user registration
class signUp(generic.CreateView):
    form_class = UserCreationForm
    
    # redirect user to login url after registration
    # 'reverse_lazy' is used instead of just 'reverse' because for all generic class based views the urls are not loaded when the 
    # file is imported. Lazy of the 'reverse' type loads the generic class later when they are available
    success_url = reverse_lazy("login")    
    template_name =  'registration/register.html'

# user login
# class signIn(generic.CreateView):
#     form_class = AuthenticationForm
    
#     success_url = reverse_lazy('index')
#     template_name = "registration/login.html"
    
# user logout
# def logOut(request):
#     logout(request)
#     return redirect(to = 'signUp')

# resetting passwords
def password_reset_request(request):
    if request.method == 'POST':
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            print(data)
            associated_users = User.objects.filter(Q(email=data))
            print(associated_users)
            if associated_users.exists():
                

                for user in associated_users:
                    subject = 'Password Reset Requested'
                    email_template_name = "user/password_reset_email.txt"
                    # in production, reset domain to actual website name and protocol to https
                    c = {
                        "email":user.email,
                        "domain": '127.0.0.1:8000',
                        'site_name': 'Senami',
                        'uid':urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',                            
                    }
                    email = render_to_string(email_template_name, c)
                    # in production also, send_mail function will be updated with verified email address
                    try:
                        send_mail(subject, email, 'admin@gmail.com', [user.email], fail_silently= False)
                    except BadHeaderError:
                        return HttpResponse('Invalid Header Found')
                    
                    messages.success(request, 'A message with a reset password instructions has been emailed to you')
                    return redirect('index')
                messages.error(request, 'Entered invalid email address')
    password_reset_form = PasswordResetForm()
    context = {"password_reset_form": password_reset_form}
    return render(request, 'registration/password_reset.html', context)

@login_required
def index(request):
    return render(request, 'chat/index.html')

@login_required
def room(request, room_name):
    return render(request, 'chat/room.html', {"room_name": room_name})