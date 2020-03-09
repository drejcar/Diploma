from django.forms import ModelForm
from FortiGate.models import *


class addFortigateForm(ModelForm):
    class Meta:
        model = addFortigate
        fields = ["ipaddress", "username", "password"]

    def clean(self):
        super(addFortigateForm, self).clean()
        ipaddress = self.cleaned_data.get("ipaddress")
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        # pogoji
        #if len(str(ipaddress)) != 15:
        #   self.errors['ipaddress'] = self.error_class(['maximum 15 characters allowed in IPv4 address!'])

        return self.cleaned_data

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
