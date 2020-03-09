import os
import sqlite3

import requests
import paramiko
import time

from django.http import HttpResponseRedirect
from urllib3.exceptions import InsecureRequestWarning
from FortiGate.forms import addFortigateForm
from django.shortcuts import HttpResponse, render, redirect
from netmiko import Netmiko
from getpass import getpass
from django.views.generic import ListView

from FortiGate.tables import FortiTable
from .models import FortiGate

class homePage(ListView):
    model = FortiGate
    conn = sqlite3.connect('FortiGate.db')
    c = conn.cursor()
    c.execute('SELECT * FROM Forti')
    dbOne=c.fetchall()
    for row in dbOne:
        FortiGate.create(row[1],row[0],row[2])
    table_class=FortiTable
    template_name = 'home.html'























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

            # testiranje nacinov povezovanja
            # populate the payload with login data
            FG = {
                "host": ipaddress,
                "username": username,
                "password": password,
                "device_type":"fortinet"
            }
            exists = 0
            net_connect = Netmiko(**FG)
            # send_config_set() will automatically enter/exit config mode
            output = net_connect.send_command("get system api-user")
            print(output)
            string = output.split(" ")

            for i in string:
                if i == "Rest_Admin":
                    exists = 1

            if exists == 0:
                # create rest admin profile - allow all - REST_ACC
                commandset=["config system accprofile","edit REST_ACC","set netgrp read-write","set loggrp read-write","set fwgrp read-write","next","end"]

                output = net_connect.send_config_set(commandset)
                print(output)

                commandset2 = ["config system api-user", "edit Rest_Admin", "set accprofile REST_ACC",
                              "set cors-allow-origin https://fndn.fortinet.net", "config trusthost", "edit 1",
                              "set ipv4-trusthost 10.0.0.0/8", "next", "edit 2", "set ipv4-trusthost 192.168.1.0/24",
                              "next","end","end"]

                output = net_connect.send_config_set(commandset2)
                print(output)
                output = net_connect.send_command("execute api-user generate-key Rest_Admin")
                print(output)
                restkey = output.split(' ')[3]
                restkey=restkey.split('\n')[0]
                print(restkey)
                output = net_connect.send_command("get sys global")
                #print(output)
                hostname = output.split(":")[77]
                hostname = hostname.split(" ")[1]
                net_connect.disconnect()
                dbvalues = (hostname, ipaddress, restkey)
                # add the key to the database, create table/database if empty
                conn = sqlite3.connect('FortiGate.db')
                c = conn.cursor()

                c.execute('''CREATE TABLE IF NOT EXISTS Forti
                             (hostname text PRIMARY KEY UNIQUE , ipaddress text NOT NULL, key text NOT NULL)''')
                c.execute("INSERT INTO Forti VALUES (?,?,?)", dbvalues)
                FortiGate.create(ipaddress,hostname,restkey)
                conn.commit()
                conn.close()
                #ssh.close()
                return HttpResponseRedirect('/')
                return
            net_connect.disconnect()
            return HttpResponse(output)
        else:
            print("invalid form")
            return render(request, "addFortigate.html", {'form': addform})
        # if a different method we'll create a blank form
    else:
        addform = addFortigateForm()
        return render(request, "addFortigate.html", {'form': addform})
