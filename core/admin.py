from django.contrib import admin

# Register your models here.
from .models import Medic, Facility, Commitment, Request

admin.site.register(Medic)
admin.site.register(Facility)
admin.site.register(Commitment)
admin.site.register(Request)
