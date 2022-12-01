from django.contrib import admin
from app.models import JobPost, Location, Author, Skills


class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'salary',)
    list_filter = ['salary']
    search_fields = ['title']
    search_help_text = "Masukkan kata pencarian"
    # fields = ['title']
    exclude = ['slug']
    fieldsets = (
        ('Basic Information', {
            "fields": (
                'title','description'
            ),
        }),('More Information', {
            "classes" : ('collapse',),
            "fields": (
                'expiry','salary'
            ),
        })
    )
    

# Register your models here.
admin.site.register(JobPost)
admin.site.register(Location)
admin.site.register(Author)
admin.site.register(Skills)