from django.contrib import admin
from .models import CustomerUser, OtpLog, Profile

# Register your models here.
admin.site.register(CustomerUser)
admin.site.register(OtpLog)
admin.site.register(Profile)


