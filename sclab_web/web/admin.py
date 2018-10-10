from django.contrib import admin
from .models import *

from django_summernote.admin import SummernoteModelAdmin

# Apply summernote to all TextField in model.
class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'

# Register your models here.
admin.site.register(Lab)
admin.site.register(Professor)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Lecture)
admin.site.register(Member)
admin.site.register(Post, SomeModelAdmin)
admin.site.register(Publication)
admin.site.register(Project)
admin.site.register(Link)
