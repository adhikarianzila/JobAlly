from django.db import models


class JobModel(models.Model):

    Jobtitle = models.CharField(max_length=200)
    Jobtype = models.TextField(max_length=255)
    CompanyName = models.TextField(max_length=20)
    CompanyURL = models.TextField(max_length=200)
    JobArea = models.TextField(max_length=40)
    JobLink = models.TextField(max_length=200)
    JobDescription = models.TextField(max_length=200)
    Skill = models.TextField(max_length=200)


class meta:
    db_table = 'jobally'


class InternshipModel(models.Model):
    InternTitle = models.CharField(max_length=100)
    InternType = models.TextField(max_length=50)
    CompanyName = models.TextField(max_length=50)
    CompanyURL = models.TextField(max_length=200)
    InternArea = models.TextField(max_length=40)
    InternLink = models.TextField(max_length=100)
    InternDescription = models.TextField(max_length=200)
    Skill = models.TextField(max_length=200)


class RegistrationModel(models.Model):
    Name = models.CharField(max_length=30)
    Email = models.EmailField(max_length=40)
    Password = models.CharField(max_length=50)


class UserModel(models.Model):
    Email = models.EmailField(max_length=50)
    Password = models.CharField(max_length=50)


class ContactModel(models.Model):
    Name = models.CharField(max_length=20)
    Email = models.EmailField(max_length=50)
    Message = models.TextField(max_length=100)
    Subject = models.CharField(max_length=100, blank=True)


def __str__(self):
    return self.title
