from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone


class Profile(models.Model):
    DUBLIN = 'Dublin'
    MALE = 'Male'
    GENDER = (("Male", 'Male'), ("Female", 'Female'), ("Other", 'Other'))
    COUNTY = (
        ("Carlow", 'Carlow'),
        ("Cavan", 'Cavan'),
        ("Clare", 'Clare'),
        ("Cork", 'Cork'),
        ("Donegal", 'Donegal'),
        ("Dublin", 'Dublin'),
        ("Galway", 'Galway'),
        ("Kerry", 'Kerry'),
        ("Kildare", 'Kildare'),
        ("Kilkenny", 'Kilkenny'),
        ("Laois", 'Laois'),
        ("Leitrim", 'Leitrim'),
        ("Limerick", 'Limerick'),
        ("Longford", 'Longford'),
        ("Louth", 'Louth'),
        ("Mayo", 'Mayo'),
        ("Meath", 'Meath'),
        ("Monaghan", 'Monaghan'),
        ("Offaly", 'Offaly'),
        ("Roscommon", 'Roscommon'),
        ("Sligo", 'Sligo'),
        ("Tipperary", 'Tipperary'),
        ("Waterford", 'Waterford'),
        ("Westmeath", 'Westmeath'),
        ("Wexford", 'Wexford'),
        ("Wicklow", 'Wicklow'),
    )
    user = models.OneToOneField(
        User, null=True, on_delete=models.CASCADE,  related_name="profile")
    image = models.ImageField(
        upload_to="accounts/profiles/", null=True, blank=True)
    first_name = models.CharField(
        max_length=15, default='', null=False, blank=False)
    last_name = models.CharField(
        max_length=15, default='', null=False, blank=False)
    email = models.EmailField(max_length=65, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    description = models.CharField(max_length=75, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    eircode = models.CharField(max_length=10, null=True, blank=True)
    city = models.CharField(max_length=25, null=True, blank=True)
    county = models.CharField(max_length=50,choices=COUNTY, default=DUBLIN, null=True, blank=True)
    gender = models.CharField(max_length=6,choices=GENDER, default=MALE, null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '%s' % self.user.username


User.accounts = property(lambda u: Profile.objects.get_or_create(user=u)[0])
