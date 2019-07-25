from django.db import models

# Create your models here.
from hris.models import Employee

class Paycal(models.Model):
    p_period = models.IntegerField()
    employee = models.ForeignKey(Employee,on_delete = models.CASCADE)
    ei_er = models.DecimalField(max_digits = 16, decimal_places = 5)
    cpp_er = models.DecimalField(max_digits = 16, decimal_places = 5)
    qpip_er = models.DecimalField(max_digits = 16, decimal_places = 5)
    wcb_er = models.DecimalField(max_digits = 16, decimal_places = 5)
    cnt_er = models.DecimalField(max_digits = 16, decimal_places = 5)
    hsf_er = models.DecimalField(max_digits = 16, decimal_places = 5)
    vac_er = models.DecimalField(max_digits = 16, decimal_places = 5)
    pmtf_er = models.DecimalField(max_digits = 16, decimal_places = 5)
    ei_ee = models.DecimalField(max_digits = 16, decimal_places = 5)
    cpp_ee = models.DecimalField(max_digits = 16, decimal_places = 5)
    qpip_ee = models.DecimalField(max_digits = 16, decimal_places = 5)
    taxp_ee = models.DecimalField(max_digits = 16, decimal_places = 5)
    taxf_ee = models.DecimalField(max_digits = 16, decimal_places = 5)
    earning_pp = models.DecimalField(max_digits = 16, decimal_places = 5)
    
