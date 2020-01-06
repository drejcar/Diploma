from django import forms
from django.core.validators import ip_address_validators, RegexValidator
from django.core.exceptions import ValidationError
from django.conf import settings
import urllib.request
from django.http import response
from django.shortcuts import render


class addFortigate(forms.Form):
    connections=['html','ssh','serial']
    ipaddress = forms.CharField(label='IPv4 address:',initial='192.168.1.99')
    username = forms.CharField(label='Username',initial='admin')
    password = forms.CharField(label='password',initial='', widget=forms.PasswordInput, required=False )
    contype = forms.RadioSelect(choices=connections)
    address=str(ipaddress)


    address='https://'+address
    values = {'username': username,
              'password': password}





 #   def clean(self):
 #       cleaned_data = super().clean()
 #       super().ipaddress = cleaned_data.get("ipaddress")
 #       super().username = cleaned_data.get("username")
 #       super().password = cleaned_data.get("password")
 #   clean()


 #   def search(self, ipaddress,values):
 #       data = urllib.parse.urlencode(values)
 #       data = data.encode('ascii')  # data should be bytes
 #       req = urllib.request.Request(ipaddress, data)
 #       with urllib.request.urlopen(req) as response:
 #           the_page = response.read()

 #   result = {}
 #   if response.status_code == 200:  # SUCCESS
 #       result = response.json()
 #       result['success'] = True
 #   else:
 #       result['success'] = False
 #      if response.status_code == 404:  # NOT FOUND
 #           result['message'] = 'No entry found for "%s"' % ipaddress
 #       else:
 #           result['message'] = 'The Firewall is not available at the moment. Please try again later, or try another ip.'
 #   return result