from django.contrib import admin

from student.models import Student
from result.models import Result


class ResultInline(admin.StackedInline):
    model = Result
    exclude = ['total_num','average_num','grade']

class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','reg_year','name','madrasa','marhala','registrar','is_active']
    list_display_links = ['id','name']
    list_filter = ['result__grade', 'reg_year','marhala','is_active']
    search_fields = ['id','name']
    inlines = [ResultInline]

    # fields = [('name','father'),'address',('reg_year','marhala'), ('madrasa','markaz')]
    fieldsets = (
        ("Student's Personal Info", {
            'fields': (('name', 'father'), 'address','is_active')
        }),
        ('Registration Info', {
            'fields': (('reg_year','marhala'), ('madrasa','markaz'))
        }),
    )


admin.site.register(Student, StudentAdmin)