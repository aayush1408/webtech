from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


GENDER = (
    ('MALE', 'male'),
    ('FEMALE', 'female'),
    ('OTHER', 'other'),
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=GENDER)
    birth_date = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=30, blank=True)
    city = models.CharField(max_length=20)
    pincode = models.IntegerField(null=True, blank=True)
    state = models.CharField(max_length=20)
    mobile_number = models.IntegerField(null=True, blank=True)
    # email_id = models.EmailField()
    profile_pic = models.FileField(upload_to='images', blank=True, null=True)

    def __str__(self):
        return str(self.user)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
