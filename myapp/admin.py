from django.contrib import admin
from .models import ROLE,USER_DETAIL,USER_ADDRESS,CITY,COUNTRY,STATE,BANK_DETAIL

class showROLE(admin.ModelAdmin):
    list_display = ['USER_TYPENAME']
admin.site.register(ROLE,showROLE)

class showUSER_DETAIL(admin.ModelAdmin):
    list_display = ['U_NAME','U_PASSWORD','U_EMAIL','U_PHONE','U_TYPE','U_STATUS']
admin.site.register(USER_DETAIL,showUSER_DETAIL)

class showBANK_DETAIL(admin.ModelAdmin):
    list_display = ['U_ID','BANK_NAME','DIGIT_N0','END_MONTH','END_YEAR']
admin.site.register(BANK_DETAIL,showBANK_DETAIL)
class showCOUNTRY(admin.ModelAdmin):
    list_display = ['COUNTRY_NAME']
admin.site.register(COUNTRY,showCOUNTRY)

class showUSER_ADDRESS(admin.ModelAdmin):
    list_display = ['U_ID','BUILDING_NAME','STREET_NAME','CITY_NAME_ONLY','PIN_CODE']
admin.site.register(USER_ADDRESS,showUSER_ADDRESS)

class showCITY(admin.ModelAdmin):
    list_display = ['State_ID','CITY_NAME']
admin.site.register(CITY,showCITY)

class showSTATE(admin.ModelAdmin):
    list_display = ['COUNTRY_ID','STATE_NAME']
admin.site.register(STATE,showSTATE)
