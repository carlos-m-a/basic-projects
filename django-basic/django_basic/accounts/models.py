from core.models import BaseModel
from django.conf import settings
from django.contrib.auth.models import AbstractUser, Group
from django.core import validators
from django.db import models
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class UsernameValidator(validators.RegexValidator):
    regex = r"^[a-z0-9_]{3,30}\Z"
    message = _(
        "Enter a valid value. This value may contain only lowercase letters, "
        "numbers, and underscores (_), between 3 and 30 characters long."
    )
    flags = 0

username_validator = UsernameValidator()


# DELETE ONE OPTION OR OTHER DEPENDING OF THE TYPE OF SYSTEM:
# B2O (business to organizacions = B2B)
# B2P (business to people = B2C)


######################################################
##              For B2P (=B2C)                      ##
######################################################

class User(BaseModel, AbstractUser):
    PREFIX = "usr"
    # 1. IDs and AUTH data
    username = models.CharField(
        _("username"),
        max_length=30,
        unique=True,
        help_text=_(
            "Required. Between 3 and 30 characters. Lowercase letters, digits and underscore only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    email = models.EmailField(_("email address"), unique=True)
    phone_number = models.CharField(max_length=20, blank=True)
    first_name = models.CharField(_("first name"), max_length=120, blank=True)
    last_name = models.CharField(_("last name"), max_length=120, blank=True)

    def deactivate(self):
        self.is_active = False
        self.set_unusable_password()
        self.save()

    def reactivate(self):
        self.is_active = True
        self.save()

    def __str__(self):
        return self.email


######################################################
##              For B2O (=B2B)                      ##
######################################################

class User(BaseModel, AbstractUser):
    PREFIX = "usr"
    # 1. IDs and AUTH data
    username = models.CharField(
        _("username"),
        max_length=30,
        unique=True,
        help_text=_(
            "Required. Between 3 and 30 characters. Lowercase letters, digits and underscore only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    email = models.EmailField(_("email address"), unique=True)
    phone_number = models.CharField(max_length=20, blank=True)
    first_name = models.CharField(_("first name"), max_length=120, blank=True)
    last_name = models.CharField(_("last name"), max_length=120, blank=True)

    # 2. Flags for B2O - B2B
    is_sso_only = models.BooleanField(
        default=False,
        help_text="If True, only SSO login is allowed, password login is forbidden."
    )
    is_managed = models.BooleanField(
        default=False,
        help_text="If True, email and username are not editable by the user."
    )

    def deactivate(self):
        self.is_active = False
        self.set_unusable_password()
        self.save()

    def reactivate(self):
        self.is_active = True
        self.save()

    @property
    def can_change_password(self):
        return not self.is_sso_only

    @property
    def can_change_email(self):
        return not self.is_managed

    @property
    def can_change_username(self):
        return not self.is_managed

    def __str__(self):
        return self.email


class Organization(BaseModel):
    PREFIX = "org"
    name = models.CharField(max_length=120)
    # like username, e.g. "acme_corp"
    handle = models.CharField(
        max_length=30,
        unique=True,
        validators=[username_validator],
        error_messages={
            "unique": _("An organization with that handle already exists."),
        },
    )
    domain = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(
        default=True,
        help_text="Indica si la organización está activa o suspendida."
    )
    group = models.OneToOneField(
        Group,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="organization"
    )
    def __str__(self):
        return self.name


class OrganizationMembership(BaseModel):
    PREFIX = "mem"

    class Roles(models.TextChoices):
        OWNER = 'OWNER', 'Owner'
        ADMIN = 'ADMIN', 'Admin'
        MEMBER = 'MEMBER', 'Member'

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="usr_memberships"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="org_memberships"
    )
    role = models.CharField(
        max_length=15,
        choices=Roles.choices,
        default=Roles.MEMBER
    )

    class Meta:
        unique_together = ('organization', 'user')

    def __str__(self):
        return f"{self.user} - {self.organization} ({self.role})"


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        null=False, 
        related_name='profile'
    )
    is_verified = models.BooleanField(
        null=False, 
        default=False
    )
    is_private = models.BooleanField(
        null=False, 
        default=False
    )
    date_of_birth = models.DateField(
        null=True, 
        blank=True
    )
    sex_or_genre = models.PositiveSmallIntegerField(
        null=False, 
        default=1
    )
    avatar_image = models.ImageField(
        upload_to='images/', 
        null=True, 
        blank=True, 
        max_length=254
    )
    description_text = models.CharField(
        blank=True, 
        max_length=254, 
        null=True
    )
    # Inside organizations, normally users has a organization id, different from database id
    other_id = models.CharField(
        blank=True, 
        max_length=128, 
        null=True
    )

    def __str__(self):
        return self.user.username


class Setting(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        null=False, 
        related_name='setting'
    )
    # Dark or light theme, for example
    frontend_theme = models.PositiveSmallIntegerField(
        null=False, 
        default=1
    )
    language = models.PositiveSmallIntegerField(
        null=False, 
        default=1
    )
    time_zone = models.PositiveSmallIntegerField(
        null=False, 
        default=1
    )
    date_format = models.PositiveSmallIntegerField(
        null=False, 
        default=1
    )
    # International (SI) vs US system
    measurement_system = models.PositiveSmallIntegerField(
        null=False, 
        default=1
    )