from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import django

# Create your models here.


class User(models.Model):
    user_id = models.CharField(max_length=20)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    SEX = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    gender = models.CharField(max_length=1, choices=SEX)
    mobile_number = PhoneNumberField(null=False, blank=False, unique=True)
    email = models.EmailField(max_length=40, default='zzzz@yyy')

    dob = models.DateField(null=False, default=django.utils.timezone.now)
    nationality = models.CharField(max_length=20, default='Japan')

    security_question1 = models.TextField(null=True, max_length=80)
    security_question2 = models.TextField(null=True, max_length=80)
    security_answer1 = models.TextField(max_length=80, null=True)
    security_answer2 = models.TextField(max_length=80, null=True)
    wallet_id = models.CharField(max_length=50, default='ADCD')

    registration = models.DateField(null=False, default=django.utils.timezone.now)


class UPreference(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    #image = models.ImageField(upload_to='upload_image')
    ep_key = models.TextField(max_length=100)


class Password(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    password = models.CharField(max_length=30)
    ACTIVITY = (
        ('Y', 'Yes'),
        ('N', 'No')
    )
    active = models.CharField(max_length=1, choices=ACTIVITY)
    pin = models.IntegerField()


class Nft(models.Model):
    nft_address = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    info = models.TextField(max_length=100, null=True)


class NftTransactions(models.Model):
    transaction_type = models.CharField(max_length=4)
    send_receive_address = models.CharField(max_length=30)
    t_status = models.CharField(max_length=5)
    t_history = models.TextField(max_length=100, null=True)
