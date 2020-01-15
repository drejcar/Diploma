import requests
# from rest_framework import requests.models.Response
from django.shortcuts import render
from rest_framework.decorators import api_view

from urllib3.exceptions import InsecureRequestWarning
from bs4 import BeautifulSoup

from .forms import addFortigate


@api_view(['GET'])
def newFortigate(request):
  #  form = addFortigate()
 #   template_name='templates/addFortigate.html'
    if request.method == 'GET':
        # create a form instance and populate it with data from the request:
        form = addFortigate(request.GET)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            print(form.cleaned_data['username'])
            username = form.cleaned_data['username']
            print(form.cleaned_data['password'])
            password = form.cleaned_data['password']
            print(form.cleaned_data['ipaddress'])
            ipaddress = form.cleaned_data['ipaddress']
            print(form.cleaned_data['contype'])
            Connection=form.cleaned_data['contype']
            ###testiranje nacinov povezovanja
            #populate the payload with login data
            payload={'username':username,'secretkey':password}

            requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
           # args = {'form': form, 'username':username, 'password': password, 'ipaddress': ipaddress}
            url = 'https://' + ipaddress + '/'
            print(url+"\n")
            with requests.Session() as s:
                requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                res = s.get(url)
                #signin = BeautifulSoup(res._content, 'html.parser')
                #payload['token_code'] = signin.find('input', id='token_code')['value']
                f=requests.get(url, data=payload, verify=False)
                a=f.text
                print(a)
                return f
            return f




        # if a GET (or any other method) we'll create a blank form
    else:
        return 4
        #return render(request, 'addFortigate.html', {'form': form})
        #form = addFortigate()
    return render(request, 'addFortigate.html', {'form': form})
