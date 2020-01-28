import requests
from urllib3.exceptions import InsecureRequestWarning
from FortiGate.forms import addFortigateForm
from django.shortcuts import HttpResponse, render, redirect


def newFortigate(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        addform = addFortigateForm(request.POST)
        # check whether it's valid:
        print(addform.errors)
        if addform.is_valid():
            # process the data in form.cleaned_data as required
            print(addform.cleaned_data['username'])
            username = addform.cleaned_data['username']
            print(addform.cleaned_data['password'])
            password = addform.cleaned_data['password']
            print(addform.cleaned_data['ipaddress'])
            ipaddress = addform.cleaned_data['ipaddress']
            print(addform.cleaned_data['contype'])
            connection = addform.cleaned_data['contype']

            # testiranje nacinov povezovanja
            # populate the payload with login data

            # ssh connection

            # initiate connection according to filetype
            payload = {'username': username, 'secretkey': password}

            requests.packages.urllib3.disable_warnings()
            requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
            args = {'form': addform, 'username':username, 'secretkey': password}
            url = 'https://' + ipaddress + '/'
            print(url + "\n")
            with requests.Session() as s:
                requests.packages.urllib3.disable_warnings()
                requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

                f=requests.get(url, data=args, verify=False)
                #create a rest api user


                a=f.text
                print(a)

                #savebuffer = addform.save(commit=False)
                #savebuffer.save()
                return HttpResponse(f)
        else:
            print("invalid form")
            return render(request, "addFortigate.html", {'form': addform})
        # if a different method we'll create a blank form
    else:
        addform = addFortigateForm()
        return render(request, "addFortigate.html", {'form': addform})
