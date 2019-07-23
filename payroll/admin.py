from django.contrib import admin
from payroll.models import Paycal
# Register your models here.
@admin.register(Paycal)
class PaycalAdmin(admin.ModelAdmin):
    list_display = (
        'p_period',
        'employee',
        'ei_er',
        'cpp_er',
        'qpip_er',
        'wcb_er',
        'cnt_er',
        'hsf_er',
        'vac_er',
        'pmtf_er',
        'ei_ee',
        'cpp_ee',
        'qpip_ee',
        'taxp_ee',
        'taxf_ee',
)
