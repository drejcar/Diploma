import django_tables2 as tables
from .models import FortiGate

class FortiTable(tables.Table):
    class Meta:
        model=FortiGate
        template_name="django_tables2/bootstrap.html"
        fields=('ipaddress','hostname','token')