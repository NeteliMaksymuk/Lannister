from django.contrib import admin
# psql -h localhost -U postgres
# Register your models here.
from .models import UserModel

admin.site.register(UserModel)