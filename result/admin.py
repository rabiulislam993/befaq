from django.contrib import admin

from result.models import Result



class ResultAdmin(admin.ModelAdmin):
    exclude = ['total_num','average_num','grade']
    raw_id_fields = ('student',)

admin.site.register(Result, ResultAdmin)