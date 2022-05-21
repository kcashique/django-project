from django.contrib import admin
from core.custom_admin import CustomAdmin
from .models import Job, Company, Department


@admin.register(Job)
class JobAdmin(CustomAdmin):
    pass

@admin.register(Company)
class CompanyAdmin(CustomAdmin):
    pass

@admin.register(Department)
class DepartmentAdmin(CustomAdmin):
    pass
