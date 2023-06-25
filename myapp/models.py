from django.db import models

TYPENAME_LIST =[
    ('1','USER'),
    ('2','SELLER'),
    ('3','ADMIN')
]

STATUSLIST=[
    ('0','ACTIVE'),
    ('1','INACTIVE'),
]

ENDMONTHLIST =[
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    ('6','6'),
    ('7','7'),
    ('8','8'),
    ('9','9'),
    ('10','10'),
    ('11','11'),
    ('12','12')
]

ENDYEARLIST =[
    ('1','2022'),
    ('2','2023'),
    ('3','2024'),
    ('4','2025'),
    ('5','2026'),
    ('6','2027'),
    ('7','2028'),
    ('8','2029'),
    ('9','2030'),
]
# Create your models here.
class ROLE(models.Model):
    USER_TYPENAME = models.CharField(choices=TYPENAME_LIST,max_length=30)
    def __str__(self):
        return self.USER_TYPENAME

class USER_DETAIL(models.Model):
    U_NAME = models.CharField(max_length=30)
    U_PASSWORD = models.IntegerField()
    U_EMAIL = models.EmailField()
    U_PHONE = models.IntegerField()
    U_TYPE = models.ForeignKey(ROLE,on_delete=models.CASCADE)
    U_STATUS = models.CharField(choices=STATUSLIST,max_length=50)
    def __str__(self):
        return self.U_NAME

class COUNTRY(models.Model):
    COUNTRY_NAME = models.CharField(max_length=40)

    def __str__(self):
        return self.COUNTRY_NAME


class STATE(models.Model):
    COUNTRY_ID = models.ForeignKey(COUNTRY,on_delete=models.CASCADE)
    STATE_NAME = models.CharField(max_length=40)

    def __str__(self):
        return self.STATE_NAME

class CITY(models.Model):
    State_ID = models.ForeignKey(STATE,on_delete= models.CASCADE)
    CITY_NAME = models.CharField(max_length=40)
    def __str__(self):
         return self.CITY_NAME

class BANK_DETAIL(models.Model):
    U_ID = models.ForeignKey(USER_DETAIL,on_delete=models.CASCADE)
    BANK_NAME = models.CharField(max_length=40)
    DIGIT_N0 = models.IntegerField()
    END_MONTH = models.IntegerField(choices=ENDMONTHLIST)
    END_YEAR = models.IntegerField(choices=ENDYEARLIST)

class USER_ADDRESS(models.Model):
    U_ID = models.ForeignKey(USER_DETAIL,on_delete=models.CASCADE)
    BUILDING_NAME = models.CharField(max_length=40)
    STREET_NAME = models.CharField(max_length=30)
    CITY_NAME_ONLY = models.ForeignKey(CITY,on_delete=models.CASCADE)
    PIN_CODE = models.IntegerField()


