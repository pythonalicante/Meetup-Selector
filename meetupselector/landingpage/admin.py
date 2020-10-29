from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin
from .models import Content


class ContentAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')
    list_display = (
        'title',
        'date_added'
    )
    readonly_fields = ('date_added',)


admin.site.register(Content, ContentAdmin)
