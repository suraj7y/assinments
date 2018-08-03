# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Person, City, Country
# Register your models here.
admin.site.register(Person)
admin.site.register(City)
admin.site.register(Country)
