from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from django.core.mail import send_mail

from django.utils import timezone

from .manager import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    Username and password are required. Other fields are optional.
    """

    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    email = models.EmailField(_("email address"), unique=True,  blank=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    
    is_student = models.BooleanField(
        _("student status"),
        default=False,
        help_text=_("Designates whether the user is a student."),
    )
    
    is_professor = models.BooleanField(
        _("professor status"),
        default=False,
        help_text=_("Desigantes whether the user is a prof")
    )
    
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    objects = UserManager() # User.objects.all()
    

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]


    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        
        
        

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)
    
    
    
    # def has_perm(self, perm, obj=None):
    #     """ check permission """
        
    #     return True   
    
    

class CustomPermission(models.Model):
    
    """
    Custom Permission model
    """
    
    class Meta:
       
       managed = False
       
       permissions = (
              ('view_user_info', 'Can view user info'),
              ('view_group_inof', 'Can view group info'),
              ('view_permission', 'Can view permission'),
              ('view_content_type', 'Can view content type'),
              ('view_session', 'Can view session'),
              ('view_message', 'Can view message'),
              ('view_logentry', 'Can view log entry'),
              ('view_book', 'Can view book'),
              ('view_author', 'Can view author'),
              ('view_publisher', 'Can view publisher'),
              ('view_category', 'Can view category'),
              ('view_comment', 'Can view comment'),
              ('view_bookinstance', 'Can view bookinstance'),
              ('view_genre', 'Can view genre'),
              ('view_language', 'Can view language'),
              
       )