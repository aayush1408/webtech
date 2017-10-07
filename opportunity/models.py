from django.db import models
from django.contrib.auth.models import User
# from access.models import student
# Create your models here.


class opportunity(models.Model):
    title = models.CharField(max_length=50, default="title")
    added_by = models.OneToOneField(User)
    description = models.CharField(max_length=100, default='description')
    last_apply_date = models.DateTimeField('last_date_to_apply')
    # resume = models.ForeignKey(student, on_delete=models.CASCADE)
    # temp_applications = models.ForeignKey(student, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class assigned_opportunities(models.Model):
    # assigned_to = models.ForeignKey(student, on_delete=models.CASCADE)
    post = models.OneToOneField(opportunity)

    def __str__(self):
        return self.post


class comment(models.Model):
    comment = models.CharField(max_length=50, default='comment')
    post = models.OneToOneField(opportunity)
    # commented_by = models.ForeignKey(student)

    def __str__(self):
        return self.post
