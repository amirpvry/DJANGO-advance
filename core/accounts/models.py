from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin , BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)
    
class User(AbstractBaseUser , PermissionsMixin):
    email = models.EmailField(max_length=255 , unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(max_length= 256 , default= True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = UserManager()

    created_date = models.DateTimeField(auto_now_add= True)
    updated_date = models.DateTimeField(auto_now= True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    first_name = models.CharField (max_length= 255)
    last_name = models.CharField (max_length= 255)
    description = models.TextField (max_length= 255)
    created_date = models.DateTimeField(auto_now_add= True)
    updated_date = models.DateTimeField(auto_now= True)

    def __str__(self) :

        return self.user.email
    
@receiver(post_save, sender=User)
def save_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
