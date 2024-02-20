from django.contrib import admin
from appUser.models import *


# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    '''Admin View for Profile'''

    list_display = ('user','title','isview','id', 'isnew', 'islogin') # hangilerini görüntülemek istediğini gösterir
    list_editable = ('isview', 'isnew', 'islogin')
    # list_filter = ('',) # filtreleme
    readonly_fields = ('title',)
    search_fields = ('user__username',)
    # date_hierarchy = '' # tarih çizelgesi
    # ordering = ('',) # sıralama




