from django.contrib import admin
from timecards.models import Allcards
# Register your models here.
@admin.register(Allcards)
class AllcardsAdmin(admin.ModelAdmin):
    list_display = ('employee_number','clocked_in','clocked_out')
    