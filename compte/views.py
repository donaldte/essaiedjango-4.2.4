from django.shortcuts import redirect, render

from django.core.mail import send_mail, EmailMessage

from compte.utils import send_email_with_template
from .models import User
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str # force_text on django < 1.5
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

from django.conf import settings

from .token import TokenGenerator

generate_token = TokenGenerator()

from django.contrib.auth.decorators import login_required, permission_required

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

def user_registration_view(request, *args, **kwargs):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        
        if password != password2:
            
            messages.error(request, "Les mots de passe ne correspondent pas.")
            
        elif User.objects.filter(username=username).exists():
            
            messages.error(request, "Ce nom d'utilisateur existe déjà.")  
            
        elif User.objects.filter(email=email).exists():
            
            messages.error(request, "Cet email existe déjà.")  
            
        else:
                
            user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email)
            
            user.is_active = False
            user.save()
            
            
            subject = "Message de bienvenue"
            
            message = "Bienvenue sur notre site. {} {}.".format(user.first_name, user.last_name)
            
            to_email = user.email
            
            from_email = settings.EMAIL_HOST_USER
            
            send_mail(subject, message, from_email, [to_email], fail_silently=False)
            
            template_name = 'registration/activate_account.html'
            
            subject = "Activation de compte"
            
            
            domain = get_current_site(request).domain
            
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            
            token = generate_token.make_token(user)
            
            
                
            context = {
                'user': f"{user.first_name} {user.last_name}",
                'domain': domain,
                'uid': uid,
                'token': token,
            }
            
            send_email_with_template(subject, template_name, context, [to_email], from_email)
            
            
            
            # send email to user to activate account
            
            messages.success(request, "Votre compte a été créé avec succès.")        
           
    
    
    return render(request, 'registration/register.html', {})




def activate_account_view(request, uidb64, token, *args, **kwargs):
    
    try: 
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist): 
        user = None
        
    
    if user is not None and generate_token.check_token(user, token):
        
        user.is_active = True
        user.save()
        
        messages.success(request, "Votre compte a été activé avec succès.")    

    else:
        
        messages.error(request, "Le lien d'activation est invalide.")
        
    return redirect('compte:login')


def user_login_view(request, *args, **kwargs):
    
    if request.method == 'POST':
        next = request.GET.get('next')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = User.objects.filter(username=username)
        
        if user.exists():
            
            if user.first().is_active:
                
                user = authenticate(request, username=username, password=password)
                
                #user = user.first().check_password(password)
                
                if user is not None:
                    
                    login(request, user)
                    
                    messages.success(request, "Vous êtes connecté.")
                    
                    if next:
                        return redirect(next)
                    
                else:
                    
                    messages.error(request, "Le nom d'utilisateur ou le mot de passe est incorrect.")
                    
            else:
                    
                messages.error(request, "Votre compte n'est pas encore activé. Veuillez vérifier votre boîte de réception.")    
                
        else:
            
            messages.error(request, "Le nom d'utilisateur ou le mot de passe est incorrect.")          
    
    return render(request, 'registration/login.html', {})


# 
"""
Etape de reinitialisation de mot de passe
1. L'utilisateur entre son email
2. On vérifie si l'email existe dans la base de données
3. On envoie un email avec un lien de reinitialisation de mot de passe

4. L'utilisateur clique sur le lien et est redirigé vers une page de reinitialisation de mot de passe

creer une session pour l'utilisateur: request.session['uid'] = user.id
recuperer la session: request.session.get('uid')
user = User.objects.get(pk=request.session.get('uid'))
supprimer la session: del request.session['uid']
user.set_password(new_password)
user.save()
"""

def logout_view(request, *args, **kwargs):
    
    user = request.user
    
    # if user.has_perm('compte.view_user_info'):
        
    #     print("User can view user info")
        
    # # many perms 
    
    # if user.has_perms(['compte.view_user_info', 'compte.view_group_info']):
        
    #     print("User can view user info and group info")    
    
    
    # if user.is_student:
    #     print('user is student')
        
    logout(request)
    
    messages.success(request, "Vous êtes déconnecté.")
    
    return redirect('compte:login')


