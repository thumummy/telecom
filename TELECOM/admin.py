from django.contrib import admin
from TELECOM.models import customer,ourservices,imagemodel,workers

# Register your models here.
admin.site.register(customer)
admin.site.register(ourservices)
admin.site.register(imagemodel)
admin.site.register(workers)