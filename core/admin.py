from django.contrib import admin

# Register your models here.
from .models import Doctor, Facility, Commitment

admin.site.register(Doctor)
admin.site.register(Facility)
admin.site.register(Commitment)
