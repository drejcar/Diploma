from django.core.validators import validate_ipv4_address
from django.db import models


# Create your models here.
class addFortigate(models.Model):
    Choices = (('html', 'HTML'), ('ssh', 'SSH'))
    ipaddress = models.CharField(max_length=15,default="192.168.1.99",name="ipaddress",blank=True,validators=[validate_ipv4_address])
    username = models.CharField(max_length=22, blank=True,name="username")
    password = models.CharField(max_length=30,blank=True,name="password")
    contype = models.CharField(max_length=4, choices=Choices, default="html",blank=True,name="contype")

    def __str__(self):
        return self.ipaddress


class FortiGate(models.Model):
    ipaddress = models.GenericIPAddressField(protocol="IPv4", blank=False, default="192.168.1.99")
    username = models.CharField(max_length=22, blank=False)
    password = models.CharField(blank=True, max_length=30)
    contype = models.CharField(max_length=4)

    def __str__(self):
        return self.ipaddress
