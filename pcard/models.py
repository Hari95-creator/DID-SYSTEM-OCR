from django.db import models


# Create your models here.
class ImageUploadModel(models.Model):
    description = models.CharField(max_length=255, blank=True)
    image = models.ImageField()
    uploaded_at = models.DateTimeField(auto_now_add=True)


class aadhardb(models.Model):
    aadharnumber = models.CharField(max_length=100, primary_key=True, unique=True)
    aadharname = models.CharField(max_length=100)
    aadharbirth = models.CharField(max_length=100)
    aadhargender = models.CharField(max_length=100)
    aadharimage = models.ImageField()


class dirverdata(models.Model):
    drlicenceno = models.CharField(max_length=100, primary_key=True, unique=True)
    drlicencename = models.CharField(max_length=100)
    drlicencelname = models.CharField(max_length=100)
    drlicenceimage = models.ImageField()


class voteriddata(models.Model):
    voterfname = models.CharField(max_length=100, primary_key=True, unique=True)
    votername = models.CharField(max_length=100)
    voterimage = models.ImageField(default=True)


class panddata(models.Model):
    panno = models.CharField(max_length=100, primary_key=True, unique=True)
    fathername = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    pandob = models.CharField(max_length=100, default=True)
    panimage = models.ImageField(default=True)


class panapi(models.Model):
    uid = models.CharField(max_length=100, unique=True)
    pname = models.CharField(max_length=100)
    fname = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)


class aadharapi(models.Model):
    uid = models.CharField(max_length=100, unique=True)
    aadharno = models.CharField(max_length=100)
    pname = models.CharField(max_length=100)
    fname = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)


class drvingapi(models.Model):
    uid = models.CharField(max_length=100, unique=True)
    licenceno = models.CharField(max_length=100)
    licencename = models.CharField(max_length=100)
    fathername = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    issuedate = models.CharField(max_length=100)
    validate = models.CharField(max_length=100)
    authtodr = models.CharField(max_length=100)
    authtodrive = models.CharField(max_length=100)


class voterapi(models.Model):
    voterfname = models.CharField(max_length=100)
    votername = models.CharField(max_length=100)
    voterid = models.CharField(max_length=100)


class FileUploadModel(models.Model):
    description = models.CharField(max_length=255, blank=True)
    file = models.FileField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    choices = (
        ('SBI', 'State Bank Of India'),
        ('Alla', 'Allahabad Bank'),
        ('Yes', 'Yes Bank'),
    )

    select_bank = models.CharField(max_length=4, choices=choices, default='green')
