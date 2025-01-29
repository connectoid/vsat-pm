from django.contrib import admin

from .models import Customer, Client, Task, WorkType


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'is_operator', 'contact_person_name') 
    search_fields = ('name',) 
    list_filter = ('is_operator',) 


class ClientAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'contact_person_name') 
    search_fields = ('name',) 


class WorkTypesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description', 'base_price') 
    search_fields = ('title',) 


class TaskAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'customer') 
    search_fields = ('title',) 
    list_filter = ('customer',) 


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(WorkType, WorkTypesAdmin)
admin.site.register(Task, TaskAdmin)