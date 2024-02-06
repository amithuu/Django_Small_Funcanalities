from django.contrib import admin
from .models import CustomerUser, OtpLog

# Register your models here.
admin.site.register(CustomerUser)
admin.site.register(OtpLog)

